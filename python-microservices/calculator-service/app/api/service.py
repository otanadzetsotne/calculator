import os
import httpx

TAG_SERVICE_HOST_URL = 'http://localhost:8002/api/tags/'
url = os.environ.get('TAG_SERVICE_HOST_URL') or TAG_SERVICE_HOST_URL


def tag_exists(tag_id: int):
    r = httpx.get(f'{url}{tag_id}')
    return True if r.status_code == 200 else False
