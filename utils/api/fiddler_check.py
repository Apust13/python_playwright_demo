import socket

def is_fiddler_running(host='127.0.0.1', port=8888, timeout = 1):
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except (socket.timeout, ConnectionRefusedError):
        return False



