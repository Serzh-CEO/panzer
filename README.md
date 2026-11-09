# Panzer

A two-player tank battle game written in Python with [pygame](https://www.pygame.org/).
Destroy the other tank, pick up hearts, shields and ammo, and use the level editor to draw your own maps.

## Run

```bash
pip install -r requirements.txt
python main.py
```

## Controls

| Action | Player 1 | Player 2 |
|---|---|---|
| Move | W A S D | Arrow keys |
| Shoot | Space | L |
| Restart | R | R |

## Map editor

`python cart_maker.py` opens the level editor. The map is a 26x19 grid stored in `gamemap.py`
(`0` – empty, `1` – indestructible block, `2` – brick block).

## Project structure

- `main.py` – game loop
- `classes.py` – blocks, bullets, players, loot
- `gamemap.py` – level layout
- `cart_maker.py` – map editor
- `res/` – sprites and textures
