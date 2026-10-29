# Changelog: Thunderlight Ping Pong

## Python

### Unreleased (0.2.0 in progress)

#### Added
- "CPU" and "Player" name labels above the scores

#### Changed
- CPU paddle speed lowered to 4
- Scores are centred under their labels
- Game values (screen, paddle, ball and speed settings) are named constants, and comments explain the why instead of the what

### 0.1.0 (2026-10-28)
Tutorial baseline: all 9 steps of the Programming With Nick Pong tutorial.

#### Added
- Window, game loop and 60 fps clock
- Arena, paddles and ball
- Ball movement with bounces off the top and bottom edges
- Player paddle controlled with the arrow keys, kept on screen
- CPU paddle that follows the ball
- Paddle collisions
- Scoring with a ball reset after each point, and on-screen scores

#### Known issues
- The CPU paddle tracks the ball perfectly, so it cannot be beaten
- A hit on the top or bottom side of a paddle can make the ball stutter
- Releasing one arrow key while holding the other stops the paddle
