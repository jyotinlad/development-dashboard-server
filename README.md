# Development Dashboard Server

## Overview
A backend API service..

## Setup

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