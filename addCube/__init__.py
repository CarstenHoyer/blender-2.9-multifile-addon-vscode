from . import addCubePanel
from . import addCube

bl_info = {
    'name': 'Test Multifile Addon',
    'category': 'All',
    'version': (0, 0, 1),
    'blender': (2, 92, 0)
}


def register():
    addCube.register()
    addCubePanel.register()


def unregister():
    addCube.unregister()
    addCubePanel.unregister()


if __name__ == "__main__":
    register()
