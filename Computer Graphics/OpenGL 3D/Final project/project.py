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
    """ Gives functions for some keys"""

    global lightOffset
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

    # limits where the cam can go
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

    # to toggle polygonal mode
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

    if key == 85 and (action == 1 or action == 2):  # key U, increase luminosity
        lightOffset += 0.05

    if key == 73 and (action == 1 or action == 2):  # key I, decrease luminosity
        lightOffset -= 0.05


def mouse_event(window, xpos, ypos):
    """Gives functions for mouse buttons"""

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

    matrix_transform = glm.mat4(1.0)  # identity matrix

    # applies translation
    matrix_transform = glm.translate(matrix_transform, glm.vec3(t_x, t_y, t_z))

    # applies rotation
    matrix_transform = glm.rotate(
        matrix_transform, angle, glm.vec3(r_x, r_y, r_z))

    # applies scale
    matrix_transform = glm.scale(matrix_transform, glm.vec3(s_x, s_y, s_z))

    # gets transpose matrix (glm works with its inverse)
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


def load_custom_transformations_parameters(program, angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z):
    """Loads custom parameters for transformation matrix"""
    mat_model = model(angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    loc_model = glGetUniformLocation(program, "model")
    glUniformMatrix4fv(loc_model, 1, GL_TRUE, mat_model)


def load_default_transformations_parameters(program):
    """Loads predefined parameters for transformation matrix"""
    mat_model = model(0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1, 1, 1)
    loc_model = glGetUniformLocation(program, "model")
    glUniformMatrix4fv(loc_model, 1, GL_TRUE, mat_model)


def draw_ground(program):

    # applies model matrix (angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    load_default_transformations_parameters(program)

    load_light_parameters(0.1 + lightOffset, 0.1, 0.9, 64, program)

    # defines texture model id
    glBindTexture(GL_TEXTURE_2D, 0)
    glDrawArrays(GL_TRIANGLES, 0, 6)  # renders


def draw_house(program):

    # applies model matrix (angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    load_default_transformations_parameters(program)

    load_light_parameters(0.1 + lightOffset, 0.1, 0.9, 64, program)

    # defines texture model id
    glBindTexture(GL_TEXTURE_2D, 1)
    glDrawArrays(GL_TRIANGLES, 6, 1434-6)  # renders


def draw_trees(program):

    # applies model matrix (angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    load_default_transformations_parameters(program)

    load_light_parameters(0.1 + lightOffset, 0.1, 0.9, 64, program)

    # draws trees flowers
    glBindTexture(GL_TEXTURE_2D, 3)
    glDrawArrays(GL_TRIANGLES, 1440, 195717-1440)  # renders

    glBindTexture(GL_TEXTURE_2D, 3)
    glDrawArrays(GL_TRIANGLES, 197808, 392085-197808)  # renders

    glBindTexture(GL_TEXTURE_2D, 3)
    glDrawArrays(GL_TRIANGLES, 394176, 588453-394176)  # renders

    glBindTexture(GL_TEXTURE_2D, 3)
    glDrawArrays(GL_TRIANGLES, 590544, 784821-590544)  # renders

    glBindTexture(GL_TEXTURE_2D, 3)
    glDrawArrays(GL_TRIANGLES, 786912, 981189-786912)  # renders

    # draws trees torse
    glBindTexture(GL_TEXTURE_2D, 4)
    glDrawArrays(GL_TRIANGLES, 392085, 394176-392085)  # renders

    glBindTexture(GL_TEXTURE_2D, 4)
    glDrawArrays(GL_TRIANGLES, 195717, 197808-195717)  # renders

    glBindTexture(GL_TEXTURE_2D, 4)
    glDrawArrays(GL_TRIANGLES, 588453, 590544-588453)  # renders

    glBindTexture(GL_TEXTURE_2D, 4)
    glDrawArrays(GL_TRIANGLES, 784821, 786912-784821)  # renders

    glBindTexture(GL_TEXTURE_2D, 4)
    glDrawArrays(GL_TRIANGLES, 981189, 983280-981189)  # renders


def draw_frog(program):

    # applies model matrix (angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    load_default_transformations_parameters(program)

    load_light_parameters(0.1 + lightOffset, 0.1, 0.9, 64, program)

    # draws frog
    glBindTexture(GL_TEXTURE_2D, 5)
    glDrawArrays(GL_TRIANGLES, 983280, 1157328-983280)  # renders


def draw_horse(program):

    # applies model matrix (angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    load_custom_transformations_parameters(program,
                                           0.0, 0.0, 0.0, 1, -40, 0, 0, 0.7, 0.7, 0.7)

    load_light_parameters(0.1 + lightOffset, 0.1, 0.9, 64, program)

    # draws horse
    glBindTexture(GL_TEXTURE_2D, 10)
    glDrawArrays(GL_TRIANGLES, 1157328, 1256952-1157328)  # renders

    glBindTexture(GL_TEXTURE_2D, 11)
    glDrawArrays(GL_TRIANGLES, 1157328, 1256952-1157328)  # renders

    glBindTexture(GL_TEXTURE_2D, 12)
    glDrawArrays(GL_TRIANGLES, 1157328, 1256952-1157328)  # renders

    glBindTexture(GL_TEXTURE_2D, 6)
    glDrawArrays(GL_TRIANGLES, 1256952, 1274052-1256952)  # renders

    glBindTexture(GL_TEXTURE_2D, 7)
    glDrawArrays(GL_TRIANGLES, 1276332, 1282092-1276332)  # renders


