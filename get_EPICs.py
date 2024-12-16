import requests
import os


from datetime import datetime
from dotenv import load_dotenv
from pathlib import Path


def download_EPICs(filepath, api_key):
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    params = {
        'api_key': api_key,
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    epics = response.json()
    image_url_template = 'https://epic.gsfc.nasa.gov/archive/natural/{}/{}/{}/png/{}.png'
    image_template = 'NASA_EPIC{}.png'
    for epic_number, epic in enumerate(epics):
        date = epic['date']
        image_name = epic['image']
        datetime_date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
        image_url = image_url_template.format(datetime_date.year, datetime_date.month, datetime_date.day, image_name)
        response = requests.get(image_url, params=params)
        filename = image_template.format(epic_number)
        image_path = os.path.join(filepath, filename)
        with open(image_path, 'wb') as file:
            file.write(response.content)


def main():
    load_dotenv()
    api_key = os.getenv('NASA_API_TOKEN')
    relative_path = Path('DEVMAN_TASKS/Space/images/NASA')
    absolute_path = relative_path.resolve()
    Path(absolute_path).mkdir(parents=True, exist_ok=True)
    download_EPICs(absolute_path, api_key)


if __name__ == '__main__':
    main()
