#!/usr/bin/env python

'''
   Initial main file for our project.  This app takes a picture from the
   webcam, extracts the face, extracts the eyes from the face, and then uses
   the existance of frontal face/two eyes to determine attention.
'''

from src import CameraHandler
from src import AttentionTracker
from src import ImageProcessor
from src import MediaHandler

import sys
import os
import time


#    Main function, runs a while loop that continuously grabs images, extract
#    face, extracts eyes, determines attention.
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
    # Name of song in the resource folder
    songPath = os.path.join(resourceFolder, 'Campfire+Song.mp3')

    # Initialize our object instances
    cam = CameraHandler.CameraHandler(0)
    image_process = ImageProcessor.ImageProcessor(resourceFolder)
    attention_track = AttentionTracker.AttentionTracker()
    media_player = MediaHandler.MediaHandler(songPath)

    # Set our color thresholds (min and max correspond to green and red)
    image_process.set_colors_thresholds(attention_track.INATTENTION_MIN,
        attention_track.INATTENTION_MAX)

    # Kick off the while loop that will run attention detection
    while True:
        # Get image from Camera Handler (use/build out cam)
        rawImage = cam.grab_image()

        # Process image (use/build out image_process)
        image_process.convert_raw(rawImage)

        # Grab face from image if it exists
        if not image_process.extract_face():
            # No face was detected, sleep for a second and try again
            print('INFO: No face detected.')

            # Log the inattention.  If returns true, inattention limit hit
            if attention_track.track_inattention():
                # Turn off media if it's playing
                if media_player.isMediaPlaying:
                    # Turn off media
                    media_player.stop_media()

            # Still display the image so it's fluid
            if not image_process.show_image(image_process.rawImage,
                attention_track.inattentionScore):

                break

            continue

        # Determine Eye locations if they exist
        if not image_process.extract_eyes():
            # No eyes were detected
            print('INFO: Two open eyes not detected')

            # Log the inattention.  If returns true, inattention limit hit
            if attention_track.track_inattention():
                # Turn off media if it's playing
                if media_player.isMediaPlaying:
                    # Turn off media
                    media_player.stop_media()

            # Still display the image so it's fluid
            if not image_process.show_image(image_process.rawImage,
                attention_track.inattentionScore):

                break

            continue

        # Log that the user was in fact paying attention
        if attention_track.track_attention():
            # Start media if it's not playing
            if not media_player.isMediaPlaying:
                media_player.start_media()

        # Show the image and check if we should break
        #   (function would return false)
        if not image_process.show_image(image_process.rawImage,
            attention_track.inattentionScore):

            break

    # Release the capture and destroy our webcam output window
    cam.camera.release()

    return


#  Pythonism - If this script is run directly then this will trigger.  If you
#     import this script into another script this won't.
if __name__ == "__main__":
    main()