def draw_chair(program):

    # applies model matrix (angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    load_default_transformations_parameters(program)

    load_light_parameters(0.1 + lightOffset, 0.1, 0.9, 64, program)

    glBindTexture(GL_TEXTURE_2D, 13)
    glDrawArrays(GL_TRIANGLES, 1282092, 2753433-1282092)  # renders


def draw_screen(program):

    # applies model matrix (angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    load_default_transformations_parameters(program)

    load_light_parameters(0.1 + lightOffset, 0.1, 0.9, 64, program)

    glBindTexture(GL_TEXTURE_2D, 14)
    glDrawArrays(GL_TRIANGLES, 2753433, 2764542-2753433)  # renders

    glBindTexture(GL_TEXTURE_2D, 15)
    glDrawArrays(GL_TRIANGLES, 2764542, 2765082-2764542)  # renders

    glBindTexture(GL_TEXTURE_2D, 14)
    glDrawArrays(GL_TRIANGLES, 2765082, 2765112-2765082)  # renders

    glBindTexture(GL_TEXTURE_2D, 16)
    glDrawArrays(GL_TRIANGLES, 2765112, 2765382-2765112)  # renders

    glBindTexture(GL_TEXTURE_2D, 17)
    glDrawArrays(GL_TRIANGLES, 2765382, 2766762-2765382)  # renders


def draw_table(program):

    # applies model matrix (angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    load_default_transformations_parameters(program)

    load_light_parameters(0.1 + lightOffset, 0.1, 0.9, 64, program)

    glBindTexture(GL_TEXTURE_2D, 18)
    glDrawArrays(GL_TRIANGLES, 2766762, 2767818-2766762)  # renders


def draw_cpu(program):

    # applies model matrix (angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    load_default_transformations_parameters(program)

    load_light_parameters(0.1 + lightOffset, 0.1, 0.9, 64, program)

    glBindTexture(GL_TEXTURE_2D, 17)
    glDrawArrays(GL_TRIANGLES, 2767818, 2767962-2767818)  # renders

    glBindTexture(GL_TEXTURE_2D, 14)
    glDrawArrays(GL_TRIANGLES, 2767962, 3361914-2767962)  # renders


def draw_wind_mill_body(program):

    # applies model matrix (angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    load_custom_transformations_parameters(
        program, 0, 0, 0, 1, 40, 0, 0, 1, 1, 1)

    load_light_parameters(0.1 + lightOffset, 0.1, 0.9, 64, program)

    glBindTexture(GL_TEXTURE_2D, 20)
    glDrawArrays(GL_TRIANGLES, 3364872, 3364974-3364872)  # renders

    glBindTexture(GL_TEXTURE_2D, 20)
    glDrawArrays(GL_TRIANGLES, 3364974, 3371022-3364974)  # renders

    glBindTexture(GL_TEXTURE_2D, 20)
    glDrawArrays(GL_TRIANGLES, 3371022, 3371154-3371022)  # renders

    glBindTexture(GL_TEXTURE_2D, 25)
    glDrawArrays(GL_TRIANGLES, 3371154, 3371922-3371154)  # renders

    glBindTexture(GL_TEXTURE_2D, 22)
    glDrawArrays(GL_TRIANGLES, 3371922, 3371970-3371922)  # renders

    glBindTexture(GL_TEXTURE_2D, 24)
    glDrawArrays(GL_TRIANGLES, 3371970, 3372390-3371970)  # renders


