import requests
import os
import argparse
from pathlib import Path


def fetch_spacex_last_launch(filepath, launch_id):
    url = 'https://api.spacexdata.com/v5/launches/{}'
    launch_url = url.format(launch_id)
    response = requests.get(launch_url)
    response.raise_for_status()
    image_links = response.json()['links']['flickr']['original']
    image_template = 'spaceX{}.jpeg'
    for link_number, link in enumerate(image_links):
        filename = image_template.format(link_number)
        image_path = os.path.join(filepath, filename)
        response = requests.get(link)
        response.raise_for_status()
        with open(image_path, 'wb') as file:
            file.write(response.content)


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('launch_id', default='latest')
    return parser


def main():
    filepath = '/home/eugene/DEVMAN_TASKS/Space/images/SpaceX'
    Path(filepath).mkdir(parents=True, exist_ok=True)
    launch_id = create_parser().parse_args().launch_id
    fetch_spacex_last_launch(filepath, launch_id)


if __name__ == '__main__':
    main()
