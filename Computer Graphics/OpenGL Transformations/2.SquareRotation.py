import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np
import math


def rotation():

    global angle

    rad = math.radians(angle)

    c = math.cos(rad)
    s = math.sin(rad)

    mat_translation = np.array([c, -s, 0.0, 0,
                                s, c, 0.0, 0,
                                0.0, 0.0, 0, 0.0,
                                0.0, 0.0, 0.0, 1.0], np.float32)

    return mat_translation


def key_event(window, key, scancode, action, mods):
    print('[key event] key=', key)
    print('[key event] scancode=', scancode)
    print('[key event] action=', action)
    print('[key event] mods=', mods)
    print('-------')

    global angle

    if key == 263:
        angle += 1  # left
    if key == 262:
        angle -= 1  # right


def start_window():
    glfw.init()
    glfw.window_hint(glfw.VISIBLE, glfw.FALSE)
    window = glfw.create_window(720, 600, "SquareRotation", None, None)
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
        raise RuntimeError("Erro de compilacao no Shader")

    # Attach shader objects to the program
    glAttachShader(program, slot)


def draw_object():
    # prepare space for 4 vertices using 2d coords (x,y)
    vertices = np.zeros(4, [("position", np.float32, 2)])

    vertices['position'] = [
        (+0.5, -0.5),
        (+0.5, +0.5),
        (-0.5, -0.5),
        (-0.5, +0.5)
    ]

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

    R = 1.0
    G = 0.0
    B = 0.0

    glfw.show_window(window)

    while not glfw.window_should_close(window):

        glfw.poll_events()

        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(1.0, 1.0, 1.0, 1.0)

        # Draw Triangle
        mat_translation = np.zeros((4, 4), np.float32)
        mat_translation = rotation()

        loc = glGetUniformLocation(program, "mat_transformation")
        glUniformMatrix4fv(loc, 1, GL_TRUE, mat_translation)

        glDrawArrays(GL_TRIANGLE_STRIP, 0, len(vertices))
        glUniform4f(loc_color, R, G, B, 1.0)  # modificando a cor do objeto!

        glfw.swap_buffers(window)

    glfw.terminate()


def init():

    window = start_window()

    vertex_code = """
        attribute vec2 position;
        uniform mat4 mat_transformation;
        void main(){
            gl_Position = mat_transformation * vec4(position,0.0,1.0);
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

    glVertexAttribPointer(loc, 2, GL_FLOAT, False, stride, offset)

    loc_color = glGetUniformLocation(program, "color")

    show_window(window, program, loc, loc_color, vertices)


# global var
angle = 0
t_x = 0
t_y = 0
e_x = 0
e_y = 0

init()