def draw_wind_mill_circle(program, rotacao_inc):

    # applies model matrix (angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    load_custom_transformations_parameters(program,
                                           rotacao_inc, 1, 0, 0, 30.8, 40.4, -0.5, 1, 1, 1)

    load_light_parameters(0.1 + lightOffset, 0.1, 0.9, 64, program)

    glBindTexture(GL_TEXTURE_2D, 21)
    glDrawArrays(GL_TRIANGLES, 3361914, 3363042-3361914)  # renders

    glBindTexture(GL_TEXTURE_2D, 21)
    glDrawArrays(GL_TRIANGLES, 3363042, 3364578-3363042)  # renders

    glBindTexture(GL_TEXTURE_2D, 23)
    glDrawArrays(GL_TRIANGLES, 3364578, 3364596-3364578)  # renders

    glBindTexture(GL_TEXTURE_2D, 23)
    glDrawArrays(GL_TRIANGLES, 3364596, 3364614-3364596)  # renders

    glBindTexture(GL_TEXTURE_2D, 23)
    glDrawArrays(GL_TRIANGLES, 3364614, 3364800-3364614)  # renders

    glBindTexture(GL_TEXTURE_2D, 23)
    glDrawArrays(GL_TRIANGLES, 3364800, 3364854-3364800)  # renders

    glBindTexture(GL_TEXTURE_2D, 23)
    glDrawArrays(GL_TRIANGLES, 3364854, 3364872-3364854)  # renders


def draw_sky(program):

    # applies model matrix (angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    load_default_transformations_parameters(program)

    load_light_parameters(1 + lightOffset, 1, 0.9, 500, program)

    glBindTexture(GL_TEXTURE_2D, 28)
    glDrawArrays(GL_TRIANGLES, 3372390, 3372426-3372390)  # renders


def draw_street(program):

    # applies model matrix (angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    load_default_transformations_parameters(program)

    load_light_parameters(0.1 + lightOffset, 0.1, 0.9, 64, program)

    glBindTexture(GL_TEXTURE_2D, 29)
    glDrawArrays(GL_TRIANGLES, 3372426, 3372432-3372426)  # renders


def draw_secondary_yard(program):

    # applies model matrix (angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    load_default_transformations_parameters(program)

    load_light_parameters(0.1 + lightOffset, 0.1, 0.9, 64, program)

    glBindTexture(GL_TEXTURE_2D, 0)
    glDrawArrays(GL_TRIANGLES, 3372432, 3372438-3372432)  # renders


def draw_floor(program):

    # applies model matrix (angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    load_default_transformations_parameters(program)

    load_light_parameters(0.1 + lightOffset, 0.1, 0.9, 64, program)

    glBindTexture(GL_TEXTURE_2D, 30)
    glDrawArrays(GL_TRIANGLES, 3372438, 3372522-3372438)  # renders


def draw_keyboard(program):

    # applies model matrix (angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    load_default_transformations_parameters(program)

    load_light_parameters(0.1 + lightOffset, 0.1, 0.9, 64, program)

    glBindTexture(GL_TEXTURE_2D, 31)
    glDrawArrays(GL_TRIANGLES, 3372522, 3464400-3372522)  # renders


def load_light_parameters(ka, kd, ks, ns, program):
    """Loads custom parameters for luminosity"""

    # recovers variable ka location on GPU
    loc_ka = glGetUniformLocation(program, "ka")
    glUniform1f(loc_ka, ka)  # envia ka pra gpu

    # recovers variable kd location on GPU
    loc_kd = glGetUniformLocation(program, "kd")
    glUniform1f(loc_kd, kd)  # envia kd pra gpu

    # recovers variable ks location on GPU
    loc_ks = glGetUniformLocation(program, "ks")
    glUniform1f(loc_ks, ks)  # envia ks pra gpu

    # recovers variable ns location on GPU
    loc_ns = glGetUniformLocation(program, "ns")
    glUniform1f(loc_ns, ns)  # envia ns pra gpu


def draw_moon(x, y, z, program):

    # applies model matrix (angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    load_custom_transformations_parameters(
        program, 0.0, 0.0, 1.0, 0.0, x, y - 60, z, 1, 1, 1)

    load_light_parameters(1, 1, 1, 1000.0, program)

    # recovers variable lightPos location on GPU
    loc_light_pos = glGetUniformLocation(program, "lightPos")

    # light source position
    glUniform3f(loc_light_pos, x, y - 60, z)

    # defines texture model id
    glBindTexture(GL_TEXTURE_2D, 32)
    glDrawArrays(GL_TRIANGLES, 3464400, 3467280-3464400)  # renders


