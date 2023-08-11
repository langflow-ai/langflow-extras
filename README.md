# Langflow-Extras Template Repository

This repository is a template for creating new repositories for Langflow-Extras. It contains the necessary files and folders to get started with creating a new Langflow-Extras repository.

## Getting Started

Install Poetry:

Follow the steps in the [Poetry documentation](https://python-poetry.org/docs/) to install Poetry.

Install the dependencies:

```bash
poetry install
```

## Extending Langflow-Extras

Add new components to the folder `src/langflow_extras/components`. Each component should be in its category folder (almost always `custom_components`) and the component should subclass `langflow.interface.custom.custom_component.CustomComponent`

There is an example component in `src/langflow_extras/components/custom_components/ComponentExample.py` that you can use as a template.

Documentation for the CustomComponent can be found in Langflow's [documentation](https://langflow.org).

Any other modules you need to add can be added normally using poetry.

## Usage

To run Langflow-Extras, run the following command:

```bash
poetry run python -m langflow serve
```

## Docker

There is a Dockerfile included in this repository.
To run Langflow-Extras in a Docker container, run the following command:

```bash
docker build -t langflow-extras .
docker run -p 5352:5352 -it langflow-extras
```
