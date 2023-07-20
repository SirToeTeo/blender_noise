import bpy
from bpy.types import Panel


class NGT_PT_Panel(Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Noise Generation"
    bl_category = "Noise"

    def draw(self, context):
        layout = self.layout

        box = layout.box()

        box.label(text="Utils")

        row = box.row()
        row.operator("obj.delete_all", text="Delete all")

        box = layout.box()

        box.label(text="Grid generation")

        row = box.row()
        row.prop(bpy.data.scenes[0], "size", text="Grid size")

        row = box.row()
        row.operator("obj.create_grid", text="Create grid")

        box = layout.box()

        box.label(text="Noise generation")

        row = box.row()
        row.prop(bpy.data.scenes[0], "target_name", text="Target")

        row = box.row()
        row.prop(bpy.data.scenes[0], "height_scale", text="Height scale")

        row = box.row()
        row.prop(bpy.data.scenes[0], "exponent", text="Exponent")

        row = box.row()
        row.prop(bpy.data.scenes[0], "scale", text="Scale")

        row = box.row()
        row.prop(bpy.data.scenes[0], "seed", text="Seed")

        row = box.row()
        row.prop(bpy.data.scenes[0], "persistence", text="Persistence")

        row = box.row()
        row.prop(bpy.data.scenes[0], "lacunarity", text="Lacunarity")

        row = box.row()
        row.prop(bpy.data.scenes[0], "octaves", text="Octaves")

        row = box.row()
        row.prop(bpy.data.scenes[0], "offset", text="Offset")

        row = box.row()
        row.operator("obj.generate_noise", text="Generate noise")
