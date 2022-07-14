#encoding
#coding:utf-8
"""
notes:
    ? DOCS:
        ? This is meant to manage everything related to music in "Mazes ???"

    § TODO:
        § Amplify weapons on Wallhammer.

    % FIXME:
        % Target compromised: move in, move in.

        & FIX:
            & Overwatch, target one sterilized.

    µ WHYNOT:
        µ Overwatch reports possible hostiles inbound.

    ! IMPORTANT:
        ! Roger that. Waiting for contact. Over.

    $ LOGS:
        $ Ready weapons, stay alert.
"""



#libraries/modules
import threading
from time import sleep

from pygame import mixer as mixer
from mutagen.mp3 import MP3 as mp3

#libs setup
mixer.init()


#classes


#functions

#? not sure this one is very useful... :/
def enqueue_music_tracks(*music_tracks):
    """ Gets selected music tracks and enqueues them
    to play one after the other. """

    playlist = list(music_tracks)
    return playlist

def play_queue(playlist, playback_mode="standard"):
    """
    Plays the music tracks queue according to a selected
    playback mode.

    `playback_mode` accepts as values:
    - "`standard`"  : linear queue playback
    - "`shuffle`"   : plays a random track from the queue

    `playback_mode` defaults to "`standard`"
    """

    #if playback_mode == "standard":
    #    for track in music_queue:
    #        mixer.music.load(track)
    #        threading.Thread(target=mixer.music.play(), args=(0, 0.0, 1000), daemon=True).start()
    #        threading.Thread(target=sleep(int(mp3(track).info.length)))
    if playback_mode == "standard":
        for track in range(0, len(playlist)-1, 1):
            mixer.music.load(playlist[0])
            playlist.pop(0)
            mixer.music.play()
            mixer.music.queue(playlist[track])
            #sleep(int(mp3(track).info.length))

#script

#! DEBUG ZONE !###! HERE BE DRAGONS !############################################################
#track = R"assets/music/MundialRonaldinhoSoccer64_intro.mp3"
#print(mp3(track).info.length)

music_queue = enqueue_music_tracks(R"assets/music/MundialRonaldinhoSoccer64_intro.mp3",
                                    R"assets/music/ambient_1.mp3")
play_queue(music_queue)