# Asteroids Game

A classic asteroids game built with Python and Pygame. Inspired and guided by [Boot.dev](https://www.boot.dev)!

## Requirements

- Python 3.8+
- UV package manager

## Installation

**Step 1**: Clone the repository
```bash
git clone https://github.com/dejank21/asteroids.git
cd asteroids
```

**Step 2**: Install UV if you don't have it
```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## Running the Game

From the project directory, run:

```bash
uv run main.py
```

UV will automatically create a virtual environment and install all necessary dependencies (including pygame).

## Controls

- **W** - Move forward
- **S** - Move backward
- **A** - Rotate left
- **D** - Rotate right  
- **Space** - Shoot

## How to Play

Navigate your ship through space and destroy asteroids by shooting them. When you shoot larger asteroids, they break into smaller pieces. Avoid colliding with asteroids or you'll be destroyed. The game gets progressively harder as you advance.

## Troubleshooting

**UV not found**: Make sure UV is installed following Step 2 above.

**Pygame not installing**: UV should handle this automatically, but if issues occur, try:
```bash
uv pip install pygame
uv run main.py
```

**Game won't start**: Ensure you have proper graphics drivers and that no other application is blocking the game window.

