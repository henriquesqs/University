import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np
import math


def translation():

    return np.array([1.0, 0.0, 0.0, t_x,
                    0.0, 1.0, 0.0, t_y,
                    0.0, 0.0, 1.0, 0.0,
                    0.0, 0.0, 0.0, 1.0], np.float32)


def rotation():

    global angulo

    rad = math.radians(angulo)

    c = math.cos(rad)
    s = math.sin(rad)

    return np.array([c, -s, 0.0, 0,
                     s, c, 0.0, 0,
                     0.0, 0.0, 0, 0.0,
                     0.0, 0.0, 0.0, 1.0], np.float32)


def key_event(window, key, scancode, action, mods):
    print('[key event] key=', key)
    print('[key event] scancode=', scancode)
    print('[key event] action=', action)
    print('[key event] mods=', mods)
    print('-------')

    global t_x, t_y
    key == 65 or key == 264

    if key == 87 or key == 265:  # W
        t_y += 0.01
    if key == 65 or key == 263:  # A
        t_x -= 0.01
    if key == 83 or key == 264:  # S
        t_y -= 0.01
    if key == 68 or key == 262:  # D
        t_x += 0.01


def mouse_event(window, button, action, mods):
    print('[mouse event] button=', button)
    print('[mouse event] action=', action)
    print('[mouse event] mods=', mods)
    print('-------')

    global angulo

    if action == 1:
        if button == 0:
            angulo += 1  # left button
        elif button == 1:
            angulo -= 1  # right button


def init_window():
    glfw.init()
    glfw.window_hint(glfw.VISIBLE, glfw.FALSE)
    window = glfw.create_window(
        720, 600, "MoveCircleRotateTriangle", None, None)
    glfw.make_context_current(window)

    glfw.set_key_callback(window, key_event)  # gets keyboard inputs
    glfw.set_mouse_button_callback(window, mouse_event)  # gets mouse inputs

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


def draw_object():
    # prepare space for 3 (triangle) + 64 (circle) vertices using 2 coords (x,y)

    pi = 3.14
    counter = 0
    radius = 0.2
    qual = 64
    angle = 1.0

    vertices = np.zeros(3 + qual, [("position", np.float32, 2)])

    # apply the vertices coords
    vertices['position'][0] = (0.0, +0.5)   # vertice 0
    vertices['position'][1] = (-0.5, -0.5)  # vertice 1
    vertices['position'][2] = (+0.5, -0.5)  # vertice 2

    for counter in range(qual):
        angle += 2*pi/qual
        x = math.cos(angle)*radius
        y = math.sin(angle)*radius
        vertices['position'][3 + counter] = [x, y]

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

        # modificando a cor do triangulo!
        glUniform4f(loc_color, R, G, B, 1.0)
        glDrawArrays(GL_TRIANGLES, 0, 3)

        # Draw Circle
        mat_translation2 = np.zeros((4, 4), np.float32)
        mat_translation2 = translation()

        loc = glGetUniformLocation(program, "mat_transformation")
        glUniformMatrix4fv(loc, 1, GL_TRUE, mat_translation2)

        # modificando a cor do circulo!
        glUniform4f(loc_color, 0.521, 0.521, 0.521, 1)
        glDrawArrays(GL_TRIANGLE_FAN, 3, len(vertices))

        glfw.swap_buffers(window)

    glfw.terminate()


def init():

    window = init_window()

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
angulo = 0
t_x = 0
t_y = 0

init()