def upload_data(buffer, data, program, size, name):
    # Make this buffer the default one
    glBindBuffer(GL_ARRAY_BUFFER, buffer)
    glBufferData(GL_ARRAY_BUFFER, data.nbytes, data, GL_STATIC_DRAW)

    stride = data.strides[0]
    offset = ctypes.c_void_p(0)

    loc = glGetAttribLocation(program, name)

    glEnableVertexAttribArray(loc)
    glVertexAttribPointer(loc, size, GL_FLOAT, False, stride, offset)


def send_to_gpu(vertices_list, textures_list, normals_list, program):

    # Request a buffer slot from GPU
    buffer = glGenBuffers(3)

    # First, send the vertices list
    vertices = np.zeros(len(vertices_list), [("position", np.float32, 3)])
    vertices['position'] = vertices_list
    upload_data(buffer[0], vertices, program, 3, "position")

    # Now, send the textures coordinates list
    textures = np.zeros(len(textures_list), [("position", np.float32, 2)])
    textures['position'] = textures_list
    upload_data(buffer[1], textures, program, 2, "texture_coord")

    # Now, send the normals list
    normals = np.zeros(len(normals_list), [("position", np.float32, 3)])
    normals['position'] = normals_list
    upload_data(buffer[2], normals, program, 3, "normals")

    return buffer


def show_window(window, program):

    glfw.show_window(window)
    glfw.set_cursor_pos(window, lastX, lastY)

    glEnable(GL_DEPTH_TEST)

    rotacao_inc = 0
    moon_angle = 0.1

    while not glfw.window_should_close(window):

        glfw.poll_events()

        # clear the screen color and set to black
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glClearColor(0, 0, 0, 1)

        # check if polygonal mode is on
        if polygonal_mode == True:
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        if polygonal_mode == False:
            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

        # draws objects
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

        # increases rotacao_inc to rotate the windmill circle
        rotacao_inc += 0.1

        # increases moon_angle to rotate the moon
        moon_angle += 0.3

        draw_moon(70 * np.cos(np.deg2rad(moon_angle)),
                  70, 70 * np.sin(np.deg2rad(moon_angle)), program)

        mat_view = view()
        loc_view = glGetUniformLocation(program, "view")
        glUniformMatrix4fv(loc_view, 1, GL_FALSE, mat_view)

        mat_projection = projection()
        loc_projection = glGetUniformLocation(program, "projection")
        glUniformMatrix4fv(loc_projection, 1, GL_FALSE, mat_projection)

        # updates the camera position on GPU to calcula specular reflection

        # recover viesPos variable position on GPU
        loc_view_pos = glGetUniformLocation(program, "viewPos")

        # camera position (x, y, z)
        glUniform3f(loc_view_pos, cameraPos[0], cameraPos[1], cameraPos[2])

        glfw.swap_buffers(window)

    glfw.terminate()


def load_model_from_file(filename):
    """
    Loads a Wavefront OBJ file. 
    Code by Ricardo Marcacini.
    """

    objects = {}
    vertices = []
    normals = []
    texture_coords = []
    faces = []

    material = None

    # opens .obj file to read
    for line in open(filename, "r"):
        if line.startswith('#'):
            continue  # ignore comments
        values = line.split()  # breaks line by space
        if not values:
            continue

        # recover vertices
        if values[0] == 'v':
            vertices.append(values[1:4])

        # recover normal vertices
        if values[0] == 'vn':
            normals.append(values[1:4])

        # recover textures coordinates
        elif values[0] == 'vt':
            texture_coords.append(values[1:3])

        # recover faces
        elif values[0] in ('usemtl', 'usemat'):
            material = values[1]
        elif values[0] == 'f':
            face = []
            face_texture = []
            face_normals = []
            for v in values[1:]:
                w = v.split('/')
                face.append(int(w[0]))
                face_normals.append(int(w[2]))
                if len(w) >= 2 and len(w[1]) > 0:
                    face_texture.append(int(w[1]))
                else:
                    face_texture.append(0)

            faces.append((face, face_texture, face_normals, material))

    model = {}
    model['vertices'] = vertices
    model['texture'] = texture_coords
    model['faces'] = faces
    model['normals'] = normals

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
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, img_width, img_height,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data)


