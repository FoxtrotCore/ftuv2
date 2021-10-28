import os
import csv
import math
import psutil
import argparse
import cv2.cv2 as c
from .classifier import Classifier
from . import APP_NAME, APP_DESCRIPTION


UNITS = {
    'B': 0,
    'KB': 1,
    'MB': 2,
    'GB': 3,
    'TB': 4
}


def trunc_mem_usage() -> str:
    process = psutil.Process(os.getpid())
    net_usage = process.memory_info().rss

    mem_unit = 'N/A'
    mem_usage = -1

    for unit, exp in UNITS.items():
        usage = math.floor(net_usage / 1024 ** exp)
        if(usage < 1):
            break
        mem_unit = unit
        mem_usage = usage

    return f'{mem_usage} {mem_unit}'


def max_usage_exceeded(limit: str) -> bool:
    process = psutil.Process(os.getpid())
    net_usage = process.memory_info().rss

    limit_usage = int(limit.split(' ')[0])
    limit_unit = limit.split(' ')[1].upper()
    exp = UNITS[limit_unit]
    net_limit = limit_usage * (1024 ** exp)

    return net_usage > net_limit



def train(classifier: Classifier):
    print('Starting training mode!')
    print(classifier)


def test(classifier: Classifier):
    print('Starting testing mode!')
    print(classifier)


def main():
    parser = argparse.ArgumentParser(prog=APP_NAME, description=APP_DESCRIPTION)
    parser.add_argument('-tn', '--training-labels',
                        dest='training_data_path',
                        type=str,
                        help='Path to the training data')
    parser.add_argument('-tt', '--testing-labels',
                        dest='testing_data_path',
                        type=str,
                        help='Path to the testing data.')
    parser.add_argument('-m', '--max-mem-usage',
                        dest='max_mem_usage',
                        type=str,
                        help='Set a limit for maximum amount of memory used. (Throttles loaded data set).')
    parser.add_argument('action',
                        type=str,
                        choices=['train', 'test'],
                        default='train',
                        help='Which mode to run the model in.')
    parser.add_argument('frames_dir',
                        type=str,
                        help='Path to the directory of frames.')
    args = parser.parse_args()

    # Fetch the correct labels file
    label_file = {
        'train': args.training_data_path,
        'test': args.testing_data_path
    }[args.action]

    if(label_file is None):
        raise Exception(f'{args.action} action expects the correct labels-file to also be specified!')

    # Load in the labels
    labels = []
    with open(label_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            labels.append(row)
    labels = labels[1:] # Toss the header row
    print(f'Gathered {len(labels)} labels for {args.action} mode!')

    # Fetch the mem limit info
    has_limit = args.max_mem_usage is not None

    # Load in the necessary frames
    frames = []
    for label in labels:
        # Load a frame
        path = f'{args.frames_dir}/{label[0]}-frame.png'
        if(not os.path.exists(path)):
            raise Exception(f'Expected file to exist: {path}')
        frame = c.imread(path)
        if(frame is None):
            raise Exception(f'Failed to load frame: {path}')
        frames.append(frame)

        # Get and display ative memory usage
        print(f'Using {trunc_mem_usage()} of memory!')

        if(has_limit and max_usage_exceeded(args.max_mem_usage.upper())):
            print(f'{trunc_mem_usage()}/{args.max_mem_usage.upper()} memory has been used! Ending frame loading!')
            break
    print(f'Loaded {len(frames)} frames from disk!')

    # Create the classifier
    classifier = Classifier(labels, frames)

    # Determine the action then run it
    mode = {
        'train': train,
        'test': test
    }[args.action]
    mode(classifier)
