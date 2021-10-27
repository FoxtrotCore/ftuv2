import os
import csv
import argparse
from .classifier import Classifier
from . import APP_NAME, APP_DESCRIPTION


def train(args):
    pass

def test(args):
    pass


def main():
    parser = argparse.ArgumentParser(prog=APP_NAME, description=APP_DESCRIPTION)
    parser.add_argument('-tn', '--training-data',
                        dest='training_data_path',
                        type=str,
                        help='Path to the training data')
    parser.add_argument('-tt', '--testing-data',
                        dest='testing_data_path',
                        type=str,
                        help='Path to the testing data')
    parser.add_argument('action',
                        type=str,
                        choices=['train', 'test'],
                        default='train',
                        help='Which mode to run the model in.')
    args = parser.parse_args()

    # Determine the action then run it
    mode = {
        'train': train,
        'test': test
    }[args.action]
    mode(args)
