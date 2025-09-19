from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent
DATA_DIR = ROOT_DIR/'data'
USER_FILE_PATH = DATA_DIR / 'users.txt'

print(USER_FILE_PATH)
