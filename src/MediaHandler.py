#!/usr/bin/env python

'''
   Class to interact with media player
'''

from pygame import mixer

class MediaHandler:
    def __init__(self, songPath):
        # Assume media is playing to begin
        self.isMediaPlaying = True
        self.mixer = mixer
        self.mixer.init()

        # Assign music file
        self.musicFile = songPath
        self.mixer.music.load(self.musicFile)
        print('ACTION: Starting media')
        self.mixer.music.play(loops=-1)

    def start_media(self):
        print('ACTION: Unpausing media')
        self.mixer.music.unpause()

        self.isMediaPlaying = True

        return

    def stop_media(self):
        print('ACTION: Pausing media')
        self.mixer.music.pause()
        self.isMediaPlaying = False

        return
