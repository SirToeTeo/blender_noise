from bpy.types import Operator
from . import ngt_main


class NGT_OT_CreateGrid(Operator):
    bl_idname = "obj.create_grid"
    bl_label = "Create grid"
    bl_description = "Create grid"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        ngt_main.create_grid()

        return {"FINISHED"}


class NGT_OT_GenerateNoise(Operator):
    bl_idname = "obj.generate_noise"
    bl_label = "Generate noise"
    bl_description = "Generate noise"

    @classmethod
    def poll(cls, context):
        obj = context.object
        if obj is not None:
            if obj.mode == "OBJECT":
                return True

        return False

    def execute(self, context):
        ngt_main.generate_noise()

        return {"FINISHED"}


class NGT_OT_Delete(Operator):
    bl_idname = "obj.delete_all"
    bl_label = "Delete all"
    bl_description = "Delete all"

    @classmethod
    def poll(cls, context):
        obj = context.object
        if obj is not None:
            if obj.mode == "OBJECT":
                return True

        return False

    def execute(self, context):
        ngt_main.delete_all()

        return {"FINISHED"}
