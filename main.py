#!/usr/bin/env python

'''
   Initial main file for our project.  Run with 'python main.py'.
'''

from src import CameraHandler
from src import EyeTracker
from src import ImageProcessor
from src import MediaHandler


# Main function for project
def main():
    # Just so if you run the shell something happens
    print('Hello World')

    # Initialize our object instances
    cam = CameraHandler()
    image_process = ImageProcessor()
    eyetrack = EyeTracker()
    media_player = MediaHandler()

    # TODO: Get image from Camera Handler (use/build out cam)

    # TODO: Process image (use/build out image_process)

    # TODO: Determine eye position (use/build out eyetrack)

    # TODO: Action media player if necessary

    return

'''
    Pythonism - If this script is run directly then this will trigger.  If you
        import this script into another script this won't.
'''
if __name__ == "__main__":
    main()
