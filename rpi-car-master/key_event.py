import pygame
from pygame.locals import *

pygame.init()

while True:
#    pressed = pygame.key.get_pressed()
#    print pressed
    
    for event in pygame.event.get():
        if not hasattr(event, 'key'):
            continue
        if event.type == KEYDOWN:
            print event.key
            if event.key == ord('h'):
                print 'left'
            elif event.key == ord('j'):
                print 'forward'
            elif event.key == ord('k'):
                print 'backward'
            elif event.key == ord('l'):
                print 'right'
        elif event.type == KEYUP:
            print event.key
            if event.key == ord('h'):
                print 'stop'
            elif event.key == ord('j'):
                print 'stop'
            elif event.key == ord('k'):
                print 'backward'
            elif event.key == ord('l'):
                print 'right'