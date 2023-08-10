import json
from pathlib import Path
import os
from dotenv import load_dotenv, find_dotenv
from langflow.__main__ import (
    app as existing_app,
    # main as existing_main,
)  # Import the original app


@existing_app.callback(invoke_without_command=True)
def run():
    components_path = Path(__file__).parent / "components"
    os.environ["LANGFLOW_COMPONENTS_PATH"] = json.dumps([str(components_path)])
    load_dotenv(find_dotenv())


def main():
    existing_app()  # Run the existing app


if __name__ == "__main__":
    main()
