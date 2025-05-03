# Unity\_Fly\_Navigation\_BlenderPlugin

A simple Blender 4.4 add-on that enables Unity-style WASD fly navigation in the 3D Viewport with Shift for a speed boost.

## Features

* **WASD movement**: Move forward, backward, and strafing left/right.
* **Shift+F to enter fly mode**: Instant toggle into Unity-like free-fly.
* **Speed boost**: Holding **Shift** while flying multiplies your movement speed.
* **Customizable parameters**: Adjust base speed, boost factor, view height, jump height, and teleport time via code.

## Installation

1. **Download the plugin**

   * Save the file as `unity_fly_nav.py`.

2. **Copy to Add-ons folder**

   * **Windows**: `%APPDATA%\Blender Foundation\Blender\4.4\scripts\addons\`
   * *.x.x* corresponds to your Blender version (e.g., `3.5`, `4.4`, etc.)

   **macOS**: `~/Library/Application Support/Blender/4.4/scripts/addons/`

   **Linux**: `~/.config/blender/4.4/scripts/addons/`

3. **Enable in Blender**

   * Open Blender and go to **Edit → Preferences → Add-Ons**.
   * Click **Refresh** if the list is already open.
   * Search for **Unity-Style Walk/Fly Navigator** and enable the checkbox.

4. **Enter Fly Mode**

   * In the 3D Viewport, press **Shift + F** to enter Unity-style navigation.
   * Use **W/A/S/D** to move and hold **Shift** to move at boosted speed.
   * Press **Esc** or **Left Mouse Button** to exit fly mode.

## Configuration

If you’d like to tweak the default settings, open `unity_fly_nav.py` and edit the following lines in the `register()` function:

```python
prefs = bpy.context.preferences.inputs.walk_navigation
prefs.walk_speed        = 2.0    # Base movement speed
prefs.walk_speed_factor = 2.0    # Multiplier when holding Shift (speed boost)
prefs.view_height       = 1.6    # Camera height off the “floor”
prefs.jump_height       = 0.5    # Jump height
prefs.teleport_time     = 0.2    # Warp time on Spacebar
```

* **`walk_speed`**: Increase for faster base movement.
* **`walk_speed_factor`**: Increase for stronger shift-boost.
* **`view_height`**: Adjust camera height.
* **`jump_height`**: Change how high you can jump.
* **`teleport_time`**: Modify the duration of the teleport effect when pressing Spacebar.

After saving your changes, click **Refresh** in the Add-Ons preferences and toggle the add-on off and on to apply.

## Troubleshooting

* **Add-on not visible**:

  * Ensure the `.py` file is directly in the `addons` folder (not nested in extra folders).
  * Make sure `__init__.py` is present if using a package folder structure.
  * Click **Refresh** in the Add-Ons preferences.

* **`No module named 'unity_fly_nav'` error**:

  * Do **not** manually `import unity_fly_nav` in Blender’s Python console. Just enable it via Preferences.

* **Pref values not applying**:

  * Confirm you’re editing the correct Blender version’s add-ons path.
  * Restart Blender after making changes.

## Contributing

Contributions and suggestions are welcome! Feel free to:

* Open an issue for bugs or feature requests.
* Submit pull requests with improvements or new features.

Please follow the project’s coding style and add clear commit messages.

## License

This plugin is released under the MIT License. See [LICENSE](LICENSE) for details.

## Changelog

* **v1.1**: Added shift-speed boost functionality and customizable speed factor.
* **v1.0**: Initial release with base WASD fly navigation.
