# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import bpy
from .ngt_ops import NGT_OT_Delete, NGT_OT_CreateGrid, NGT_OT_GenerateNoise
from .ngt_pnl import NGT_PT_Panel
from . import ngt_main


# INFO

bl_info = {
    "name": "NoiseGeneratorTest",
    "author": "ToeTeo",
    "description": "Generate Noise",
    "blender": (3, 6, 0),
    "version": (0, 0, 1),
    "location": "",
    "warning": "",
    "category": "Generic",
}

# REGISTRATION / UNREGISTRATION

classes = (
    NGT_PT_Panel,
    NGT_OT_Delete,
    NGT_OT_CreateGrid,
    NGT_OT_GenerateNoise,
)


def register():
    for c in classes:
        bpy.utils.register_class(c)


def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)


# INITIALIZE PROPERTIES


def regenerate(self, context):
    ngt_main.generate_noise()


bpy.types.Scene.size = bpy.props.IntProperty(min=1, max=240, default=100)
bpy.types.Scene.height_scale = bpy.props.FloatProperty(
    min=1,
    max=100,
    step=10,
    default=10,
    precision=1,
    update=regenerate,
    description="Maximum distance between the lowest and highest vertex of the mesh",
)
bpy.types.Scene.exponent = bpy.props.IntProperty(
    min=1,
    max=20,
    step=1,
    default=1,
    update=regenerate,
    description="Exponent for the easing function",
)
bpy.types.Scene.scale = bpy.props.FloatProperty(
    min=0.1,
    max=100,
    step=10,
    default=2,
    precision=1,
    update=regenerate,
    description="Scale used in noise sampling",
)
bpy.types.Scene.seed = bpy.props.IntProperty(
    min=0, max=100, step=1, default=0, update=regenerate
)
bpy.types.Scene.persistence = bpy.props.FloatProperty(
    min=0.01,
    max=1,
    step=1,
    default=0.5,
    precision=2,
    update=regenerate,
    description="Amplitude falloff",
)
bpy.types.Scene.lacunarity = bpy.props.FloatProperty(
    min=1,
    max=10,
    step=10,
    default=2,
    precision=1,
    update=regenerate,
    description="Frequency gain",
)
bpy.types.Scene.octaves = bpy.props.IntProperty(
    min=2,
    max=16,
    step=1,
    default=8,
    update=regenerate,
    description="Number of noise iterations",
)
bpy.types.Scene.offset = bpy.props.FloatVectorProperty(
    step=10, default=(0, 0, 0), update=regenerate
)

bpy.types.Scene.target_name = bpy.props.StringProperty(
    default="NoiseGrid", description="Name of the object the script should target"
)
