#!/usr/bin/env python3
import csv
import math
import argparse


def main():
    parser = argparse.ArgumentParser(prog='Training And Test Frame Organizer')
    parser.add_argument('--training-output',
                        dest='train_file',
                        type=str,
                        default='./training.csv',
                        help='Path to training-file output.')
    parser.add_argument('--test-output',
                        dest='test_file',
                        type=str,
                        default='./test.csv',
                        help='Path to test-file output.')
    parser.add_argument('-p', '--partition',
                        dest='training_partition',
                        type=float,
                        default=0.8,
                        help='Percentage of data to assign to training. (The rest is implicitly assigned to testing).')
    parser.add_argument('labels_file',
                        type=str,
                        help='Path to labels file to organize.')
    args = parser.parse_args()

    # Create the buckets
    frames = {}
    frames['2D'] = []
    frames['3D'] = []

    # Populate the buckets
    with open(args.labels_file, 'r') as file:
        reader = csv.reader(file)

        for row in reader:
            try:
                frame_number = int(row[0])
            except Exception:
                continue

            mode = row[1]
            frames[mode].append(frame_number)

    # Post analysis
    mid_2d = math.ceil(args.training_partition * len(frames['2D']))
    mid_3d = math.ceil(args.training_partition * len(frames['3D']))

    train_set_2d = frames['2D'][:mid_2d]
    test_set_2d = frames['2D'][mid_2d:]

    train_set_3d = frames['3D'][:mid_3d]
    test_set_3d = frames['3D'][mid_3d:]

    print(f'Training: {len(train_set_2d)} 2D Frames, {len(train_set_3d)} 3D Frames, {len(train_set_2d) + len(train_set_3d)} Total')
    print(f'Test: {len(test_set_2d)} 2D Frames, {len(test_set_3d)} 3D Frames, {len(test_set_2d) + len(test_set_3d)} Total')

    # Write the training set data
    with open(args.train_file, 'w+') as file:
        writer = csv.writer(file)
        writer.writerow(['frame-number', 'mode'])
        for frame_num in train_set_2d:
            writer.writerow([frame_num, '2D'])
        for frame_num in train_set_3d:
            writer.writerow([frame_num, '3D'])

    # Write the test set data
    with open(args.test_file, 'w+') as file:
        writer = csv.writer(file)
        writer.writerow(['frame-number', 'mode'])
        for frame_num in test_set_2d:
            writer.writerow([frame_num, '2D'])
        for frame_num in test_set_3d:
            writer.writerow([frame_num, '3D'])


if __name__ == '__main__':
    main()
