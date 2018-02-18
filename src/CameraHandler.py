#!/usr/bin/env python

'''
   Class to handle the interaction with the computer's webcam
'''

import cv2


class CameraHandler:
    def __init__(self, cameraPort):
        # Define our constants
        self.INITIAL_FRAME_DISCARD = 30

        # Object variables
        self.cameraPort = cameraPort

        # Connect to the webcam
        self.camera = cv2.VideoCapture(self.cameraPort)

        # Throw away the first bunch of pictures as the camera adjusts
        for i in xrange(self.INITIAL_FRAME_DISCARD):
            _, _ = self.camera.read()

    # Grab an image from the webcam
    def grab_image(self):
        _, self.last_image = self.camera.read()

        return self.last_image

    # Release our lock on the camera
    def release_camera(self):
        del(self.camera)

        return
