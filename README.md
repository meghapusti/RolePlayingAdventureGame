# 🗡️ Choose Your Own Adventure!

> A story-driven role-playing adventure game with four embedded minigames, built entirely in Python using `tkinter` and `turtle`.

---

## 📖 About

**Choose Your Own Adventure!** follows **Tim**, a cat hero on a quest to recover stolen bread for his friend Chickpea the chick. Along the way, players navigate branching dialogue, explore richly illustrated scenes, and unlock minigames that must be completed to progress the story.

The game was built as a collaborative team project (**Team 9A**) and showcases a full game loop — from a polished main menu with a credits screen, through a multi-chapter narrative, to a minigame hub with four distinct games.

---

## 🎮 Features

- **Narrative Adventure** — Branching dialogue and player choices that affect how the story unfolds across multiple chapters
- **Main Menu System** — Start Game, Mini Games, Credits, and Quit, with scene transitions powered by `subprocess`
- **4 Playable Minigames** integrated into the story:
  - 🧱 **Brick Breaker** — OOP-based ball-and-paddle game with multi-hit bricks and lives system
  - ⭕ **Tic-Tac-Toe** — Two-player game drawn with `turtle` graphics on a custom board
  - 🎨 **Crack the Code** — Colour memory game where players memorise and reproduce a flashing sequence
  - 🐥 **Hot Chicks, Hotter Bread** — Top-down collection game with directional sprite animations and escalating difficulty
- **Custom Pixel Art & Sprites** — Animated GIF character sprites (directional chick animations, cherry bomb obstacles)
- **Full-Screen Illustrated Backgrounds** — Fantasy-themed scene artwork loaded per chapter
- **Scene Management** — Dynamic canvas swapping within windows for smooth in-game transitions
- **Credits Screen** — Art attribution and team credits accessible from the main menu

---

## 🛠️ Tech Stack

| Technology | Usage |
|---|---|
| **Python 3** | Core language |
| **tkinter** | Main menu, narrative UI, scene management, Brick Breaker |
| **turtle** | Tic-Tac-Toe board, Crack the Code colour engine, Hot Chicks game loop |
| **subprocess** | Scene-to-scene and minigame launching |
| **OOP (Classes)** | `GameObject`, `Ball`, `Paddle`, `Brick`, `Color` — game entity architecture |
| **GIF / PNG assets** | Sprite animation, background scene art |

---

## 📁 Project Structure

```
1D Project - Team 9A/
├── Start Game.py                        # Entry point
├── All Codes & Assets/
│   ├── Graphics_and_structure/
│   │   ├── MainMenu                     # Main menu screen
│   │   ├── Starting Your Adventure      # Story intro
│   │   ├── minigame1                    # Chapter 1 — Chickpea's kitchen
│   │   ├── minigame1_2                  # Chapter 1 continued
│   │   ├── minigame2                    # Chapter 2 — Brick wall
│   │   ├── minigame3                    # Chapter 3 — Lost in the woods
│   │   ├── minigame4                    # Chapter 4 — The locked door
│   │   └── Graphics/                    # All background PNGs
│   ├── Brick Game.py                    # Brick Breaker minigame
│   ├── Tic Tac Toe.py                   # Tic-Tac-Toe minigame
│   ├── Color Code Game.py               # Crack the Code minigame
│   └── Chick/
│       ├── Pei Pei - Chick.py           # Hot Chicks collection game
│       └── *.gif                        # Directional chick sprites
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- `tkinter` (bundled with most Python installations)
- `turtle` (bundled with most Python installations)

### Running the Game

1. Clone or download this repository
2. Navigate to the `1D Project - Team 9A/` folder
3. Run the entry point:

```bash
python "Start Game.py"
```

> **Note:** The game uses relative file paths. Make sure to run the script from inside the `1D Project - Team 9A/` directory so all assets load correctly.

---

## 🎯 How to Play

1. Launch `Start Game.py` — the **Main Menu** opens
2. Click **Start Game** to begin Tim's adventure
3. Read the story and click through dialogue choices
4. When prompted, play the embedded minigame to progress:
   - **Brick Breaker** — Use `←` `→` arrow keys to move the paddle
   - **Tic-Tac-Toe** — Click on the board to place your piece
   - **Crack the Code** — Watch the colour sequence flash, then click colours to match it
   - **Hot Chicks** — Use arrow keys to move; collect bread, dodge cherry bombs
5. Complete all chapters to finish Tim's quest!


---

## 🎨 Credits

- **Background Graphics:** Fantasy Forest assets from [lornn.itch.io](https://lornn.itch.io/)
- **Character Sprites:** Cute Legends: Cat Heroes from [9e0.itch.io](https://9e0.itch.io/)

---

## 📝 Notes

This project was developed as a **1D (Introduction to Digital Design) team project**. It is an educational project built to demonstrate applied programming concepts including OOP, GUI design, event-driven programming, and collaborative software development.
