# Use an official Node.js runtime as a parent image
FROM node:14

# Set the working directory
WORKDIR .

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install app dependencies
RUN npm install

# Copy the content of the current directory to the working directory in the container
COPY GAPP.js .
COPY views views

# Expose the port the app runs on
EXPOSE 4000

# Define the command to run your app
CMD ["node", "GAPP.js"]
