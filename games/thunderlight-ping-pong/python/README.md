# Thunderlight Ping Pong (Python)

A Pong game built with Python and Pygame, following the [Programming With Nick](https://www.youtube.com/@programmingwithnick) tutorial (about 40 minutes of video, 9 small steps).

## Goal

The game runs, both sides score, and the ball resets after each point.

## Requirements

- Python 3
- [pygame-ce](https://pyga.me/) (the community edition of Pygame; the code still uses `import pygame`)

```
pip install -r requirements.txt
```

## Running

From this folder:

```
python main.py
```

On Windows, if `python` is not found, use the launcher instead: `py main.py`.

## Build steps

- [x] 1. Install pygame
- [x] 2. Blank screen and game loop
- [x] 3. Draw the arena, paddles and ball
- [x] 4. Move the ball around
- [ ] 5. Check for collisions with all edges
- [ ] 6. Move the player's paddle
- [ ] 7. Move the CPU paddle with simple AI
- [ ] 8. Check for collisions with the paddles
- [ ] 9. Add scoring (and reset the ball)

## Ideas after the tutorial

- Make the CPU beatable (lower or randomised speed)
- Add sound and a win/restart screen
- Difficulty levels for the CPU paddle