def load_model_and_texture(vertices_list, normals_list, textures_coord_list, model_file, texture_files, id_offset):

    faces_visited = []
    model_name = model_file.split('/')

    # load model, its own texture and gives this texture an id
    modelo = load_model_from_file(model_file)

    if len(model_name) > 1:
        print('Processing model ' +
              model_name[1] + '. Inital vertex:', len(vertices_list))
    else:
        print('Processing model ' +
              model_name[0] + '. Inital vertex:', len(vertices_list))

    # inserts model vertices on vertices array
    for face in modelo['faces']:
        for vertice_id in face[0]:
            vertices_list.append(modelo['vertices'][vertice_id-1])
        for texture_id in face[1]:
            textures_coord_list.append(modelo['texture'][texture_id-1])
        for normal_id in face[2]:
            normals_list.append(modelo['normals'][normal_id-1])

    if len(model_name) > 1:
        print('Processing model ' +
              model_name[1] + '. Final vertex:', len(vertices_list))
    else:
        print('Processing model ' +
              model_name[0] + '. Final vertex:', len(vertices_list))

    # in case we're going to load more than one texture for the .obj.
    # we sum texture_id + id_offset because if we loaded some texture before,
    # we need to load the new textures considering the already added ones
    if len(texture_files) > 0:
        for texture_id in range(len(texture_files)):
            print(texture_id + id_offset, texture_files[texture_id])
            load_texture_from_file(
                texture_id + id_offset, texture_files[texture_id])

    return vertices_list, normals_list, textures_coord_list


def generate_models_and_textures(NUM_TEXTURES):

    glHint(GL_LINE_SMOOTH_HINT, GL_DONT_CARE)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glEnable(GL_LINE_SMOOTH)
    glEnable(GL_TEXTURE_2D)

    # Generate NUM_TEXTURES textures
    textures = glGenTextures(NUM_TEXTURES)

    normals_list = []
    vertices_list = []
    textures_coord_list = []

    ground_textures = [
        'textures/terreno/grama.jpg'
    ]

    house_textures = [
        'textures/abandonada/cottage_diffuse.png',
        'textures/abandonada/cottage_normal.png'
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
        'textures/tela/texture.png',
        'textures/tela/texture1.png',
        'textures/tela/texture2.png',
        'textures/tela/texture3.png'
    ]

    table_textures = [
        'textures/escrivaninha/texturaMesa.jpg'
    ]

    cpu_textures = [
        'textures/escrivaninha/texturaMesa.jpg'
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
        'textures/ceu/pngegg.png'
    ]

    street_textures = [
        'textures/terreno/rua.jpg',
    ]

    floor_textures = [
        'textures/terreno/piso.jpg',
    ]

    keyboard_textures = [
        'textures/keyboard/pl.jpg',
    ]

    moon_textures = [
        'textures/moon/moon.png'
    ]

    vertices_list, normals_list, textures_coord_list = load_model_and_texture(
        vertices_list, normals_list, textures_coord_list, 'textures/terreno/quintal.obj', ground_textures, 0)

    vertices_list, normals_list, textures_coord_list = load_model_and_texture(
        vertices_list, normals_list, textures_coord_list, 'textures/abandonada/cottage_obj.obj', house_textures, 1)

    vertices_list, normals_list, textures_coord_list = load_model_and_texture(
        vertices_list, normals_list, textures_coord_list, 'textures/trees/birch_tree.obj', trees_textures, 3)

    vertices_list, normals_list, textures_coord_list = load_model_and_texture(
        vertices_list, normals_list, textures_coord_list, 'textures/frog/frog.obj', frog_textures, 5)

    vertices_list, normals_list, textures_coord_list = load_model_and_texture(
        vertices_list, normals_list, textures_coord_list, 'textures/horse/horse.obj', horse_textures, 6)

    vertices_list, normals_list, textures_coord_list = load_model_and_texture(
        vertices_list, normals_list, textures_coord_list, 'textures/gaming_chair/chair.obj', chair_textures, 13)

    vertices_list, normals_list, textures_coord_list = load_model_and_texture(
        vertices_list, normals_list, textures_coord_list, 'textures/tela/tela.obj', screen_textures, 14)

    vertices_list, normals_list, textures_coord_list = load_model_and_texture(
        vertices_list, normals_list, textures_coord_list, 'textures/escrivaninha/mesa.obj', table_textures, 18)

    vertices_list, normals_list, textures_coord_list = load_model_and_texture(
        vertices_list, normals_list, textures_coord_list, 'textures/CPU/cpu.obj', cpu_textures, 19)

    vertices_list, normals_list, textures_coord_list = load_model_and_texture(
        vertices_list, normals_list, textures_coord_list, 'textures/windMill/rodaMoinho2.obj', win_mill_textures, 20)

    vertices_list, normals_list, textures_coord_list = load_model_and_texture(
        vertices_list, normals_list, textures_coord_list, 'textures/windMill/corpoMoinho1.obj', [], 20)

    vertices_list, normals_list, textures_coord_list = load_model_and_texture(
        vertices_list, normals_list, textures_coord_list, 'textures/ceu/ceu.obj', sky_textures, 28)

    vertices_list, normals_list, textures_coord_list = load_model_and_texture(
        vertices_list, normals_list, textures_coord_list, 'textures/terreno/rua.obj', street_textures, 29)

    vertices_list, normals_list, textures_coord_list = load_model_and_texture(
        vertices_list, normals_list, textures_coord_list, 'textures/terreno/quintal_lado_oposto.obj', ground_textures, 0)

    vertices_list, normals_list, textures_coord_list = load_model_and_texture(
        vertices_list, normals_list, textures_coord_list, 'textures/terreno/piso.obj', floor_textures, 30)

    vertices_list, normals_list, textures_coord_list = load_model_and_texture(
        vertices_list, normals_list, textures_coord_list, 'textures/keyboard/keyboard.obj', keyboard_textures, 31)

    vertices_list, normals_list, textures_coord_list = load_model_and_texture(
        vertices_list, normals_list, textures_coord_list, 'textures/moon/moon.obj', moon_textures, 32)

    return vertices_list, normals_list, textures_coord_list


