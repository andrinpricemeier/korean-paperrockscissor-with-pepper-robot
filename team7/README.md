![](readme_images/banner.jpg)
# Dibi-shi

## Instructions on how to run this behavior

1. Install all dependencies
1. Install the activities by opening the activities project in Choreographe and install the project on pepper
1. Run start_api.cmd in pose_estimation_api. This starts the REST API for pose estimation
1. Run main.py in game_logic_service/runner. This registers the dibi service which in turn starts the game

** Important note for PyCharm users: To run main.py, the run configuration has to be edited. Interpreter options: `-m runner.main` **

## Testing

The pose estimation and game logic service have pytest-tests written. They can be run by changing to the corresponding folder and running:

`python -m pytest`

## Logging

The project uses the default logging package provided by Python. The pose estimation and game logic service have a logger.conf for this purpose.

## Configuration

The project uses the default configparser provided by Python. There's an api.conf for the pose estimation API and a dibi.conf for the game logic service (in the runner subfolder).


## Project structure

* activites: the custom solitary/interactive activies in the form of a Choreographe project
* game_logic_service: the implementation of the dibi game, activated by calling the service through an interactive activity
* libraries: the pepper wrappers
* pose_estimation_api: the pose estimation REST API
* testat: examples for using the tablet

### Game logic service

This package implements the dibi game. Packages and their function:

* actuators: all classes and functions related with acting/outputting some action
* agent_logic: the state machine controlling the entire game flow
* game_logic: the dibi game logic. Care has been taken to decouple the core game logic from the pepper platform so that it is easier to test.
* runner: the pepper service and entry point
* sensors: sensors for the environment
* tests: tests that can be run with python -m pytest in the game_logic_service folder
* utils: various utilities

### Pose Estimation API

This package has an REST API for estimating a pose. It's in a separate project because the MediaPipe library requires Python 3+.

![](readme_images/footer.jpg)