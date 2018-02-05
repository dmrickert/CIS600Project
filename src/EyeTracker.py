#!/usr/bin/env python

'''
   Class to handle the tracking of the eye in a processed image
'''


class EyeTracker:
    def __init__(self):
        self.inattentionScore = 0

        self.INATTENTION_MAX = 10
        self.INATTENTION_MIN = 0

    def determine_attention(self, eyeLocations, pupilLocation):

        return True

    def track_inattention(self):
        # Max intattention score of 10 so that it doesn't take a while to
        #    start again
        if self.inattentionScore < self.INATTENTION_MAX:
            self.inattentionScore += 1

        # Check if we're at an inattention score of 10
        if self.inattentionScore == self.INATTENTION_MAX:
            return True

        return False

    def track_attention(self):
        # Min inattention score of 0 so that it doesn't take a while to build up
        if self.inattentionScore > self.INATTENTION_MIN:
            self.inattentionScore -= 1

        if self.inattentionScore == self.INATTENTION_MIN:
            return True

        return False
