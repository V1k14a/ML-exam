import os
from dotenv import load_dotenv

script_dir = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(script_dir, '.env')
load_dotenv(dotenv_path=env_path)

api_key = os.getenv("MY_API_KEY")

if not api_key:
    print(f"Error: API KEY not found in {env_path}")
    exit(1)

llm_config = {
    "config_list": [
        {
            "model": "open-mistral-nemo",
            "api_key": api_key,
            "api_type": "mistral",
            "api_rate_limit": 0.25,
            "repeat_penalty": 1.1,
            "temperature": 0.5,
            "seed": 42,
        }
    ]
}