import telegram
import os
import argparse
import time
import random


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('time', default='14400')
    return parser


def get_file_paths(directory):
    return [os.path.join(root, filename) for root, _, files in os.walk(directory) for filename in files]


def main():
    filepaths = get_file_paths('/home/eugene/DEVMAN_TASKS/Space/images')
    random.shuffle(filepaths)
    print(filepaths)
    sleeping_time = create_parser().parse_args().time
    tg_token = os.getenv('TG_TOKEN')
    for filepath in filepaths:
        bot = telegram.Bot(tg_token)
        bot.send_photo(chat_id=-1002293261601, photo=open(filepath, 'rb'))
        time.sleep(sleeping_time)


if __name__ == '__main__':
   main()
