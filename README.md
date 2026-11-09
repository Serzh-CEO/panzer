# Panzer

A two-player tank battle game written in Python with [pygame](https://www.pygame.org/).
Destroy the other tank, pick up hearts, shields and ammo, and use the level editor to draw your own maps.

>Written in 2023–2024, uploaded to GitHub in November 2026.

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

`python cart_maker.py` opens the level editor (26x19 grid, saved to `map.txt`).

| Key | Action |
|---|---|
| 1 / 2 / 3 / 4 | Select brick / destructible block / heart / shield |
| D (hold) | Draw under the mouse |
| Space (hold) | Erase |
| S | Save map |

## Project structure

- `main.py` – game loop
- `classes.py` – blocks, bullets, players, loot
- `gamemap.py` – level layout
- `cart_maker.py` – map editor
- `res/` – sprites and textures

##Screenshot
<img width="1201" height="883" alt="image" src="https://github.com/user-attachments/assets/ed4d9295-896f-4ede-af0f-f7ff60de74bf" />

