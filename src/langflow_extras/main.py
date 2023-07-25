from pathlib import Path
import os
from dotenv import load_dotenv, find_dotenv


def run_langflow_extras():
    from langflow.__main__ import main

    components_path = Path(__file__).parent / "components"
    os.environ["LANGFLOW_COMPONENT_PATH"] = str(components_path)
    load_dotenv(find_dotenv())
    main()


if __name__ == "__main__":
    run_langflow_extras()
