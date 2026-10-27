# GT Arcade

One multi-game app that gathers classic games, built by [Gideon Tladi](https://github.com/gtcodes22) in Python, C++ and JavaScript, behind one modern interface. The aim is learning and practice first, then a public record of growth.

> Status: early. The first game, Thunderlight Ping Pong (Python), is in progress. The hub comes later.

## Games

| Game | Classic | Python | C++ | JavaScript |
|---|---|---|---|---|
| [Thunderlight Ping Pong](games/thunderlight-ping-pong/) | Pong | In progress | Planned | - |

More games are planned. See the [roster](docs/roster.md) and the [roadmap](docs/roadmap.md).

## Repository layout

```
GT-Arcade/
├── docs/        architecture, message contract, roadmap, roster, build and ship
├── hub/         the web hub (not started)
└── games/
    └── <game>/
        ├── assets/      shared sounds, fonts, images
        ├── python/      Python and Pygame version
        └── cpp/         C++ and Raylib version (later)
```

Every version of a game lives in the same game folder, each in its own language subfolder.

## Documentation

- [Architecture](docs/architecture.md)
- [Message contract](docs/message-contract.md)
- [Roadmap](docs/roadmap.md)
- [Roster](docs/roster.md)
- [Build and ship](docs/build-and-ship.md)
- [Credits](CREDITS.md)

## Licence

[MIT](LICENSE) © 2026 Gideon Tladi. The games are built following third-party tutorials; see [CREDITS.md](CREDITS.md).
