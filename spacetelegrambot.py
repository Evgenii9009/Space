import telegram
import os
import argparse
import time
import random


from dotenv import load_dotenv


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('time', default='14400')
    parser.add_argument('image_path', default='')
    return parser


def get_file_paths(directory):
    return [os.path.join(root, filename) for root, _, files in os.walk(directory) for filename in files]


def send_photos(filepaths, bot, sleeping_time):
    while True:
        for filepath in filepaths:
            bot.send_photo(chat_id=-1002293261601, photo=open(filepath, 'rb'))
            time.sleep(sleeping_time)

def main():
    load_dotenv()
    filepaths = get_file_paths('/home/eugene/DEVMAN_TASKS/Space/images')
    random.shuffle(filepaths)
    sleeping_time = create_parser().parse_args().time
    image_path = create_parser().parse_args().image_path
    tg_token = os.getenv('TG_TOKEN')
    bot = telegram.Bot(tg_token)
    if image_path:
        bot.send_photo(chat_id=-1002293261601, photo=open(image_path, 'rb'))
        time.sleep(sleeping_time)
    send_photos(filepaths, bot, sleeping_time)


if __name__ == '__main__':
    main()
