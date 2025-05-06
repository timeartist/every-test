# every.org coding challenge

This is a simple webapp that helps people find (and donate to) non-profits that align with their interests.

## Installation

This is built using Python3, Poetry, Flask and Requests.  [Install poetry using the instructions on their website](https://python-poetry.org/docs/#installation)

Once Poetry is installed, you can install the dependancies by running `poetry install` inside the root folder of this application.

## Run

This requires an API key from every.org to run.  You can get one [here](every.org/developer).

Set the API key to env var `EVERY_ORG_API_KEY="YOUR_API_KEY"`

Run the application using Poetry.  `poetry run python3 webapp.py`

