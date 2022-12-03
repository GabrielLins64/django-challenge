# pull official base image
FROM node:18-alpine3.15

# Argument parameter
ARG app_env
ENV APP_ENV $app_env

# set working directory
WORKDIR /code

# install app dependencies
COPY package.json ./
COPY package-lock.json ./
RUN npm install --silent

# add app
COPY . /code
