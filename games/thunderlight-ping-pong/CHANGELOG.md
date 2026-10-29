# Changelog: Thunderlight Ping Pong

## Python

### 0.2.0 (2026-10-29)
First playable milestone: the tutorial game with a CPU you can beat, name labels and cleaner code.

#### Added
- "CPU" and "Player" name labels above the scores

#### Changed
- CPU paddle speed lowered to 4, so the CPU can be beaten
- Scores are centred under their labels
- Window title is now "Thunderlight Ping Pong"
- Game values (screen, paddle, ball and speed settings) are named constants, and both paddles share one helper to stay on screen
- Comments explain the why instead of the what

#### Known issues
- A hit on the top or bottom side of a paddle can make the ball stutter
- Releasing one arrow key while holding the other stops the paddle
- After a point, the ball restarts near the top of the screen and its direction is random, not toward the player who lost the point

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
