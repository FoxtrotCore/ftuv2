from __future__ import annotations
import cv2.cv2 as c

class VideoLoader:
    def __init__(self: VideoLoader, path: str):
        self.video = c.VideoCapture(path)


    def __iter__(self: VideoLoader) -> VideoLoader:
        self.frame_number = 0
        return self

    def __next__(self: VideoLoader) -> tuple:
        if(not self.video.isOpened()):
            raise StopIteration()

        is_frame, image = self.video.read()


        if(is_frame):
            current_frame = self.frame_number
            self.frame_number += 1
            return current_frame, image
        else:
            raise StopIteration
