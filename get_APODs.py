import requests
import os
import urllib


from os.path import splitext
from dotenv import load_dotenv
from pathlib import Path
from functions import check_and_save, define_extension


def download_APODs(filepath, api_key):
    url = 'https://api.nasa.gov/planetary/apod'
    images_amount = 30
    params = {
        'api_key': api_key,
        'count': images_amount
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    apods = response.json()
    image_template = "NASA_APOD{}{}"
    for apod_number, apod in enumerate(apods):
        image_url = apod['url']
        extension = define_extension(image_url)
        try:
            response = requests.get(image_url)
        except requests.exceptions.MissingSchema:
            continue
        check_and_save(response, image_template, apod_number, extension, filepath)


def main():
    load_dotenv()
    relative_path = Path('DEVMAN_TASKS/Space/images/NASA')
    absolute_path = relative_path.resolve()
    api_key = os.getenv('NASA_API_TOKEN')
    Path(absolute_path).mkdir(parents=True, exist_ok=True)
    download_APODs(absolute_path, api_key)


if __name__ == '__main__':

    main()