def init():

    global largura, altura, aspect
    largura = 1600
    altura = 1200
    aspect = largura/altura

    window = start_window(largura, altura)

    vertex_code = """
        attribute vec3 position;
        attribute vec2 texture_coord;
        attribute vec3 normals;
        
       
        varying vec2 out_texture;
        varying vec3 out_fragPos;
        varying vec3 out_normal;
                
        uniform mat4 model;
        uniform mat4 view;
        uniform mat4 projection;        
        
        void main(){
            gl_Position = projection * view * model * vec4(position,1.0);
            out_texture = vec2(texture_coord);
            out_fragPos = vec3(  model * vec4(position, 1.0));
            out_normal = vec3( model *vec4(normals, 1.0));            
        }
        """

    fragment_code = """

        // parametro com a cor da(s) fonte(s) de iluminacao
        uniform vec3 lightPos; // define coordenadas de posicao da luz
        vec3 lightColor = vec3(1.0, 1.0, 1.0);
        
        // parametros da iluminacao ambiente e difusa
        uniform float ka; // coeficiente de reflexao ambiente
        uniform float kd; // coeficiente de reflexao difusa
        
        // parametros da iluminacao especular
        uniform vec3 viewPos; // define coordenadas com a posicao da camera/observador
        uniform float ks; // coeficiente de reflexao especular
        uniform float ns; // expoente de reflexao especular
        


        // parametros recebidos do vertex shader
        varying vec2 out_texture; // recebido do vertex shader
        varying vec3 out_normal; // recebido do vertex shader
        varying vec3 out_fragPos; // recebido do vertex shader
        uniform sampler2D samplerTexture;
        
        
        
        void main(){
        
            // calculando reflexao ambiente
            vec3 ambient = ka * lightColor;             
        
            // calculando reflexao difusa
            vec3 norm = normalize(out_normal); // normaliza vetores perpendiculares
            vec3 lightDir = normalize(lightPos - out_fragPos); // direcao da luz
            float diff = max(dot(norm, lightDir), 0.0); // verifica limite angular (entre 0 e 90)
            vec3 diffuse = kd * diff * lightColor; // iluminacao difusa
            
            // calculando reflexao especular
            vec3 viewDir = normalize(viewPos - out_fragPos); // direcao do observador/camera
            vec3 reflectDir = normalize(reflect(-lightDir, norm)); // direcao da reflexao
            float spec = pow(max(dot(viewDir, reflectDir), 0.0), ns);
            vec3 specular = ks * spec * lightColor;             
            
            // aplicando o modelo de iluminacao
            vec4 texture = texture2D(samplerTexture, out_texture);
            vec4 result = vec4((ambient + diffuse + specular),1.0) * texture; // aplica iluminacao
            gl_FragColor = result;

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
    vertices_list, normals_list, textures_coord_list = generate_models_and_textures(
        NUM_TEXTURES)

    buffer = send_to_gpu(
        vertices_list, textures_coord_list, normals_list, program)

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

lightOffset = 0

init()
