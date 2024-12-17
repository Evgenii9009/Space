import telegram
import os
import argparse
import time
import random


from dotenv import load_dotenv
from pathlib import Path


def create_parser():
    parser = argparse.ArgumentParser(description='Скрипт предназначен для автоматической публикации фото в телеграм-канал')
    parser.add_argument('--time', default=14400)
    parser.add_argument('--image_path', default='')
    return parser


def get_file_paths(directory):
    return [os.path.join(root, filename) for root, _, files in os.walk(directory) for filename in files]


def send_photos(filepaths, bot, sleeping_time, chat_id):
    while True:
        for filepath in filepaths:
            with open(filepath, 'rb') as file:
                bot.send_photo(chat_id=chat_id, photo=file)
                time.sleep(sleeping_time)
                file.close()


def main():
    load_dotenv()
    chat_id = os.getenv('CHAT_ID')
    relative_path = Path('DEVMAN_TASKS/Space/images')
    absolute_path = relative_path.resolve()
    filepaths = get_file_paths(absolute_path)
    random.shuffle(filepaths)
    args = create_parser().parse_args()
    sleeping_time = args.time
    image_path = args.image_path
    tg_token = os.getenv('TG_TOKEN')
    bot = telegram.Bot(tg_token)
    if image_path:
        bot.send_photo(chat_id=chat_id, photo=open(image_path, 'rb'))
        time.sleep(sleeping_time)
    send_photos(filepaths, bot, sleeping_time, chat_id)


if __name__ == '__main__':
    main()
