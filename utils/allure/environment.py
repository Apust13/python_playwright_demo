import platform
from datetime import datetime

from config import settings

def create_allure_environment_file():
    system_info = {
        "OS": platform.system(),
        "OS_Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
        "Python_Version": platform.python_version(),
        "Run_Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

    env_info = {
        "API_Base_URL": settings.http_client.client_url,
        "API_Timeout": settings.http_client.timeout,
        "App_URL": settings.app_url,
        "Headless": settings.headless,
        "Browsers": ", ".join(settings.browsers),
    }

    combined = {**system_info, **env_info}
    lines = [f"{key}={value}" for key, value in combined.items()]
    properties = "\n".join(lines)

    with open(settings.allure_results_dir.joinpath('environment.properties'), 'w+') as file:
         file.write(properties)