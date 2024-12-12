import requests
import os


from datetime import datetime
from dotenv import load_dotenv
from pathlib import Path


def download_EPICs(filepath):
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    params = {
        'api_key': os.getenv('NASA_API_TOKEN'),
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    epics = response.json()
    image_url_template = 'https://epic.gsfc.nasa.gov/archive/natural/{}/{}/{}/png/{}.png'
    image_template = 'NASA_EPIC{}.png'
    for epic_number, epic in enumerate(epics):
        date = epic['date']
        image_name = epic['image']
        datetime_date = strptime(date)
        image_url = image_url_template.format(datetime_date.year, datetime_date.month, datetime_date.day, image_name)
        response = requests.get(image_url, params=params)
        filename = image_template.format(epic_number)
        image_path = os.path.join(filepath, filename)
        with open(image_path, 'wb') as file:
            file.write(response.content)


def strptime(date):
    datetime_object = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    return datetime_object


def main():
    load_dotenv()
    filepath = '/home/eugene/DEVMAN_TASKS/Space/images/NASA'
    Path(filepath).mkdir(parents=True, exist_ok=True)
    download_EPICs(filepath)


if __name__ == '__main__':
    main()
