# GameJam 2025 - Balance

This repository contains a minimal prototype for a cooperative platformer.
The code no longer depends on `pygame` so it can run in restricted
environments. The level layout is loaded from `game/assets/level1.txt`.

## Getting Started

1. **Clone the repository**
   ```bash
   git clone <repository_url>
   cd GameJam2025
   ```
2. **Run the sample timer logic (optional)**
   ```bash
   python -m game.main
   ```
   The `update_game_state` function demonstrates how the timer would reset
   the level and players when it expires.

## Running Tests

Tests are written with Python's built-in `unittest` framework.
Run the suite from the repository root:

```bash
python -m unittest discover -v tests
```
