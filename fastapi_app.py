import requests
import datetime
import time

def send_heartbeat():
    # Replace the URL with the actual URL of your FastAPI app
    url = "http://localhost:8000/post/car/hb"

    # Heartbeat data
    heartbeat_data = {"car_heartbeat_value": str(datetime.datetime.utcnow()), "car_id": "car1", "latitude": 50.073, "longitude": 14.418, "altitude": 400}

    # Send POST request to the FastAPI app
    response = requests.post(url, json=heartbeat_data)
    
    # Replace the URL with the actual URL of your FastAPI app
    url = "http://localhost:8000/post/car/hb"

    # Heartbeat data
    heartbeat_data = {"car_heartbeat_value": str(datetime.datetime.utcnow()), "car_id": "car2", "latitude": 50.073, "longitude": 14.418, "altitude": 400}

    # Send POST request to the FastAPI app
    response = requests.post(url, json=heartbeat_data)
    
    # Replace the URL with the actual URL of your FastAPI app
    url = "http://localhost:8000/post/car/hb"

    # Heartbeat data
    heartbeat_data = {"car_heartbeat_value": str(datetime.datetime.utcnow()), "car_id": "car3", "latitude": 50.073, "longitude": 14.418, "altitude": 400}

    # Send POST request to the FastAPI app
    response = requests.post(url, json=heartbeat_data)

    if response.status_code == 200:
        print("Heartbeat sent successfully")
    else:
        print(f"Failed to send heartbeat. Status code: {response.status_code}, Response: {response.text}")

def send_data():
    # Replace the URL with the actual URL of your FastAPI app
    url = "http://localhost:8000/post/car/data"

    # Heartbeat data
    data = {
    "GPS_RAW_INT": {
        "lat": "",
        "lon": "",
        "alt": "",
        "eph": "",
        "epv": "",
        "vel": "",
        "cog": "",
        "satellites_visible": "",
        "h_acc": "",
        "v_acc": ""
    },
    "GPS_RAW_INT_updated": "",
    "ATTITUDE": {
        "roll": "",
        "pitch": "",
        "yaw": "",
        "rollspeed": "",
        "pitchspeed": "",
        "yawspeed": ""
    },
    "ATTITUDE_updated": "",
    "ALTITUDE": {
        "altitude_amsl": "",
        "altitude_local": ""
    },
    "ALTITUDE_updated": "",
    "GLOBAL_POSITION_INT": {
        "lat": "1",
        "lon": "2",
        "alt": "3",
        "relative_alt": "",
        "vx": "4",
        "vy": "5",
        "vz": "6"
    },
    "GLOBAL_POSITION_INT_updated": "",
    "GPS_GLOBAL_ORIGIN": {
        "altitude": ""
    },
    "GPS_GLOBAL_ORIGIN_updated": "",
    "GPS_STATUS": {
        "satellites_visible": "",
        "satellite_used": ""
    },
    "GPS_STATUS_updated": "",
    "HOME_POSITION": {
        "latitude": "1",
        "longitude": "1",
        "altitude": "1"
    },
    "HOME_POSITION_updated": "",
    "HYGROMETER_SENSOR": {
        "id": "",
        "temperature": "",
        "humidity": ""
    },
    "HYGROMETER_SENSOR_updated": "",
    "TUNNEL": {
        "payload_length": 1,
        "payload": [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
        26,
        27,
        28,
        29,
        30,
        31,
        32,
        33,
        34,
        35,
        36,
        37,
        38,
        39,
        40,
        41,
        42,
        43,
        44,
        45,
        46,
        47,
        48,
        49,
        50,
        51,
        52,
        53,
        54,
        55,
        56,
        57,
        58,
        59,
        60,
        61,
        62,
        63,
        64,
        65,
        66,
        67,
        68,
        69,
        70,
        71,
        72,
        73,
        74,
        75,
        76,
        77,
        78,
        79,
        80,
        81,
        82,
        83,
        84,
        85,
        86,
        87,
        88,
        89,
        90,
        91,
        92,
        93,
        94,
        95,
        96,
        97,
        98,
        99,
        100,
        101,
        102,
        103,
        104,
        105,
        106,
        107,
        108,
        109,
        110,
        111,
        112,
        113,
        114,
        115,
        116,
        117,
        118,
        119,
        120,
        121,
        122,
        123,
        124,
        125,
        126,
        127
        ]
    },
    "tmp": "2023-12-01 19:00:18.323136",
    "latitude": 50.073,
    "longitude": 14.418,
    "altitude": 400,
    "lastPosUpdate": "",
    "car_id": "car1",
    "balloon_id": "fik_SiK"
    }


    # Send POST request to the FastAPI app
    response = requests.post(url, json=data)
    

    if response.status_code == 200:
        print("Data sent successfully")
    else:
        print(f"Failed to send data. Status code: {response.status_code}, Response: {response.text}")


if __name__ == "__main__":
    # Send a heartbeat every 5 seconds (adjust as needed)
    while True:
        # send_heartbeat()
        send_data()
        time.sleep(5)
