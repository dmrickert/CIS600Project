#!/usr/bin/env python

'''
   Class to handle the processing of the input from the webcam
'''

import cv2
import os


class ImageProcessor:
    def __init__(self, resourceFolder):
        # Haar Cascade that detects a faces
        self.face_cascade = cv2.CascadeClassifier(
            os.path.join(resourceFolder, 'haarcascade_frontalface_default.xml')
            )
        # Haar Cascade that detects eyes
        self.eye_cascade = cv2.CascadeClassifier(
            os.path.join(resourceFolder, 'haarcascade_eye.xml'))

        self.face = {}

        # Thresholds for when to turn text green and when to turn text red
        self.green_threshold = 0
        self.red_threshold = 10

    # Set color set_colors_thresholds
    def set_colors_thresholds(self, minLevel, maxLevel):
        self.green_threshold = minLevel
        self.red_threshold = maxLevel

    # Convert a raw webcam image to an image we want to process
    def convert_raw(self, image):
        #self.show_image(image)
        self.rawImage = image
        self.grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        return

    # Pull the face out of the picture (if it exists)
    def extract_face(self):
        # Use our HaarCaascade to find any faces
        self.faces = self.face_cascade.detectMultiScale(self.rawImage,
                                                        scaleFactor=1.1,
                                                        minNeighbors=16
                                                        )

        # If we didn't find any faces, let the caller know
        if not len(self.faces):
            return False

        # Only expect 1 face
        if len(self.faces) > 1:
            print('INFO: Multiple faces found... only taking 1.')

        # Grab teh first face that was found
        (x, y, w, h) = self.faces[0]

        # Draw a rectangel around the face
        cv2.rectangle(self.rawImage, (x, y), (x+w, y+h), (255, 0, 0), 2)
        self.face_gray = self.grayImage[y:y+h, x:x+w]
        self.face_color = self.rawImage[y:y+h, x:x+w]

        # Store these values for later
        self.face['x'] = x
        self.face['y'] = y
        self.face['w'] = w
        self.face['h'] = h

        # self.show_image(self.rawImage) # Shows the rectangle on the face
        # self.show_image(self.face_color) # Show only the face (in color)

        return True

    # Extract eyes off of the face
    def extract_eyes(self):
        # Use our HaarCaascade to find any eyes
        self.eyes = self.eye_cascade.detectMultiScale(self.face_gray,
                                                      scaleFactor=1.1,
                                                      minNeighbors=15
                                                      )

        if not len(self.eyes) >= 2:
            return False

        # Loop through each eye and draw our rectangles
        for (x, y, w, h) in self.eyes:
            # Shift eyes to match original image
            x = self.face['x'] + x
            y = self.face['y'] + y

            # Draw the eyes on the original image
            cv2.rectangle(self.rawImage,
                          (x, y), (x + w, y + h),
                          (0, 255, 0),
                          2)

        # self.show_image(self.face_color) # Show only the face (in color)

        return True

    # Show an image file
    def show_image(self, image, text='None', waitTime=50):
        # Add text to the image
        if text != 'None':
            text = 'Inattention Score: {}'.format(text)
            image = self.write_text(image, text)

        cv2.imshow('Image', image)

        if cv2.waitKey(waitTime) & 0xFF == ord('q'):
            return False

        return True

    # Write text onto the image in the bottom left corner
    def write_text(self, image, text):
        # Determine if the score is 0 or 20 or inbetween to color
        if text.endswith(' ' + str(self.green_threshold)):
            color = (0, 255, 0) # Green
        elif text.endswith(' ' + str(self.red_threshold)):
            color = (0, 0, 255) # Red
        else:
            color = (0, 255, 255) # Yellow

        font = cv2.FONT_HERSHEY_SIMPLEX
        image = cv2.putText(image, text, (10,30), font, 1,
            color, 2, cv2.LINE_AA)

        return image
