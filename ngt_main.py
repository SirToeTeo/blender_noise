import bpy
import mathutils
import random
import bmesh


def delete_all():
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)


def exp_curve(x, exp):
    res = x**exp

    if exp % 2:
        return res

    return (abs(x) / x) * res


def create_grid():
    scene = bpy.context.scene
    size = int(scene.size)

    bpy.ops.mesh.primitive_grid_add(size=size, x_subdivisions=size, y_subdivisions=size)

    obj = bpy.context.active_object

    obj.name = scene.target_name


def generate_noise():
    scene = bpy.context.scene

    # Set the target as active object

    obj = bpy.data.objects[scene.target_name]
    bpy.context.view_layer.objects.active = obj

    bpy.ops.object.editmode_toggle()  # EDIT MODE

    m_obj = bmesh.from_edit_mesh(obj.data)

    # Generate the seed offset + user offset

    random.seed(scene.seed)

    octave_offsets = [
        mathutils.Vector(
            (
                random.randint(-1000, 1000) + scene.offset[0],
                random.randint(-1000, 1000) + scene.offset[1],
                0,
            )
        )
        for i in range(scene.octaves)
    ]

    # Store min and max for interpolation

    z_max = 0
    z_min = 0

    for v in m_obj.verts:
        # Reset z to get consistent noise

        co = mathutils.Vector((v.co.x, v.co.y, 0))

        frequency = 1
        amplitude = 1
        z_total = 0

        # Compute and sum each octave

        for i in range(scene.octaves):
            n = mathutils.noise.noise(co / scene.scale * frequency + octave_offsets[i])
            z_total += n * amplitude

            frequency *= scene.lacunarity
            amplitude *= scene.persistence

        v.co.z = z_total

        # Keep track of min and max

        z_max = z_total if z_total > z_max else z_max
        z_min = z_total if z_total < z_min else z_min

    # Calculate the maximum height range

    z_range = z_max + (-z_min)

    # Sampling noise at integer values returns a flat grid

    if z_range == 0:
        bpy.ops.object.editmode_toggle()  # OBJECT MODE
        return

    # Clamp vertex height to [-1, 1]
    # Evaluate vertex height relative to the easing curve

    for v in m_obj.verts:
        v.co.z += -z_min
        v.co.z /= z_range
        v.co.z *= 2
        v.co.z -= 1
        v.co.z = exp_curve(v.co.z, scene.exponent) * scene.height_scale

    bpy.ops.object.editmode_toggle()  # OBJECT MODE
