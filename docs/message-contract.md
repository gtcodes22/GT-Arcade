# Message contract (draft v0)

The only link between the hub and a game. Draft: it may change once two games use it.

| Direction | Message | Data |
|---|---|---|
| Game → hub | `ready` | none |
| Game → hub | `score` | `{ value }` |
| Game → hub | `gameover` | `{ score }` |
| Hub → game | `pause` / `resume` | none |
| Hub → game | `mute` | `{ on: true/false }` |
| Hub → game | `restart` | none |

## How each language sends a message

To be verified when building.

| Language | Route |
|---|---|
| JavaScript | `window.parent.postMessage(...)` |
| Python (Pygbag) | Pygbag exposes the browser window to Python (`platform.window`); check the current Pygbag docs |
| C++ (Emscripten) | Run JavaScript from C++ with `EM_ASM` or `emscripten_run_script`; check the Emscripten docs |
