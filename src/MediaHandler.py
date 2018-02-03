#!/usr/bin/env python

'''
   Class to interact with media player
'''


class MediaHandler:
    def __init__(self):
        # Assume media is playing to begin
        self.isMediaPlaying = True

    def start_media(self):
        print('ACTION: This would start media')
        self.isMediaPlaying = True

        return

    def stop_media(self):
        print('ACTION: This would stop media')
        self.isMediaPlaying = False

        return
