import os
import argparse
import cv2.cv2 as c
from .video_loader import VideoLoader
from . import APP_NAME, APP_DESCRIPTION

def main():
    parser = argparse.ArgumentParser(prog=APP_NAME, description=APP_DESCRIPTION)
    parser.add_argument('-d', '--destination',
                        dest='dest_path',
                        type=str,
                        default='~/Documents/ftf/training-set')
    parser.add_argument('video_path',
                        type=str,
                        help='Path to the video to analyze')
    args = parser.parse_args()
    dest_path = os.path.expanduser(args.dest_path)
    os.makedirs(dest_path, exist_ok=True)

    try:
        with VideoLoader(args.video_path) as video:
            for i, frame in video:
                c.imwrite(f'{dest_path}/{i}-frame.png', frame)
    except KeyboardInterrupt:
        print('Goodbye!')
