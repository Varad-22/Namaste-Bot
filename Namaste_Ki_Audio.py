import pygame

def audio():
    path = "/home/robotics-clubiiti/namaste_bot/welcome.mp3"

    pygame.mixer.init()
    speaker_volume = 1.0
    pygame.mixer.music.set_volume(speaker_volume)

    pygame.mixer.music.load(path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy() == True:
        continue