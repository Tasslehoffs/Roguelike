# Roguelike

This repository contains a very small terminal-based roguelike demo
implemented in Python. The game draws a simple room with walls made of `#`
characters and allows you to move the `@` player symbol around using the
arrow keys. Press `q` or `Esc` to quit.

## Running the Game

The game requires Python 3 and uses the standard `curses` library. To
start it, run:

```bash
python game.py
```

Use the arrow keys to move the player inside the room. The player cannot
move through the walls.
