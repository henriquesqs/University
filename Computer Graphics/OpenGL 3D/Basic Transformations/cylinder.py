import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np
import math
import random


def apply_transformations():

    trans = translation()
    xrot = x_rotation()
    yrot = y_rotation()
    zrot = z_rotation()
    scl = scale()

    res = np.matmul(zrot, yrot)
    res1 = np.matmul(res, xrot)
    res2 = np.matmul(trans, res1)

    return np.matmul(scl, res2).reshape((1, 16))


def translation():

    return np.array([1.0, 0.0, 0.0, t_x,
                    0.0, 1.0, 0.0, t_y,
                    0.0, 0.0, 1.0, t_z,
                    0.0, 0.0, 0.0, 1.0], np.float32).reshape((4, 4))


def scale():

    return np.array([s_x, 0.0, 0.0, 0,
                     0.0, s_y, 0.0, 0,
                     0.0, 0.0, s_z, 0.0,
                     0.0, 0.0, 0.0, 1.0], np.float32).reshape((4, 4))


def x_rotation():

    global anglex
    anglex -= 0.025

    cos = math.cos(anglex)
    sin = math.sin(anglex)

    return np.array([1.0, 0.0, 0.0, 0.0,
                     0.0, cos, -sin, 0.0,
                     0.0, sin, cos, 0.0,
                     0.0, 0.0, 0.0, 1.0], np.float32).reshape((4, 4))


def y_rotation():

    global angley
    angley -= 0.02

    cos = math.cos(angley)
    sin = math.sin(angley)

    return np.array([cos, 0.0, sin, 0.0,
                     0.0, 1.0, 0.0, 0.0,
                     -sin, 0.0, cos, 0.0,
                     0.0, 0.0, 0.0, 1.0], np.float32).reshape((4, 4))


def z_rotation():

    global anglez
    anglez -= 0.03

    cos = math.cos(anglez)
    sin = math.sin(anglez)

    return np.array([cos, -sin, 0.0, 0.0,
                     sin, cos, 0.0, 0.0,
                     0.0, 0.0, 1.0, 0.0,
                     0.0, 0.0, 0.0, 1.0], np.float32).reshape((4, 4))


def key_event(window, key, scancode, action, mods):
    print('[key event] key=', key)
    print('[key event] scancode=', scancode)
    print('[key event] action=', action)
    print('[key event] mods=', mods)
    print('-------')

    global t_x, t_y, t_z, s_x, s_y, s_z

    # If the user presses function keys
    if key == 290: # f1
        t_x += 0.01
    elif key == 291: # f2
        t_x -= 0.01
    elif key == 292: # f3
        t_y += 0.01
    elif key == 293: # f4
        t_y -= 0.01
    elif key == 294: # f5
        t_z += 0.01
    elif key == 295: # f6
        t_z -= 0.01

    # If the user presses arrow keys
    if key == 265: # up
        s_x += 0.05
        s_y += 0.05
        s_z += 0.05
    elif key == 264: # down
        s_x -= 0.05
        s_y -= 0.05
        s_z -= 0.05


def start_window():
    glfw.init()
    glfw.window_hint(glfw.VISIBLE, glfw.FALSE)
    window = glfw.create_window(
        800, 600, "Pyramid using 3D OpenGL", None, None)
    glfw.make_context_current(window)

    glfw.set_key_callback(window, key_event)  # gets keyboard inputs

    return window


def set_and_compile_shader(program, slot, slot_code):

    # Set shaders source
    glShaderSource(slot, slot_code)

    # Compiler shaders source
    glCompileShader(slot)

    if not glGetShaderiv(slot, GL_COMPILE_STATUS):
        error = glGetShaderInfoLog(slot).decode()
        print(error)
        raise RuntimeError("Shader compilation error")

    # Attach shader objects to the program
    glAttachShader(program, slot)


def make_point(u, v, r):
    x = r * math.cos(u)
    y = r * math.sin(u)
    z = v
    return (x, y, z)


