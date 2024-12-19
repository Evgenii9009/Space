import requests
import argparse


from pathlib import Path
from functions import check_and_save


def fetch_spacex_last_launch(filepath, launch_id):
    url = 'https://api.spacexdata.com/v5/launches/{}'
    launch_url = url.format(launch_id)
    response = requests.get(launch_url)
    response.raise_for_status()
    image_links = response.json()['links']['flickr']['original']
    image_template = 'spaceX{}{}'
    for link_number, link in enumerate(image_links):
        response = requests.get(link)
        extension = '.jpeg'
        check_and_save(response, image_template, link_number, extension, filepath)


def create_parser():
    parser = argparse.ArgumentParser(description='Скрипт предназначен для скачивания фото с последнего запука ракеты SpaceX')
    parser.add_argument('--launch_id', default='5eb87d47ffd86e000604b38a')
    return parser


def main():
    relative_path = Path('DEVMAN_TASKS/Space/images/SpaceX')
    absolute_path = relative_path.resolve()
    Path(absolute_path).mkdir(parents=True, exist_ok=True)
    launch_id = create_parser().parse_args().launch_id
    fetch_spacex_last_launch(absolute_path, launch_id)


if __name__ == '__main__':
    main()
