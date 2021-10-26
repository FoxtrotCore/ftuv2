import argparse
from . import APP_NAME

def main():
    parser = argparse.ArgumentParser(prog=APP_NAME)
    parser.add_argument('video_file_path',
                        help='Path to the video file to analyze.')
    args = parser.parse_args()

    print(args)
