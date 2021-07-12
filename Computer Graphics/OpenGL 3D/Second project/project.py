# Second Project to SCC0250 - Computer Graphics
# Professor Ricardo Marcacini
#
# Group members
# Bruno dos Santos                  NUSP 10786170
# Henrique de S. Q. dos Santos      NUSP 10819029
# Witor M. A. de Oliveira           NUSP 10692190

import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np
import glm
import math
from PIL import Image


def key_event(window, key, scancode, action, mods):
    global fovy, aspect, near, far
    global cameraPos, cameraFront, cameraUp, polygonal_mode

    cameraSpeed = 5
    if key == 87 and (action == 1 or action == 2):  # key W
        cameraPos += cameraSpeed * cameraFront

    if key == 83 and (action == 1 or action == 2):  # key S
        cameraPos -= cameraSpeed * cameraFront

    if key == 65 and (action == 1 or action == 2):  # key A
        cameraPos -= glm.normalize(glm.cross(cameraFront,
                                   cameraUp)) * cameraSpeed

    if key == 68 and (action == 1 or action == 2):  # key D
        cameraPos += glm.normalize(glm.cross(cameraFront,
                                   cameraUp)) * cameraSpeed

    if cameraPos[1] > 97:
        cameraPos[1] = 97
    elif cameraPos[1] < 1:
        cameraPos[1] = 1

    if cameraPos[0] < -96:
        cameraPos[0] = -96
    elif cameraPos[0] > 96:
        cameraPos[0] = 96

    if cameraPos[2] < -96:
        cameraPos[2] = -96
    elif cameraPos[2] > 96:
        cameraPos[2] = 96

    if key == 80 and action == 1 and polygonal_mode == True:
        polygonal_mode = False
    elif key == 80 and action == 1 and polygonal_mode == False:
        polygonal_mode = True

    if key == 49:  # key 1, increase 'fovy'
        fovy += 1
    elif key == 50:  # key 2, decrease 'fovy'
        fovy -= 1

    if key == 51:  # key 3, increase 'aspect'
        aspect += 0.1
    elif key == 52:  # key 4, decrease 'aspect'
        aspect -= 0.1

    if key == 53:  # key 5, increase 'near'
        near += 0.1
    elif key == 54:  # key 6, decrease 'near'
        near -= 0.1

    if key == 55:  # key 7, increase 'far'
        far += 500
    elif key == 56:  # key 8, decrease 'far'
        far -= 500


def mouse_event(window, xpos, ypos):

    global firstMouse, cameraFront, yaw, pitch, lastX, lastY

    if firstMouse:
        lastX = xpos
        lastY = ypos
        firstMouse = False

    xoffset = xpos - lastX
    yoffset = lastY - ypos
    lastX = xpos
    lastY = ypos

    sensitivity = 0.3
    xoffset *= sensitivity
    yoffset *= sensitivity

    yaw += xoffset
    pitch += yoffset

    if pitch >= 90.0:
        pitch = 90.0
    if pitch <= -90.0:
        pitch = -90.0

    front = glm.vec3()
    front.x = math.cos(glm.radians(yaw)) * math.cos(glm.radians(pitch))
    front.y = math.sin(glm.radians(pitch))
    front.z = math.sin(glm.radians(yaw)) * math.cos(glm.radians(pitch))
    cameraFront = glm.normalize(front)


def start_window(largura, altura):
    glfw.init()
    glfw.window_hint(glfw.VISIBLE, glfw.FALSE)
    window = glfw.create_window(largura, altura, "3D", None, None)
    glfw.make_context_current(window)

    glfw.set_key_callback(window, key_event)  # gets keyboard inputs
    glfw.set_cursor_pos_callback(window, mouse_event)  # gets mouse inputs

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


def model(angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z):

    angle = math.radians(angle)

    matrix_transform = glm.mat4(1.0)  # instanciando uma matriz identidade

    # aplicando translacao
    matrix_transform = glm.translate(matrix_transform, glm.vec3(t_x, t_y, t_z))

    # aplicando rotacao
    matrix_transform = glm.rotate(
        matrix_transform, angle, glm.vec3(r_x, r_y, r_z))

    # aplicando escala
    matrix_transform = glm.scale(matrix_transform, glm.vec3(s_x, s_y, s_z))

    # pegando a transposta da matriz (glm trabalha com ela invertida)
    matrix_transform = np.array(matrix_transform).T

    return matrix_transform


