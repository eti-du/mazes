#encoding
#coding:utf-8
"""
notes:
    ? DOCS:
        ? This is meant to manage everything related to music (Which mostly designates background music).

    § TODO:
        § Functions
            § `play_queue()`
                § implement the "shuffle" playback mode (randomly selects an unplayed track from the
                § playlist)

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
from pygame import mixer as mixer

#libs setup
mixer.init()


#classes


#functions
def enqueue_music_tracks(*music_tracks):#? not sure this one is very useful... :/
    """ Gets selected music tracks and enqueues them
    to play one after the other. """

    #makes a list out of the different tracks
    #(which are elements of a tuple by default)
    playlist = list(music_tracks)

    return playlist



def play_queue(playlist, playback_mode="standard"):
    """ Plays the music tracks queue according to a selected
    playback mode.

    `playback_mode` accepts as values:
    - "`standard`"  : linear queue playback
    - "`shuffle`"   : plays a random track from the queue [TBA]

    `playback_mode` defaults to "`standard`" """

    if playback_mode == "standard":
        for track in range(0, len(playlist) - 1, 1):
            mixer.music.load(playlist[0])       #loads the first track from the playlist into the mixer
            playlist.pop(0)                     #removes the loaded track from the playlist (it STILL is in the mixer!)

            mixer.music.play(0, 0.0, 1000)      #plays the loaded track

            #? not exactly sure of why THIS
            #? specifically works tbh but hey,
            #? who cares lol
            #? ( ❀´-ω-`)🤝(´-ω-`❀ )
            mixer.music.queue(playlist[track])  #enqueues the "next" track, which will play right after the current one



#script

#! DEBUG ZONE !###! HERE BE DRAGONS !############################################################
#track = R"assets/music/MundialRonaldinhoSoccer64_intro.mp3"
#print(mp3(track).info.length)

#music_queue = enqueue_music_tracks(R"assets/music/MundialRonaldinhoSoccer64_intro.mp3",
#                                    R"assets/music/ambient_1.mp3")
#play_queue(music_queue)