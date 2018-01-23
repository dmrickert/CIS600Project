#!/usr/bin/env python

'''
   Initial main file for our project.  This app takes a picture from the
   webcam, extracts the face, extracts the eyes from the face, determines
   pupil location, and then uses the pupil/eye location to determine attention.
'''

from src import CameraHandler
from src import EyeTracker
from src import ImageProcessor
from src import MediaHandler

import sys
import os
import time


#    Main function, runs a while loop that continuously grabs images, extract
#    face, extracts eyes, finds pupil location, use eyebox/pupil location
#    to determine attention.
def main():
    # Get current directory in a very future compatible way
    if hasattr(sys, "frozen"):
        main_dir = os.path.dirname(sys.executable)
        full_real_path = os.path.realpath(sys.executable)
    else:
        script_dir = os.path.dirname(__file__)
        main_dir = os.path.dirname(os.path.realpath(sys.argv[0]))
        full_real_path = os.path.realpath(sys.argv[0])
        print(script_dir, main_dir, full_real_path)

    # Get the path to the resource folder
    resourceFolder = os.path.join(main_dir, 'res')

    # Initialize our object instances
    cam = CameraHandler.CameraHandler(0)
    image_process = ImageProcessor.ImageProcessor(resourceFolder)
    eye_track = EyeTracker.EyeTracker()
    media_player = MediaHandler.MediaHandler()

    # Kick off the while loop that will run eye detection
    while True:
        # Get image from Camera Handler (use/build out cam)
        rawImage = cam.grab_image()

        # Process image (use/build out image_process)
        image_process.convert_raw(rawImage)

        # Grab face from image if it exists
        if not image_process.extract_face():
            # No face was detected, sleep for a second and try again
            print('INFO: No face detected.')
            time.sleep(1)
            continue

        # Determine eye locations if they exist
        if not image_process.extract_eyes():
            # No eyes were detected, sleep for a second and try again
            print('INFO: No eyes detected')
            time.sleep(1)
            continue

        # Determine eye position (use/build out eyetrack)
        pupilLocation = image_process.extract_pupils()

        # Determine if face is looking towards our camera or away
        attentiveFlag = eye_track.determine_attention(True, True)

        # Action media player if necessary
        # TODO: Also check if media is already playing
        if attentiveFlag:
            media_player.start_media()
        else:
            media_player.stop_media()

        #time.sleep(3)

    return


#  Pythonism - If this script is run directly then this will trigger.  If you
#     import this script into another script this won't.
if __name__ == "__main__":
    main()