def draw_object():

    global angle, radius, height
    vertices_list = []

    num_sectors = 30  # longitude
    num_stacks = 30  # latitude

    # grid sectors vs stacks (longitude vs latitude)
    sector_step = (PI * 2) / num_sectors  # from 0 to 2π
    stack_step = (height) / num_stacks  # from 0 to object's height

    # Cylinder side
    for i in range(0, num_sectors):  # for each sector (longitude)
        for j in range(0, num_stacks):  # for each stack (latitude)

            u = i * sector_step  # sector's angle
            v = j * stack_step  # stack's angle

            un = 0  # next sector's angle
            if i + 1 == num_sectors:
                un = 2 * PI
            else:
                un = (i + 1) * sector_step

            vn = 0  # next stack's angle
            if j + 1 == num_stacks:
                vn = height
            else:
                vn = (j + 1) * stack_step

            # polygomn vertices
            p0 = make_point(u, v, radius)
            p1 = make_point(u, vn, radius)
            p2 = make_point(un, v, radius)
            p3 = make_point(un, vn, radius)

            # first triangle
            vertices_list.append(p0)
            vertices_list.append(p2)
            vertices_list.append(p1)

            # second triangle
            vertices_list.append(p3)
            vertices_list.append(p1)
            vertices_list.append(p2)

    num_vertices = 60

    # Cylinder top
    counter = 0
    for counter in range(num_vertices):
        angle += (2 * PI) / num_vertices
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        z = height
        vertices_list.append((x, y, z))

    # Cylinder base
    counter = 0
    for counter in range(num_vertices):
        angle += (2 * PI) / num_vertices
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        z = 0
        vertices_list.append((x, y, z))

    total_vertices = len(vertices_list)
    vertices = np.zeros(total_vertices, [("position", np.float32, 3)])
    vertices['position'] = np.array(vertices_list)

    return vertices


def send_to_gpu(vertices):

    # Request a buffer slot from GPU
    buffer = glGenBuffers(1)

    # Make this buffer the default one
    glBindBuffer(GL_ARRAY_BUFFER, buffer)

    # Upload data
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_DYNAMIC_DRAW)
    glBindBuffer(GL_ARRAY_BUFFER, buffer)

    return buffer


def show_window(window, program, loc, loc_color, vertices):

    glfw.show_window(window)

    glEnable(GL_DEPTH_TEST)

    while not glfw.window_should_close(window):

        glfw.poll_events()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glClearColor(1.0, 1.0, 1.0, 1.0)

        mat_transform = np.zeros((4, 4), np.float32)
        mat_transform = apply_transformations()

        loc = glGetUniformLocation(program, "mat_transformation")
        glUniformMatrix4fv(loc, 1, GL_TRUE, mat_transform)

        # glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

        # Drawing cylinder side
        for polygonm in range(0, len(vertices) - (2 * 60), 3):

            random.seed(polygonm)
            R = random.random()
            G = random.random()
            # B = random.random()
            glUniform4f(loc_color, R, G, 1.0, 1.0)
            glDrawArrays(GL_TRIANGLES, polygonm, 3)

        # Drawing cylinder top
        glUniform4f(loc_color, 0.521, 0.521, 1, 1)
        glDrawArrays(GL_TRIANGLE_FAN, len(vertices) - 2 * 60, 60)

        # Drawing cylinder base
        glUniform4f(loc_color, 0.521, 0.521, 1, 1)
        glDrawArrays(GL_TRIANGLE_FAN, len(vertices) - 60, 60)

        glfw.swap_buffers(window)

    glfw.terminate()


def init():

    window = start_window()

    vertex_code = """
        attribute vec3 position;
        uniform mat4 mat_transformation;
        void main(){
            gl_Position = mat_transformation * vec4(position,1.0);
        }
        """

    fragment_code = """
        uniform vec4 color;
        void main(){
            gl_FragColor = color;
        }
        """

    # Request a program and shader slots from GPU
    program = glCreateProgram()
    vertex = glCreateShader(GL_VERTEX_SHADER)
    fragment = glCreateShader(GL_FRAGMENT_SHADER)

    set_and_compile_shader(program, vertex, vertex_code)
    set_and_compile_shader(program, fragment, fragment_code)

    # Build program
    glLinkProgram(program)
    if not glGetProgramiv(program, GL_LINK_STATUS):
        print(glGetProgramInfoLog(program))
        raise RuntimeError('Linking error')

    # Make program the default program
    glUseProgram(program)

    vertices = draw_object()

    buffer = send_to_gpu(vertices)

    # Bind the position attribute
    stride = vertices.strides[0]
    offset = ctypes.c_void_p(0)

    loc = glGetAttribLocation(program, "position")
    glEnableVertexAttribArray(loc)

    glVertexAttribPointer(loc, 3, GL_FLOAT, False, stride, offset)

    loc_color = glGetUniformLocation(program, "color")

    show_window(window, program, loc, loc_color, vertices)


# global var
angle = 0.0
anglex = 0.0
angley = 0.0
anglez = 0.0
radius = 0.3
height = 1.0
t_x = 0.0
t_y = 0.0
t_z = 0.0
s_x = 1.0
s_y = 1.0
s_z = 1.0
PI = 3.1415926

init()
