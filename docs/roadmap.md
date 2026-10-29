# Roadmap

| Phase | Done when |
|---|---|
| 0 | Thunderlight Ping Pong (Python) runs; repo has README and credits; Pygbag web build works |
| 1 | Snake and Tetris (Python), each with its own twist |
| 2 | Hub v0 is live; the message contract works with two games |
| 3 | C++ versions, Space Invaders, desktop builds via GitHub Actions, PWA install |
| 4 | 2048 and Asteroids (JavaScript) in the hub; Android wrapper |
| 5 | Stretch: iOS and macOS native builds; deeper interop experiments |

Game order: Pong, Snake, Tetris, Space Invaders, then Asteroids, with a JavaScript game when learning allows.

## Thunderlight Ping Pong (Python)

| Version | Status | What it adds |
|---|---|---|
| 0.1.0 | Done | Tutorial baseline: playable Pong with scoring. The CPU can't be beaten. |
| 0.2.0 | Done | First playable milestone: a CPU you can beat (speed 4), name labels and cleaner code |
| 0.3.0 | Planned | Better serves after a point, and fixes for ball stutter on paddles and the paddle stopping when two arrow keys overlap |
| Later 0.x | Planned | Difficulty levels, a PID-controlled CPU paddle, sound effects and volume, start/pause and win/restart screens |
| 1.0.0 | Planned | Polished game with a Pygbag web build |
