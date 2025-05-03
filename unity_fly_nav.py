bl_info = {
    "name":        "Unity-Style Walk/Fly Navigator",
    "author":      "Kody A. Nguyen",
    "version":     (1, 1),
    "blender":     (4, 4, 0),
    "location":    "3D View → Shift + F",
    "description": "Unity-style WASD fly navigation (Shift+F) in the viewport, with Shift for speed boost",
    "category":    "3D View",
}

import bpy

addon_keymaps = []

def register():
    # 1) Configure global Walk/Fly prefs:
    prefs = bpy.context.preferences.inputs.walk_navigation
    prefs.walk_speed        = 2.0    # base movement speed
    prefs.walk_speed_factor = 5.0    # multiplier when holding Shift (5x speed)
    prefs.view_height       = 1.6    # camera height off the “floor”
    prefs.jump_height       = 0.5    # jump height
    prefs.teleport_time     = 0.2    # warp time on Spacebar

    # 2) Bind Shift+F to view3d.walk:
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name="3D View", space_type='VIEW_3D')
        kmi = km.keymap_items.new(
            idname="view3d.walk",
            type='F',
            value='PRESS',
            shift=True
        )
        addon_keymaps.append((km, kmi))

def unregister():
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

if __name__ == "__main__":
    register()
