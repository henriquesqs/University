# Graphical Computing 2021
# Code based on the examples provided by Professor Ricardo M. Marcacini
# Henrique de S. Q. dos Santos - NUSP 10819029

import math
import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np

# Start GLFW window
glfw.init()

# Create a 720x600 window (but do not show yet)
glfw.window_hint(glfw.VISIBLE, glfw.FALSE)
window = glfw.create_window(
    720, 600, "A night at space with my starship...", None, None)
glfw.make_context_current(window)

# Create a vertex using GLSL
vertex_code = """
        attribute vec2 position;
        void main(){
            gl_Position = vec4(position,0.0,1.0);
        }
        """

# Define the vertex color
# gl_FragColor(R,G,B,Alpha) uses normalized values
fragment_code = """
        uniform vec4 color;
        void main(){
            // gl_FragColor = vec4(1, 0.952, 0.039,1);
            gl_FragColor = color;
        }
        """

# Request a program and shader slots from GPU
program = glCreateProgram()
vertex = glCreateShader(GL_VERTEX_SHADER)
fragment = glCreateShader(GL_FRAGMENT_SHADER)

# Set shaders source
glShaderSource(vertex, vertex_code)
glShaderSource(fragment, fragment_code)

# Compile shaders
glCompileShader(vertex)
if not glGetShaderiv(vertex, GL_COMPILE_STATUS):
    error = glGetShaderInfoLog(vertex).decode()
    print(error)
    raise RuntimeError("Vertex Shader compilation error")

glCompileShader(fragment)
if not glGetShaderiv(fragment, GL_COMPILE_STATUS):
    error = glGetShaderInfoLog(fragment).decode()
    print(error)
    raise RuntimeError("Fragment Shader compilation error")

# Attach shader objects to the program
glAttachShader(program, vertex)
glAttachShader(program, fragment)

# Build program
glLinkProgram(program)
if not glGetProgramiv(program, GL_LINK_STATUS):
    print(glGetProgramInfoLog(program))
    raise RuntimeError('Linking error')

# Make program the default program
glUseProgram(program)

# Start to send data from CPU to GPU

################################
###### OBJECTS DEFINITION ######
################################

numObjects = 501    # define how many objects to use for our primitives
dimension = 2       # dimension defines that is 2d (x,y)

vertices = np.zeros(numObjects - 1, [("position", np.float32, dimension)])

# Define "numObjects" STARS
vertices['position'] = np.random.uniform(-1, 1, (numObjects - 1, 2))

# Define the MOON
qual = 64  # quality of circle

# Circle data
pi = 3.14
radius = 0.2
angle = 1.0

counter = 0  # aux var

for counter in range(0, qual):
    angle += 2 * pi / qual
    x = math.cos(angle) * radius
    y = math.sin(angle) * radius
    vertices['position'][counter] = [x + 0.6, y + 0.7]

# Define the CLOUDS
vertices.resize(509)

xCenter = -0.5
yCenter = 0.5
vertices['position'][501] = [xCenter+0.2, yCenter-0.1]
vertices['position'][502] = [xCenter+0.2, yCenter+0.1]
vertices['position'][503] = [xCenter-0.2, yCenter-0.1]
vertices['position'][504] = [xCenter-0.2, yCenter+0.1]

xCenter = 0
yCenter = 0.7
vertices['position'][505] = [xCenter+0.2, yCenter-0.1]
vertices['position'][506] = [xCenter+0.2, yCenter+0.1]
vertices['position'][507] = [xCenter-0.2, yCenter-0.1]
vertices['position'][508] = [xCenter-0.2, yCenter+0.1]

# Define the LINE
vertices.resize(511)
vertices['position'][509] = [-1.0, -0.5]
vertices['position'][510] = [1, -0.5]

# Define the SPACESHIP
vertices.resize(514)
xCenter = -1
yCenter = -0.5
vertices['position'][511] = [xCenter, yCenter + 0.1]
vertices['position'][512] = [xCenter, yCenter - 0.1]
vertices['position'][513] = [xCenter + 0.5, yCenter]

################################

# To send data to GPU, we need to request a slot
# Request a buffer slot from GPU
buffer = glGenBuffers(1)

# Make this buffer the default one
glBindBuffer(GL_ARRAY_BUFFER, buffer)

# Upload data
glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_DYNAMIC_DRAW)
glBindBuffer(GL_ARRAY_BUFFER, buffer)

# Bind the position attribute
stride = vertices.strides[0]
offset = ctypes.c_void_p(0)

# Get position of variable 'position' defined in vertices['position']
loc = glGetAttribLocation(program, "position")
loc_color = glGetUniformLocation(program, "color")
glEnableVertexAttribArray(loc)

# Tell the GPU where is the variable "position"
glVertexAttribPointer(loc, 2, GL_FLOAT, False, stride, offset)

# Show window
glfw.show_window(window)

R = 0
G = 0
B = 0
increase = True
offsetX = 0

while not glfw.window_should_close(window):

    # This makes the window background color change from black to blue
    if increase == True and B >= 1:
        increase = False

    if increase == False and B <= 0:
        increase = True

    if increase:
        B = B + 0.01
        offsetX = offsetX + 0.015  # to move the spaceship forward
    else:
        B = B - 0.01
        offsetX = offsetX - 0.015  # to move the spaceship backward

    vertices['position'][511] = [xCenter + offsetX, yCenter + 0.1]
    vertices['position'][512] = [xCenter + offsetX, yCenter - 0.1]
    vertices['position'][513] = [xCenter + 0.5 + offsetX, yCenter]

    # Update the bufferdata to define the new position of the startship
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_DYNAMIC_DRAW)
    glBindBuffer(GL_ARRAY_BUFFER, buffer)

    # glfw function to manage mouse, keyboard events
    glfw.poll_events()

    # clean the window default background color ans sets another
    glClear(GL_COLOR_BUFFER_BIT)

    # set the window color
    glClearColor(R, G, B, 1)

    # Define a line
    glUniform4f(loc_color, 1, 1, 1, 1)
    glDrawArrays(GL_LINES, 509, 2)

    # Set the next objects color as yellow
    glUniform4f(loc_color, 1, 1, 0, 1)

    # Define "stars"
    glDrawArrays(GL_POINTS, 64, 500)

    # Define the "spaceship"
    glDrawArrays(GL_TRIANGLES, 511, 3)

    # Set the next objects color as white
    glUniform4f(loc_color, 1, 1, 1, 1)

    # Define "clouds" (yes, clouds on space)
    glDrawArrays(GL_TRIANGLE_STRIP, 501, 4)
    glDrawArrays(GL_TRIANGLE_STRIP, 505, 4)

    # Set the next objects color as gray
    glUniform4f(loc_color, 0.521, 0.521, 0.521, 1)

    # Define "moon"
    glDrawArrays(GL_TRIANGLE_FAN, 0, 64)

    # manage data exchange between window and OpenGL
    glfw.swap_buffers(window)

glfw.terminate()
