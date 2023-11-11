# Pose Estimation API

## Introduction

The Pose Estimation API is a REST API that allows the caller to estimates poses based on images.

## REST Endpoints

URL:

`POST: /poses/estimation`

Payload:

`{
    "image": imageAsBase64
}`

Response:

`{
    "estimated_pose": "ROCK|PAPER|SCISSOR"
    "confidence": "confidence, number"
    "error": "error that occurred"
}`

## How to use

Call the start_api.cmd to start the API

## How to test

Run the tests with `pytest` or if you're using VSCode, run the demo.rest file (after installing the REST extension).