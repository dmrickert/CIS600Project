#!/usr/bin/env python

'''
   Class to interact with media player
'''


class MediaHandler:
    def __init__(self):
        self.placeholder = 'placeholder'
        self.isMediaPlaying = False

    def placeholder(self):
        self.placeholder = 'change'

        return

    def start_media(self):
        print('This would start media')
        self.isMediaPlaying = True

        return

    def stop_media(self):
        print('This would stop media')
        self.isMediaPlaying = False

        return
