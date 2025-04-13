# Use an official Node runtime as a parent image
# Use an LTS version matching your local Node version if possible (e.g., 20)
FROM node:20-alpine

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json (or yarn.lock) first
# This leverages Docker cache for dependencies
COPY package*.json ./
# If using yarn, copy yarn.lock instead

# Install dependencies
RUN npm install
# If using yarn, use: RUN yarn install

# Copy the rest of the application code
COPY . .

# Build the Next.js application (optional but good practice for production)
# For development, we often run the dev server directly.
# We can create multi-stage builds later for optimized production images.
# RUN npm run build

# Expose the port the Next.js app runs on (default is 3000)
EXPOSE 3000

# Define the command to run the development server
# Host 0.0.0.0 is important to accept connections from outside the container
CMD ["npm", "run", "dev", "--", "-p", "3000", "-H", "0.0.0.0"]