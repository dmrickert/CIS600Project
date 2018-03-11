#!/usr/bin/env Pythonism

'''
    Script to classify individual pictures for getting accuracy readings.
    Directory should contain files with "not_attentive" or "attentive" in
    their name.
'''

from src import ImageProcessor

import sys
import os
import cv2
import csv

# Log our classification to a CSV file
def log_classification(filename, csvWriter, classification):
    predicted = classification
    actual = ''
    # Get actual classification from filename
    if( 'not_attentive' in filename):
        actual = 'Not Attentive'
    else:
        actual = "Attentive"

    csvWriter.writerow({'file': filename, 'actual': actual, 'predicted': predicted})

    print('DECISION: {} is {}.'.format(filename, classification))

    return

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

    # Directory that contains our samples to attempt to classify
    pictureFolder = os.path.join(main_dir, 'samples')

    # Point to where the pregenerated HaarCaascades are
    resourceFolder = os.path.join(main_dir, 'res')

    # Initialize our objects
    image_process = ImageProcessor.ImageProcessor(resourceFolder)

    # Our output CSV
    fieldnames = ['file', 'actual', 'predicted']
    csvfileName = os.path.join(main_dir, 'checker_results.csv')
    csvfile = open(csvfileName, 'wb')
    csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    csvwriter.writeheader()


    for filename in os.listdir(pictureFolder):
        print('INPUT: {}'.format(filename))
        picturePath = os.path.join(pictureFolder, filename)

        rawImage = cv2.imread(picturePath)

        # Process image (use/build out image_process)
        image_process.convert_raw(rawImage)

        # Grab face from image if it exists
        if not image_process.extract_face():
            # No face was detected, sleep for a second and try again
            print('INFO: No face detected.')
            log_classification(filename, csvwriter, 'Not Attentive')
            image_process.show_image(image_process.rawImage, waitTime=50)

            continue

        # Determine Eye locations if they exist
        if not image_process.extract_eyes():
            # No eyes were detected
            print('INFO: Two open eyes not detected.')
            log_classification(filename, csvwriter, 'Not Attentive')
            image_process.show_image(image_process.rawImage, waitTime=50)

            continue

        print('INFO: A frontal face and two open eyes detected.')
        image_process.show_image(image_process.rawImage, waitTime=50)
        log_classification(filename, csvwriter, 'Attentive')

    print('Done')

#  Pythonism - If this script is run directly then this will trigger.  If you
#     import this script into another script this won't.
if __name__ == "__main__":
    main()
