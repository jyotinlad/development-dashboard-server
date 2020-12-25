# Development Dashboard Server

## Overview
A backend API service..

![Python Package](https://github.com/jyotinlad/development-dashboard-server/workflows/Python%20Package/badge.svg)

## Setup

### Env File
Create and modify the `.env` file in the repostory. Reference the `.env_sample` file for the requirement parameters.

### Docker

List Images: 

`docker images`

Build Image: 

`docker build -t development-dashboard-server:latest . `

List Deployments:

`docker ps`

Deploy Container:

`docker run -d --restart always -p 2800:2800 development-dashboard-server` (port mapping from docker 2800 to flask server 2800)

Stop Container:

`docker stop <container>`

## Unit Tests

TODO..