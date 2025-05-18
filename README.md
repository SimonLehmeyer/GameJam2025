# GameJam 2025 - Balance

This repository contains a minimal `pygame` prototype for a cooperative
side-scrolling platformer. The goal is to work together while passing a timed
"balance" debuff back and forth. Holding the debuff for too long causes a level
reset, so coordination between players is key.

## Getting Started

1. **Clone the repository**
   ```bash
   git clone <repository_url>
   cd GameJam2025
   ```
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the prototype**
   ```bash
   python -m game.main
   ```

A window will open with two rectangles representing the players.

The level layout now loads from `game/assets/level1.tmx`, which can be edited
with [Tiled](https://www.mapeditor.org/). The map is fixed at **16 rows by 100
columns** so there's plenty of horizontal space for tricky jumps. Place custom
tiles under `game/assets/tiles` and edit the TMX file to design new levels.

### Controls
- **Player 1:** `A` left, `D` right, `W` jump, `E` pass debuff
- **Player 2:** Arrow keys to move, `Ctrl` (right) pass debuff

Collide with your partner and press the pass key to hand over the debuff.
The debuff lasts 40 seconds and a countdown is displayed at the top of the
screen. If the timer expires on either player, the level resets and you start
over. A simple horizontal camera keeps the players centered as they travel
across the wider map.

This code is only a starting point. Expanding it with additional levels,
mazes, traps, and networking would realize the full "Balance" game concept.

