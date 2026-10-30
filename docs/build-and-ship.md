# Build and ship

Notes on how the games will be packaged. Not final; check each tool's current documentation.

| Target | Python (Pygame) | C++ (Raylib) | JavaScript |
|---|---|---|---|
| Web | Pygbag (needs an async main loop) | Emscripten to WebAssembly | Runs as is |
| Windows | PyInstaller (onefile, no console) | Native build | Wrapper later |
| Linux, Android | Later | Later | Wrapper later |
| iOS, macOS | PWA | PWA | PWA |

## Windows build for a Python game (PyInstaller)

First used for Thunderlight Ping Pong (Python) 0.2.0. These steps make one `.exe` that runs without Python installed.

1. **Build from a release.** Check out the release tag (or `main` at that commit) with a clean working tree, so the `.exe` matches what is tagged. Check with `git status`.
2. **Install PyInstaller** once:

   ```powershell
   py -m pip install pyinstaller
   ```

3. **Build.** Run this from the game's `python/` folder. The output goes to a temporary folder outside the repo, so no build files appear in git:

   ```powershell
   $out = "$env:TEMP\thunderlight-build"
   py -m PyInstaller --onefile --noconsole --name ThunderlightPingPong --distpath "$out\dist" --workpath "$out\work" --specpath "$out" --noconfirm main.py
   ```

   - `--onefile` makes a single `.exe`.
   - `--noconsole` hides the black console window.
   - The result is `$out\dist\ThunderlightPingPong.exe` (about 16 MB).
4. **Test it.** Double-click the `.exe` and play a few points. A game that works from `main.py` can still fail once packaged.
5. **Zip it for sharing.** Put the `.exe` and a short `HOW TO PLAY.txt` (controls and known issues) in one zip named `ThunderlightPingPong-<version>-windows.zip`. Windows opens files from inside a zip badly, so the text file tells people to extract it first.
6. **Share the zip.** Attach it to a GitHub Release, or send it directly (Drive, USB stick). Messaging apps often block `.exe` files. Do not commit the `.exe` to git.

Notes:

- Unsigned `.exe` files trigger Windows SmartScreen ("Windows protected your PC"). Players click **More info**, then **Run anyway**. Say so in `HOW TO PLAY.txt`.
- PyInstaller builds for the system it runs on, so this makes a Windows `.exe` only. Mac and Linux builds need those systems.
- Rebuilding the same tag later behaves the same but is not byte-identical, so its file hash differs. Keep the original zip if the exact file matters.
- If the game later loads files from `assets/`, add them to the build with PyInstaller's `--add-data` option and test again.

## Releases in a monorepo

Every game shares one Releases page, so naming does the sorting.

| Habit | Example |
|---|---|
| The **tag** is the record of a version. A GitHub Release is notes and files on top of it, so it can be created later from an existing tag. | `thunderlight-ping-pong-python-v0.2.0` |
| Tag format: `<game>-<language>-v<version>`. The prefix groups and filters one game's releases. | `thunderlight-ping-pong-python-v` |
| Release title: public title, language, version. | `Thunderlight Ping Pong (Python) 0.2.0` |
| Release notes: copy that version's section from the game's `CHANGELOG.md`. | One source of truth |
| Asset names carry game, version and platform. | `ThunderlightPingPong-0.2.0-windows.zip` |

- The Releases page has a search box. Typing a tag prefix shows only one game's releases.
- GitHub shows a single "Latest" badge per repository, so it does not mean "newest version of this game". Each game's changelog and README say that instead.
- Before 1.0.0, milestones use plain version numbers (such as `0.2.0`). A release can be marked as a pre-release on GitHub without changing the tag name.
- Merge project branches into `main` with a merge commit, not squash or rebase, so earlier tags stay in `main`'s history.
- Later, a GitHub Actions workflow can build and attach the right file when a tag matching a game's pattern is pushed, and the hub's Downloads page can link the latest version of each game.
- If the page gets noisy, a game folder can move to its own repository with its own releases.

## Keeping the repo healthy

- No build output in git: GitHub Actions builds and publishes to Pages and Releases.
- Only rebuild what changed (path filters in CI).
- Keep each game folder self-contained so it can move to its own repo.
- Single files over 50 MB are warned about by GitHub and blocked at 100 MB.
