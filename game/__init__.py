import json
import pygame

from typing import List, Tuple, Optional

WINDOW = None
RUNNING = False
CLOCK = None
FPS = 0

SCORE = 0
SCOREBOARD = [0] * 10


def initialize(wsize: Tuple[int, int], fps: int, saved_data: str, **kwargs):
    """Initialize the game state from a saved gamestate -- saved_data"""
    global WINDOW, CLOCK, SCORE, SCOREBOARD, RUNNING, FPS
    with open(saved_data, 'r') as f:
        data = json.load(f)
        f.close()
    scores = data["scores"]
    for i, j in enumerate(scores):
        SCOREBOARD[i] = j
    # set window size + fps data
    FPS = fps
    WINDOW = pygame.display.set_mode(wsize, 0, 32)
    CLOCK = pygame.time.Clock()
    RUNNING = True
    # optional arguments
    if "title" in kwargs:
        pygame.display.set_caption(kwargs["title"])
    if "icon" in kwargs:
        path = kwargs["icon"]
        pygame.display.set_icon(pygame.image.load(path))
    # end



