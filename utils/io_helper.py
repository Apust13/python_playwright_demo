from paths import USER_FILE_PATH


def save_credentials(email: str, password: str):
    with open(USER_FILE_PATH, 'a', encoding='utf-8') as f:
        f.write(f'{email}:{password}\n')


def read_credentials() -> list[str]:
    try:
        with open(USER_FILE_PATH, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        # return []
        raise FileNotFoundError('File users.txt is absent')


def get_creds(count: int | None = None) -> list[dict[str, str]]:
    raw_lines = read_credentials()

    if count is not None:
        raw_lines = raw_lines[-count:]

    creds = []
    for line in raw_lines:
        try:
            email, password = line.split(':', 1)
            creds.append({'email': email, 'password': password})
        except ValueError:
            continue
    # if len(creds) == 0:
    #     raise ValueError('No valid credentials found in users.txt')

    return creds

def get_credential() -> dict:
    return get_creds(count=1)[0]

def remove_credentials(email: str, password: str):
    try:
        with open(USER_FILE_PATH, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f if line.strip()]

        target = f'{email}:{password}'.strip()
        filtered = [line for line in lines if line != target]

        with open(USER_FILE_PATH, 'w', encoding='utf-8') as f:
            f.write('\n'.join(filtered) + '\n')

    except FileNotFoundError:
        pass