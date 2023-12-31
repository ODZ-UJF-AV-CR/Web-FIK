import asyncio
import json
from fastapi import FastAPI, APIRouter, Depends, Request
from fastapi.responses import JSONResponse
import requests
import datetime
from sondehub.amateur import Uploader

app = FastAPI()
router = APIRouter()

#express_base_url = "http://localhost:4000"
express_base_url = "https://fik.crreat.eu"

car_dict = {}

uploader_data = Uploader("SlimonTest", uploader_position=[50.073, 14.418, 400])

global existing_timestamp_str

existing_timestamp_str = None

def send_data_to_express(endpoint: str, data: dict):
    try:
        url = f"{express_base_url}{endpoint}"
        response = requests.post(url, json=data)
        return response
    except:
        print("Error couldnt send data to GAPP")
        return {"message": "Error"}

def send_hb_to_express(endpoint: str, data: dict):
    try:
        url = f"{express_base_url}{endpoint}"
        response = requests.post(url, json=data)
        return response
    except:
        print("Error couldnt send data to GAPP")
        return {"message": "Error"}

def start_background_task():
    async def send_cdp_heartbeat():
        while True:
            date = datetime.datetime.utcnow()
            cdp_heartbeat_data = {"cdp_heartbeat_value": str(date)}
            response = send_hb_to_express("/post/cdp/hb", cdp_heartbeat_data)
            await asyncio.sleep(10)

    asyncio.create_task(send_cdp_heartbeat())

def on_shutdown():
    print("Shutting down...")
    uploader_data.close()
    for i in car_dict:
        print(i, ":", car_dict[i])
        car_dict[i].close()

def is_newer_timestamp(received_data: dict):
    global existing_timestamp_str
    received_timestamp_str = received_data.get("tmp")
    if received_timestamp_str:
        received_timestamp = datetime.datetime.strptime(received_timestamp_str, "%Y-%m-%d %H:%M:%S.%f")
        if existing_timestamp_str:
            existing_timestamp = datetime.datetime.strptime(existing_timestamp_str, "%Y-%m-%d %H:%M:%S.%f")
            return received_timestamp > existing_timestamp
        else:
            return True
    return False

@router.post("/post/car/hb")
async def forward_heartbeat(request: Request):
    data = await request.json()
    car_id = data.get("car_id")
    latitude = data.get("latitude")
    longitude = data.get("longitude")
    altitude = data.get("altitude")
    if (not car_id in car_dict):
        car_dict[car_id] = Uploader(car_id)
        print(car_dict) 
    car_dict[car_id].upload_station_position(
        "fik-" + car_id,
        [latitude, longitude, altitude],
        mobile=True
    )
    response = send_data_to_express("/post/car/hb", data)
    print(response.json())
    return {"message": "Heartbeat data received and forwarded successfully"}

@router.post("/post/car/data")
async def forward_data(request: Request):
    global existing_timestamp_str
    data = await request.json()
    balloon_id = data.get("balloon_id")
    latitude = data.get("latitude")
    longitude = data.get("longitude")
    altitude = data.get("altitude")
    if is_newer_timestamp(data):
        response = send_data_to_express("/post/car/data", data)
        print("Received data is newer than the existing data.")
        uploader_data.add_telemetry(
            "fik-" + balloon_id,
            datetime.datetime.utcnow(),
            latitude,
            longitude,
            altitude
        )
        existing_timestamp_str = data.get("tmp")
        return {"message": "Data data received and forwarded successfully"}
    else:
        response = send_data_to_express("/post/car/data", data)
        print("Received data is not newer than the existing data.")
        return {"message": "Data is not forwarded because it's not newer."}


try:
    app.include_router(router)
    app.add_event_handler("shutdown", on_shutdown)
    start_background_task()

except KeyboardInterrupt as e:
    print("Ended with ctrl+c")
finally:
    pass