def view():
    global cameraPos, cameraFront, cameraUp
    mat_view = glm.lookAt(cameraPos, cameraPos + cameraFront, cameraUp)
    mat_view = np.array(mat_view)
    return mat_view


def projection():
    global fovy, aspect, near, far
    # perspective parameters: fovy, aspect, near, far
    mat_projection = glm.perspective(
        glm.radians(fovy), aspect, near, far)
    mat_projection = np.array(mat_projection)
    return mat_projection


def draw_ground(program):

    # aplica a matriz model

    # rotacao
    angle = 0.0
    r_x = 0.0
    r_y = 0.0
    r_z = 1.0

    # translacao
    t_x = 0.0
    t_y = 0.0
    t_z = 0.0

    # escala
    s_x = 1
    s_y = 1
    s_z = 1

    mat_model = model(angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    loc_model = glGetUniformLocation(program, "model")
    glUniformMatrix4fv(loc_model, 1, GL_TRUE, mat_model)

    # define id da textura do modelo
    glBindTexture(GL_TEXTURE_2D, 0)
    glDrawArrays(GL_TRIANGLES, 0, 6)  # renderizando


def draw_house(program):

    # aplica a matriz model

    # rotacao
    angle = 0.0
    r_x = 0.0
    r_y = 0.0
    r_z = 1.0

    # translacao
    t_x = 0.0
    t_y = 0.0
    t_z = 0.0

    # escala
    s_x = 1.0
    s_y = 1.0
    s_z = 1.0

    mat_model = model(angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    loc_model = glGetUniformLocation(program, "model")
    glUniformMatrix4fv(loc_model, 1, GL_TRUE, mat_model)

    # define id da textura do modelo
    glBindTexture(GL_TEXTURE_2D, 1)
    glDrawArrays(GL_TRIANGLES, 6, 1434-6)  # renderizando


def draw_trees(program):

    # aplica a matriz model

    # rotacao
    angle = 0.0
    r_x = 0.0
    r_y = 0.0
    r_z = 1.0

    # translacao
    t_x = 0.0
    t_y = 0.0
    t_z = 0.0

    # escala
    s_x = 1.0
    s_y = 1.0
    s_z = 1.0

    mat_model = model(angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    loc_model = glGetUniformLocation(program, "model")
    glUniformMatrix4fv(loc_model, 1, GL_TRUE, mat_model)

    # desenha flores das arvores
    glBindTexture(GL_TEXTURE_2D, 3)
    glDrawArrays(GL_TRIANGLES, 1440, 195717-1440)  # renderizando

    glBindTexture(GL_TEXTURE_2D, 3)
    glDrawArrays(GL_TRIANGLES, 197808, 392085-197808)  # renderizando

    glBindTexture(GL_TEXTURE_2D, 3)
    glDrawArrays(GL_TRIANGLES, 394176, 588453-394176)  # renderizando

    glBindTexture(GL_TEXTURE_2D, 3)
    glDrawArrays(GL_TRIANGLES, 590544, 784821-590544)  # renderizando

    glBindTexture(GL_TEXTURE_2D, 3)
    glDrawArrays(GL_TRIANGLES, 786912, 981189-786912)  # renderizando

    # desenha tronco das arvores
    glBindTexture(GL_TEXTURE_2D, 4)
    glDrawArrays(GL_TRIANGLES, 392085, 394176-392085)  # renderizando

    glBindTexture(GL_TEXTURE_2D, 4)
    glDrawArrays(GL_TRIANGLES, 195717, 197808-195717)  # renderizando

    glBindTexture(GL_TEXTURE_2D, 4)
    glDrawArrays(GL_TRIANGLES, 588453, 590544-588453)  # renderizando

    glBindTexture(GL_TEXTURE_2D, 4)
    glDrawArrays(GL_TRIANGLES, 784821, 786912-784821)  # renderizando

    glBindTexture(GL_TEXTURE_2D, 4)
    glDrawArrays(GL_TRIANGLES, 981189, 983280-981189)  # renderizando


def draw_frog(program):

    # aplica a matriz model

    # rotacao
    angle = 0.0
    r_x = 0.0
    r_y = 0.0
    r_z = 1.0

    # translacao
    t_x = 0.0
    t_y = 0.0
    t_z = 0.0

    # escala
    s_x = 1.0
    s_y = 1.0
    s_z = 1.0

    mat_model = model(angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    loc_model = glGetUniformLocation(program, "model")
    glUniformMatrix4fv(loc_model, 1, GL_TRUE, mat_model)

    # desenha flores das arvores
    glBindTexture(GL_TEXTURE_2D, 5)
    glDrawArrays(GL_TRIANGLES, 983280, 1157328-983280)  # renderizando


def draw_horse(program):

    # aplica a matriz model

    # rotacao
    angle = 0.0
    r_x = 0.0
    r_y = 0.0
    r_z = 1

    # translacao
    t_x = -40.0
    t_y = 0.0
    t_z = 0.0

    # escala
    s_x = 0.7
    s_y = 0.7
    s_z = 0.7

    mat_model = model(angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    loc_model = glGetUniformLocation(program, "model")
    glUniformMatrix4fv(loc_model, 1, GL_TRUE, mat_model)

    # desenha cvaalo
    glBindTexture(GL_TEXTURE_2D, 10)
    glDrawArrays(GL_TRIANGLES, 1157328, 1256952-1157328)  # renderizando

    glBindTexture(GL_TEXTURE_2D, 11)
    glDrawArrays(GL_TRIANGLES, 1157328, 1256952-1157328)  # renderizando

    glBindTexture(GL_TEXTURE_2D, 12)
    glDrawArrays(GL_TRIANGLES, 1157328, 1256952-1157328)  # renderizando

    glBindTexture(GL_TEXTURE_2D, 6)
    glDrawArrays(GL_TRIANGLES, 1256952, 1274052-1256952)  # renderizando

    glBindTexture(GL_TEXTURE_2D, 7)
    glDrawArrays(GL_TRIANGLES, 1276332, 1282092-1276332)  # renderizando


def draw_chair(program):

    # aplica a matriz model

    # rotacao
    angle = 0.0
    r_x = 0.0
    r_y = 0.0
    r_z = 1.0

    # translacao
    t_x = 0.0
    t_y = 0.0
    t_z = 0.0

    # escala
    s_x = 1.0
    s_y = 1.0
    s_z = 1.0

    mat_model = model(angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    loc_model = glGetUniformLocation(program, "model")
    glUniformMatrix4fv(loc_model, 1, GL_TRUE, mat_model)

    glBindTexture(GL_TEXTURE_2D, 13)
    glDrawArrays(GL_TRIANGLES, 1282092, 2753433-1282092)  # renderizando


def draw_screen(program):

    # aplica a matriz model

    # rotacao
    angle = 0.0
    r_x = 0.0
    r_y = 0.0
    r_z = 1.0

    # translacao
    t_x = 0.0
    t_y = 0.0
    t_z = 0.0

    # escala
    s_x = 1.0
    s_y = 1.0
    s_z = 1.0

    mat_model = model(angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    loc_model = glGetUniformLocation(program, "model")
    glUniformMatrix4fv(loc_model, 1, GL_TRUE, mat_model)

    glBindTexture(GL_TEXTURE_2D, 14)
    glDrawArrays(GL_TRIANGLES, 2753433, 2764542-2753433)  # renderizando

    glBindTexture(GL_TEXTURE_2D, 15)
    glDrawArrays(GL_TRIANGLES, 2764542, 2765082-2764542)  # renderizando

    glBindTexture(GL_TEXTURE_2D, 14)
    glDrawArrays(GL_TRIANGLES, 2765082, 2765112-2765082)  # renderizando

    glBindTexture(GL_TEXTURE_2D, 16)
    glDrawArrays(GL_TRIANGLES, 2765112, 2765382-2765112)  # renderizando

    glBindTexture(GL_TEXTURE_2D, 17)
    glDrawArrays(GL_TRIANGLES, 2765382, 2766762-2765382)  # renderizando


def draw_table(program):

    # aplica a matriz model

    # rotacao
    angle = 0.0
    r_x = 0.0
    r_y = 0.0
    r_z = 1.0

    # translacao
    t_x = 0.0
    t_y = 0.0
    t_z = 0.0

    # escala
    s_x = 1.0
    s_y = 1.0
    s_z = 1.0

    mat_model = model(angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    loc_model = glGetUniformLocation(program, "model")
    glUniformMatrix4fv(loc_model, 1, GL_TRUE, mat_model)

    glBindTexture(GL_TEXTURE_2D, 18)
    glDrawArrays(GL_TRIANGLES, 2766762, 2767818-2766762)  # renderizando


def draw_cpu(program):

    # aplica a matriz model

    # rotacao
    angle = 0.0
    r_x = 0.0
    r_y = 0.0
    r_z = 1.0

    # translacao
    t_x = 0.0
    t_y = 0.0
    t_z = 0.0

    # escala
    s_x = 1.0
    s_y = 1.0
    s_z = 1.0

    mat_model = model(angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    loc_model = glGetUniformLocation(program, "model")
    glUniformMatrix4fv(loc_model, 1, GL_TRUE, mat_model)

    glBindTexture(GL_TEXTURE_2D, 17)
    glDrawArrays(GL_TRIANGLES, 2767818, 2767962-2767818)  # renderizando

    glBindTexture(GL_TEXTURE_2D, 14)
    glDrawArrays(GL_TRIANGLES, 2767962, 3361914-2767962)  # renderizando


def draw_wind_mill_body(program):

    # aplica a matriz model

    # rotacao
    angle = 0.0
    r_x = 0.0
    r_y = 0.0
    r_z = 1.0

    # translacao
    t_x = 40.0
    t_y = 0.0
    t_z = 0.0

    # escala
    s_x = 1.0
    s_y = 1.0
    s_z = 1.0

    mat_model = model(angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    loc_model = glGetUniformLocation(program, "model")
    glUniformMatrix4fv(loc_model, 1, GL_TRUE, mat_model)

    glBindTexture(GL_TEXTURE_2D, 20)
    glDrawArrays(GL_TRIANGLES, 3364872, 3364974-3364872)  # renderizando

    glBindTexture(GL_TEXTURE_2D, 20)
    glDrawArrays(GL_TRIANGLES, 3364974, 3371022-3364974)  # renderizando

    glBindTexture(GL_TEXTURE_2D, 20)
    glDrawArrays(GL_TRIANGLES, 3371022, 3371154-3371022)  # renderizando

    glBindTexture(GL_TEXTURE_2D, 25)
    glDrawArrays(GL_TRIANGLES, 3371154, 3371922-3371154)  # renderizando

    glBindTexture(GL_TEXTURE_2D, 22)
    glDrawArrays(GL_TRIANGLES, 3371922, 3371970-3371922)  # renderizando

    glBindTexture(GL_TEXTURE_2D, 24)
    glDrawArrays(GL_TRIANGLES, 3371970, 3372390-3371970)  # renderizando


def draw_wind_mill_circle(program, rotacao_inc):

    # aplica a matriz model
    # rotacao
    r_x = 1.0
    r_y = 0.0
    r_z = 0.0

    # translacao
    t_x = 30.8
    t_y = 40.4
    t_z = -0.5

    # escala
    s_x = 1.0
    s_y = 1.0
    s_z = 1.0

    mat_model = model(rotacao_inc, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    loc_model = glGetUniformLocation(program, "model")
    glUniformMatrix4fv(loc_model, 1, GL_TRUE, mat_model)

    glBindTexture(GL_TEXTURE_2D, 21)
    glDrawArrays(GL_TRIANGLES, 3361914, 3363042-3361914)  # renderizando

    glBindTexture(GL_TEXTURE_2D, 21)
    glDrawArrays(GL_TRIANGLES, 3363042, 3364578-3363042)  # renderizando

    glBindTexture(GL_TEXTURE_2D, 23)
    glDrawArrays(GL_TRIANGLES, 3364578, 3364596-3364578)  # renderizando

    glBindTexture(GL_TEXTURE_2D, 23)
    glDrawArrays(GL_TRIANGLES, 3364596, 3364614-3364596)  # renderizando

    glBindTexture(GL_TEXTURE_2D, 23)
    glDrawArrays(GL_TRIANGLES, 3364614, 3364800-3364614)  # renderizando

    glBindTexture(GL_TEXTURE_2D, 23)
    glDrawArrays(GL_TRIANGLES, 3364800, 3364854-3364800)  # renderizando

    glBindTexture(GL_TEXTURE_2D, 23)
    glDrawArrays(GL_TRIANGLES, 3364854, 3364872-3364854)  # renderizando


def draw_sky(program):

    # aplica a matriz model
    # rotacao
    angle = 0
    r_x = 1.0
    r_y = 0.0
    r_z = 0.0

    # translacao
    t_x = 0
    t_y = 0
    t_z = 0

    # escala
    s_x = 1.0
    s_y = 1.0
    s_z = 1.0

    mat_model = model(angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    loc_model = glGetUniformLocation(program, "model")
    glUniformMatrix4fv(loc_model, 1, GL_TRUE, mat_model)

    glBindTexture(GL_TEXTURE_2D, 28)
    glDrawArrays(GL_TRIANGLES, 3372390, 3372426-3372390)  # renderizando


def draw_street(program):

    # aplica a matriz model
    # rotacao
    angle = 0
    r_x = 1.0
    r_y = 0.0
    r_z = 0.0

    # translacao
    t_x = 0
    t_y = 0
    t_z = 0

    # escala
    s_x = 1.0
    s_y = 1.0
    s_z = 1.0

    mat_model = model(angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    loc_model = glGetUniformLocation(program, "model")
    glUniformMatrix4fv(loc_model, 1, GL_TRUE, mat_model)

    glBindTexture(GL_TEXTURE_2D, 29)
    glDrawArrays(GL_TRIANGLES, 3372426, 3372432-3372426)  # renderizando


def draw_secondary_yard(program):

    # aplica a matriz model
    # rotacao
    angle = 0
    r_x = 1.0
    r_y = 0.0
    r_z = 0.0

    # translacao
    t_x = 0
    t_y = 0
    t_z = 0

    # escala
    s_x = 1.0
    s_y = 1.0
    s_z = 1.0

    mat_model = model(angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    loc_model = glGetUniformLocation(program, "model")
    glUniformMatrix4fv(loc_model, 1, GL_TRUE, mat_model)

    glBindTexture(GL_TEXTURE_2D, 0)
    glDrawArrays(GL_TRIANGLES, 3372432, 3372438-3372432)  # renderizando


def draw_floor(program):

    # aplica a matriz model
    # rotacao
    angle = 0
    r_x = 1.0
    r_y = 0.0
    r_z = 0.0

    # translacao
    t_x = 0
    t_y = 0
    t_z = 0

    # escala
    s_x = 1.0
    s_y = 1.0
    s_z = 1.0

    mat_model = model(angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    loc_model = glGetUniformLocation(program, "model")
    glUniformMatrix4fv(loc_model, 1, GL_TRUE, mat_model)

    glBindTexture(GL_TEXTURE_2D, 30)
    glDrawArrays(GL_TRIANGLES, 3372438, 3372522-3372438)  # renderizando


def draw_keyboard(program):

    # aplica a matriz model
    # rotacao
    angle = 0
    r_x = 1.0
    r_y = 0.0
    r_z = 0.0

    # translacao
    t_x = 0
    t_y = 0
    t_z = 0

    # escala
    s_x = 1.0
    s_y = 1.0
    s_z = 1.0

    mat_model = model(angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    loc_model = glGetUniformLocation(program, "model")
    glUniformMatrix4fv(loc_model, 1, GL_TRUE, mat_model)

    glBindTexture(GL_TEXTURE_2D, 31)
    glDrawArrays(GL_TRIANGLES, 3372522, 3464400-3372522)  # renderizando


def upload_data(buffer, data, program, size, name):
    # Make this buffer the default one
    glBindBuffer(GL_ARRAY_BUFFER, buffer)
    glBufferData(GL_ARRAY_BUFFER, data.nbytes, data, GL_STATIC_DRAW)

    stride = data.strides[0]
    offset = ctypes.c_void_p(0)

    loc = glGetAttribLocation(program, name)

    glEnableVertexAttribArray(loc)
    glVertexAttribPointer(loc, size, GL_FLOAT, False, stride, offset)


def send_to_gpu(vertices_list, textures_list, program):

    # Request a buffer slot from GPU
    buffer = glGenBuffers(2)

    # First, send the vertices list
    vertices = np.zeros(len(vertices_list), [("position", np.float32, 3)])
    vertices['position'] = vertices_list
    upload_data(buffer[0], vertices, program, 3, "position")

    # Now, send the textures coordinates list
    textures = np.zeros(len(textures_list), [("position", np.float32, 2)])
    textures['position'] = textures_list
    upload_data(buffer[1], textures, program, 2, "texture_coord")

    return buffer


def show_window(window, program):

    glfw.show_window(window)
    glfw.set_cursor_pos(window, lastX, lastY)

    glEnable(GL_DEPTH_TEST)

    rotacao_inc = 0

    while not glfw.window_should_close(window):

        glfw.poll_events()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glClearColor(1.0, 1.0, 1.0, 1.0)

        if polygonal_mode == True:
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        if polygonal_mode == False:
            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

        draw_ground(program)
        draw_house(program)
        draw_trees(program)
        draw_frog(program)
        draw_horse(program)
        draw_chair(program)
        draw_screen(program)
        draw_table(program)
        draw_cpu(program)
        draw_wind_mill_body(program)
        draw_wind_mill_circle(program, rotacao_inc)
        draw_sky(program)
        draw_street(program)
        draw_secondary_yard(program)
        draw_floor(program)
        draw_keyboard(program)

        rotacao_inc += 0.1

        mat_view = view()
        loc_view = glGetUniformLocation(program, "view")
        glUniformMatrix4fv(loc_view, 1, GL_FALSE, mat_view)

        mat_projection = projection()
        loc_projection = glGetUniformLocation(program, "projection")
        glUniformMatrix4fv(loc_projection, 1, GL_FALSE, mat_projection)

        glfw.swap_buffers(window)

    glfw.terminate()


def load_model_from_file(filename):
    """
    Loads a Wavefront OBJ file. 
    Code by Ricardo Marcacini.
    """

    objects = {}
    vertices = []
    texture_coords = []
    faces = []

    material = None

    # abre o arquivo obj para leitura
    for line in open(filename, "r", encoding="utf-8"):  # para cada linha do arquivo .obj
        if line.startswith('#'):
            continue  # ignora comentarios
        values = line.split()  # quebra a linha por espaço
        if not values:
            continue

        # recuperando vertices
        if values[0] == 'v':
            vertices.append(values[1:4])

        # recuperando coordenadas de textura
        elif values[0] == 'vt':
            texture_coords.append(values[1:3])

        # recuperando faces
        elif values[0] in ('usemtl', 'usemat'):
            material = values[1]
        elif values[0] == 'f':
            face = []
            face_texture = []
            for v in values[1:]:
                w = v.split('/')
                face.append(int(w[0]))
                if len(w) >= 2 and len(w[1]) > 0:
                    face_texture.append(int(w[1]))
                else:
                    face_texture.append(0)

            faces.append((face, face_texture, material))

    model = {}
    model['vertices'] = vertices
    model['texture'] = texture_coords
    model['faces'] = faces

    return model


def load_texture_from_file(texture_id, img_textura):
    """Code by Ricardo Marcacini"""

    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    img = Image.open(img_textura)
    img_width = img.size[0]
    img_height = img.size[1]
    image_data = img.convert("RGBA").tobytes("raw", "RGBA", 0, -1)
    #image_data = img.tobytes("raw", "RGB", 0, -1)
    #image_data = np.array(list(img.getdata()), np.uint8)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, img_width, img_height,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data)


def load_model_and_texture(vertices_list, textures_coord_list, model_file, texture_files, id):

    faces_visited = []
    model_name = model_file.split('/')

    # carregando o modelo e a textura equivalente e definindo um id (buffer)
    modelo = load_model_from_file(model_file)

    if len(model_name) > 1:
        print('Processing model ' +
              model_name[1] + '. Initial vertex:', len(vertices_list))
    else:
        print('Processing model ' +
              model_name[0] + '. Initial vertex:', len(vertices_list))

    # inserindo vertices do modelo no vetor de vertices
    for face in modelo['faces']:
        if face[2] not in faces_visited:
            print(face[2], ' initial vertex =', len(vertices_list))
            faces_visited.append(face[2])
        for vertice_id in face[0]:
            vertices_list.append(modelo['vertices'][vertice_id-1])
        for texture_id in face[1]:
            textures_coord_list.append(modelo['texture'][texture_id-1])

    if len(model_name) > 1:
        print('Processing model ' +
              model_name[1] + '. Vertice final:', len(vertices_list))
    else:
        print('Processing model ' +
              model_name[0] + '. Vertice final:', len(vertices_list))

    # if we're going to load only one texture for the .obj
    if type(texture_files) == str:
        load_texture_from_file(id, texture_files)

    # in case we're going to load more than one texture for the .obj.
    # we sum texture_id + id because if we loaded some texture before,
    # we need to load the new textures considering the already added ones
    elif len(texture_files) > 0:
        for texture_id in range(len(texture_files)):
            print(texture_id + id, texture_files[texture_id])
            load_texture_from_file(
                texture_id + id, texture_files[texture_id])

    return vertices_list, textures_coord_list


def generate_models_and_textures(NUM_TEXTURES):

    glHint(GL_LINE_SMOOTH_HINT, GL_DONT_CARE)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glEnable(GL_LINE_SMOOTH)
    glEnable(GL_TEXTURE_2D)

    # Generate NUM_TEXTURES textures
    textures = glGenTextures(NUM_TEXTURES)

    vertices_list = []
    textures_coord_list = []

    ground_textures = [
        'textures/ground/grama.jpg'
    ]

    house_textures = [
        'textures/cottage/cottage_diffuse.png',
        'textures/cottage/cottage_normal.png'
    ]

    trees_textures = [
        'textures/trees/leaf.jpg',
        'textures/trees/stem.jpg'
    ]

    frog_textures = [
        'textures/frog/frog.jpg'
    ]

    horse_textures = [
        'textures/horse/butthorse.png',
        'textures/horse/butthorseeye.png',
        'textures/horse/butthorsenorm.png',
        'textures/horse/butthorsespec.png',
        'textures/horse/hairblond.png',
        'textures/horse/hairblondnormal.png',
        'textures/horse/hairblondspec.png'
    ]

    chair_textures = [
        'textures/gaming_chair/lambert112SG_baseColor.png'
    ]

    screen_textures = [
        'textures/screen/texture.png',
        'textures/screen/texture1.png',
        'textures/screen/texture2.png',
        'textures/screen/texture3.png'
    ]

    table_textures = [
        'textures/table/texturaMesa.jpg'
    ]

    cpu_textures = [
        'textures/table/texturaMesa.jpg'
    ]

    win_mill_textures = [
        'textures/windMill/textures/wood.jpg',
        'textures/windMill/textures/rust1.jpg',
        'textures/windMill/textures/lightblue.png',
        'textures/windMill/textures/rust.jpg',
        'textures/windMill/textures/gray.png',
        'textures/windMill/textures/darkgray.png'
    ]

    sky_textures = [
        'textures/sky/ceu_texture.png',
    ]

    street_textures = [
        'textures/ground/rua.jpg',
    ]

    floor_textures = [
        'textures/ground/piso.jpg',
    ]

    keyboard_textures = [
        'textures/keyboard/pl.jpg',
    ]

    vertices_list, textures_coord_list = load_model_and_texture(
        vertices_list, textures_coord_list, 'textures/ground/quintal.obj', ground_textures, 0)

    vertices_list, textures_coord_list = load_model_and_texture(
        vertices_list, textures_coord_list, 'textures/cottage/cottage_obj.obj', house_textures, 1)

    vertices_list, textures_coord_list = load_model_and_texture(
        vertices_list, textures_coord_list, 'textures/trees/birch_tree.obj', trees_textures, 3)

    vertices_list, textures_coord_list = load_model_and_texture(
        vertices_list, textures_coord_list, 'textures/frog/frog.obj', frog_textures, 5)

    vertices_list, textures_coord_list = load_model_and_texture(
        vertices_list, textures_coord_list, 'textures/horse/horse.obj', horse_textures, 6)

    vertices_list, textures_coord_list = load_model_and_texture(
        vertices_list, textures_coord_list, 'textures/gaming_chair/chair.obj', chair_textures, 13)

    vertices_list, textures_coord_list = load_model_and_texture(
        vertices_list, textures_coord_list, 'textures/screen/tela.obj', screen_textures, 14)

    vertices_list, textures_coord_list = load_model_and_texture(
        vertices_list, textures_coord_list, 'textures/table/mesa.obj', table_textures, 18)

    vertices_list, textures_coord_list = load_model_and_texture(
        vertices_list, textures_coord_list, 'textures/cpu/cpu.obj', cpu_textures, 19)

    vertices_list, textures_coord_list = load_model_and_texture(
        vertices_list, textures_coord_list, 'textures/windMill/rodaMoinho2.obj', win_mill_textures, 20)

    vertices_list, textures_coord_list = load_model_and_texture(
        vertices_list, textures_coord_list, 'textures/windMill/corpoMoinho1.obj', [], 20)

    vertices_list, textures_coord_list = load_model_and_texture(
        vertices_list, textures_coord_list, 'textures/sky/ceu.obj', sky_textures, 28)

    vertices_list, textures_coord_list = load_model_and_texture(
        vertices_list, textures_coord_list, 'textures/ground/rua.obj', street_textures, 29)

    vertices_list, textures_coord_list = load_model_and_texture(
        vertices_list, textures_coord_list, 'textures/ground/quintal_lado_oposto.obj', ground_textures, 0)

    vertices_list, textures_coord_list = load_model_and_texture(
        vertices_list, textures_coord_list, 'textures/ground/piso.obj', floor_textures, 30)

    vertices_list, textures_coord_list = load_model_and_texture(
        vertices_list, textures_coord_list, 'textures/keyboard/keyboard.obj', keyboard_textures, 31)

    return vertices_list, textures_coord_list


def init():

    global largura, altura, aspect
    largura = 1600
    altura = 1200
    aspect = largura/altura

    window = start_window(largura, altura)

    vertex_code = """
        attribute vec3 position;
        attribute vec2 texture_coord;
        varying vec2 out_texture;
                
        uniform mat4 model;
        uniform mat4 view;
        uniform mat4 projection;        
        
        void main(){
            gl_Position = projection * view * model * vec4(position,1.0);
            out_texture = vec2(texture_coord);
        }
        """

    fragment_code = """
        uniform vec4 color;
        varying vec2 out_texture;
        uniform sampler2D samplerTexture;
        
        void main(){
            vec4 texture = texture2D(samplerTexture, out_texture);
            gl_FragColor = texture;
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

    # generate models considering NUM_TEXTURES textures
    NUM_TEXTURES = 1000
    vertices_list, textures_coord_list = generate_models_and_textures(
        NUM_TEXTURES)

    buffer = send_to_gpu(vertices_list, textures_coord_list, program)

    show_window(window, program)


# global vars
largura = 0
altura = 0

cameraPos = glm.vec3(50.0,  20.0,  1.0)
cameraFront = glm.vec3(0.0,  0.0, -1.0)
cameraUp = glm.vec3(0.0,  1.0,  0.0)

firstMouse = True
yaw = -90.0
pitch = 0.0
lastX = largura/2
lastY = altura/2

fovy = 45.0
aspect = 0
near = 0.1
far = 1000.0

polygonal_mode = False

init()
