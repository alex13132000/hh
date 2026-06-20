# Architectural Refactoring Plan

## 1. Current architecture snapshot

The project is currently organized as a set of loosely coupled scripts with a single `Scene`/god object that owns the game loop, entity lifecycle, input handling, collision logic, spawning, and menu state.

Key modules:
- `main.py` / `scene.py` - game loop, update/draw, entity spawn logic, menu state
- `player.py` - player movement, shooting, bullet bonus state
- `enemy.py` - enemy movement, collision detection, hard-coded trajectories
- `bonus.py` - bonus entity movement and pickup effects
- `bullet.py` - player bullet
- `blast.py` - explosion effect
- `background.py` - scrolling background
- `hearts.py` / `score.py` - HUD display
- `button.py` - menu button UI
- `experiment.py` - prototype Bezier path experiment

## 2. Main architectural problems

- `Scene` is a god object
  - Handles game loop, event dispatch, entity creation, collision, spawn timing, menu state, and screen drawing.

- Entity lifecycle is not encapsulated
  - Entities directly append/remove themselves to/from `scene.transients`.
  - Collision side effects are spread across enemy and bonus classes.

- No asset management
  - Each class loads its own image/sound file repeatedly.
  - No caching or failure handling for assets.

- Hard-coded configuration
  - Enemy paths, spawn patterns, constants, and resource names are scattered across modules.
  - Global constants are duplicated and not grouped.

- Mixed responsibilities
  - `player.py` handles input polling and shooting cooldown.
  - `enemy.py` handles collision detection and health effects.
  - `bonus.py` handles both movement and bonus application.

- Event handling and game state are intertwined
  - Menu click handling, pause toggling, and gameplay use the same loop without clear state separation.

- Unused or orphaned prototype code
  - `experiment.py` is an active script outside the core game.

## 3. Refactoring goals

- Separate core game systems into distinct modules.
- Encapsulate entity behavior behind a common interface.
- Centralize resource loading and configuration.
- Make game state explicit: menu, playing, paused, game over.
- Remove direct list mutation from entities.
- Replace hard-coded spawn logic with a data-driven registry.
- Prepare the code for future features: levels, powerups, enemies, and tests.

## 4. Proposed architecture

### 4.1. Core layers

- `main.py`
  - Minimal bootstrap entry point.
  - Creates `GameEngine` / `Scene` and starts the loop.

- `engine.py` or `game/engine.py`
  - Owns the main loop, `Clock`, delta time, and high-level state transitions.
  - Orchestrates `InputSystem`, `UpdateSystem`, `RenderSystem`, `SpawnSystem`, and `CollisionSystem`.

- `resources.py`
  - Asset loader and cache for images and sounds.
  - Single source of truth for filenames and resource keys.

- `entities.py`
  - Defines common `Entity` base class/interface.
  - Implements `Player`, `Bullet`, `Enemy`, `Bonus`, `Blast`, and HUD objects.
  - Ensures each entity exposes `update(delta_time)` and `draw(surface)`.

- `entity_manager.py`
  - Tracks active entities in typed groups or `pygame.sprite.Group`.
  - Provides safe add/remove operations.
  - Supports queries like `get_entities(EntityType)`.

- `spawn.py`
  - Contains enemy and bonus spawn definitions and factories.
  - Moves patterns and path data to declarative structures or JSON data.

- `collision.py`
  - Central collision detection and resolution.
  - Handles bullet vs enemy, enemy vs player, bonus vs player.

- `ui.py`
  - Menu screen, buttons, HUD rendering, game-over overlay.
  - Separates UI drawing and input from gameplay.

### 4.2. Recommended module layout

```
hh/
  main.py
  game/
    engine.py
    resources.py
    entity_manager.py
    scene.py
    systems/
      input.py
      render.py
      collision.py
      spawn.py
    actors/
      player.py
      enemy.py
      bullet.py
      bonus.py
      blast.py
      hud.py
    data/
      enemy_patterns.py
      bonus_definitions.py
      config.py
  assets/
  README.md
  REFACTOR.md
```

