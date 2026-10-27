# Build and ship

Notes on how the games will be packaged. Not final; check each tool's current documentation.

| Target | Python (Pygame) | C++ (Raylib) | JavaScript |
|---|---|---|---|
| Web | Pygbag (needs an async main loop) | Emscripten to WebAssembly | Runs as is |
| Windows | PyInstaller (onefile, no console) | Native build | Wrapper later |
| Linux, Android | Later | Later | Wrapper later |
| iOS, macOS | PWA | PWA | PWA |

## Keeping the repo healthy

- No build output in git: GitHub Actions builds and publishes to Pages and Releases.
- Only rebuild what changed (path filters in CI).
- Keep each game folder self-contained so it can move to its own repo.
- Single files over 50 MB are warned about by GitHub and blocked at 100 MB.
