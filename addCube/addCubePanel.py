import bpy


class addCubePanel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_add_cube_panel"
    bl_label = "AddCube"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Tool"

    def draw(self, context):
        self.layout.operator("mesh.add_cube_sample",
                             icon='MESH_CUBE', text="Add Cube")


def register():
    bpy.utils.register_class(addCubePanel)


def unregister():
    bpy.utils.unregister_class(addCubePanel)