This layout keeps runtime code under `game/` and leaves root files as lightweight entry points.

## 5. Detailed refactoring actions

### 5.1. Introduce an entity model

- Create an abstract base `Entity` with methods `update(self, dt)` and `draw(self, surface)`.
- Replace `scene.transients` with `EntityManager` containing active entities.
- Add typed collections for `bullets`, `enemies`, `bonuses`, `effects`, and HUD elements.
- Avoid entities calling `scene.transients.remove(self)`.
  - Instead return a removal flag or request removal through the manager.

### 5.2. Separate game loop from gameplay logic

- Move the loop from `Scene.run()` into `engine.py`.
- `Scene` should become a pure game state object exposing `update()` and `draw()`.
- The engine should drive state transitions with explicit enums: `MENU`, `PLAYING`, `PAUSED`, `GAME_OVER`.
- Menu input handling and rendering should be handled by `UIManager`.

### 5.3. Centralize resource loading

- Add `ResourceManager.load_image(key, path)` and `load_sound(key, path)`.
- Use cached resources inside game entities instead of repeated `pygame.image.load`.
- Keep all paths in one config file or dictionary.

### 5.4. Move spawn logic to a factory/registry

- Extract enemy pattern and bonus spawn definitions from `scene.py` and `bonus.py`.
- Use a `Spawner` service to manage timers and weighted choices.
- Prefer structured path data over hard-coded sequences.
- Consider loading enemy patterns from `enemies.json` / `enemies2.json`.

### 5.5. Centralize collision and effect logic

- Move bullet/enemy collision handling out of `BaseEnemy`.
- Define a collision system that acts on entity groups.
- Handle bonus pickups in one place, applying effects to `Player` and removing the bonus.
- Make `Blast` an effect with its own lifecycle and no hidden scene side effects.

### 5.6. Clean up UI and menus

- Replace direct `Button` clicks in `Scene.run()` with a `MenuScreen` object.
- Use `SceneState` values and dedicated UI draw methods for menu vs game.
- Remove `print(self.text)` from `Button.on_click()` unless debugging.

### 5.7. Remove or refactor `experiment.py`

- `experiment.py` should be moved into `enemy.py` or `game/systems/trajectory.py` if it contains reusable Bezier logic.
- If it is only a prototype, exclude it from the production flow.

## 6. Suggested incremental migration path

1. Create `game/resources.py` and `game/entities.py`.
2. Refactor `background.py`, `bullet.py`, `blast.py`, `hearts.py`, `score.py`, and `button.py` to use the new entity base.
3. Replace `scene.transients` with `EntityManager` and update `Scene.reset_game()` accordingly.
4. Move menu rendering/interaction into `ui.py` while keeping the same public interface.
5. Move spawn timing into `spawner.py` and replace the `while ...` pattern in `_add_enemy()`.
6. Add `collision.py` and migrate collision methods from entities into a central system.
7. Clean up the game loop in `engine.py` and keep `main.py` limited to startup.
8. Validate resource loading and add logging for missing assets.

## 7. Architectural improvements by refactor

- Better separation of concerns
- Easier debugging and unit testing
- More reusable entity behavior
- Cleaner startup and restart logic
- Clearer game state transitions
- Easier extension for new enemies, bonuses, and levels
- Elimination of list mutation bugs from entity self-removal

## 8. Notes for this specific codebase

- `Scene._add_enemy()` currently uses `while ...:` and `NameError` to restart pattern iteration. Replace that with a dedicated iterator or generator.
- `Player._shoot()` mixes pygame input polling and bullet bonus logic; split input detection into `InputSystem` and bullet creation into `Weapon`/`FireController`.
- `Enemy` path data is implied by `trajectory`; make it explicit through named splines or JSON definitions.
- `BonusBomb` currently destroys enemies by mutating `scene.transients`; instead, mark enemies as destroyed and let the manager remove them.
- `Button` should not directly access `scene.screen`; pass a drawing surface or UI canvas.

## 9. Recommended next step

Start by introducing the `ResourceManager`, `Entity` base class, and `EntityManager` as the foundation for the full refactor.