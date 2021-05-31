#!/usr/bin/env python
# coding: utf-8

# # Trabalho 1 de Computação Gráfica
# ## Integrantes
# Bruno dos Santos, NUSP 10786170
# 
# Henrique de S. Q. dos Santos, NUSP 10819029
# 
# Witor M. A. de Oliveira, NUSP 10692190

# Importação dos módulos necessários

# In[1]:


import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np
import math


# A função abaixo recebe eventos de teclado.
# 
# As teclas "1" e "2" do teclado (E NÃO DO TECLADO NUMÉRICO) alteram o cenário de "manhã" e "sol" para "noite" e "lua".
# 
# As teclas W, A, S e D controlam o homenzinho. As setas direcionais controlam o passarinho.
# 
# Vale ressaltar que limitamos até onde você pode subir o homenzinho e o passarinho.

# In[2]:


def key_event(window, key, scancode, action, mods):
    # print('[key event] key=', key)
    # print('[key event] scancode=', scancode)
    # print('[key event] action=', action)
    # print('[key event] mods=', mods)
    # print('-------')

    global angle, t_x_man, t_y_man, e_x_man, e_y_man
    global t_x_bird, t_y_bird

    # Man
    if key == 87 and t_y_man < 0.0 :  # W
        t_y_man += 0.01
        e_x_man -= 0.015
        e_y_man -= 0.015
    if key == 65:  # A
        t_x_man -= 0.01
    if key == 83  and t_y_man > -1.0 + 0.2:  # S
        t_y_man -= 0.01
        e_x_man += 0.015
        e_y_man += 0.015
    if key == 68:  # D
        t_x_man += 0.01
    
    # Controls the bird
    if key == 265 and t_y_bird < 0.0 :  # Up arrow
        t_y_bird += 0.01
    if key == 263:  # Left arrow
        t_x_bird -= 0.01
    if key == 264  and t_y_bird > -1.0 + 0.05:  # Down arrow
        t_y_bird -= 0.01
    if key == 262:  # Right arrow
        t_x_bird += 0.01

    # Controls the scene switch between "day" and "night"
    if key == 49: # keyboard (NOT NUMPAD) number 1
        angle += 2
    if key == 50: # keyboard (NOT NUMPAD) number 2
        angle -= 2
    


# As funções abaixo representam as transformações disponíveis: escala, rotação e translação em 2D.

# In[3]:


def scale(e_x, e_y):

    return np.array([e_x, 0.0, 0.0, 0,
                     0.0, e_y, 0.0, 0,
                     0.0, 0.0, 1.0, 0.0,
                     0.0, 0.0, 0.0, 1.0], np.float32)


# In[4]:


def rotation(angle):

    rad = math.radians(angle)

    c = math.cos(rad)
    s = math.sin(rad)

    return np.array([c, -s, 0.0, 0,
                     s, c, 0.0, 0,
                     0.0, 0.0, 0, 0.0,
                     0.0, 0.0, 0.0, 1.0], np.float32)


# In[5]:


def translation(t_x, t_y):

    return np.array([1.0, 0.0, 0.0, t_x,
                    0.0, 1.0, 0.0, t_y,
                    0.0, 0.0, 1.0, 0.0,
                    0.0, 0.0, 0.0, 1.0], np.float32)


# Essa função é responsável por criar a janela onde os objetos geométricos serão mostrados.

# In[6]:


def start_window():
    glfw.init()
    glfw.window_hint(glfw.VISIBLE, glfw.FALSE)
    window = glfw.create_window(1000, 1000, "First project", None, None)
    glfw.make_context_current(window)

    # glfw.set_mouse_button_callback(window, mouse_event)  # gets mouse inputs
    glfw.set_key_callback(window, key_event)  # gets keyboard inputs

    return window


# Função responsável por definir e compilar os slots (vertex e fragment) dos shaders

# In[7]:


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

    return program, slot, slot_code


# A função abaixo cria o vertor de vértices contendo todos os objetos que serão mostrados na janela.

# In[8]:


def draw_object():

    vertices_list = [
        # house
            # smaller roof
            (-0.8, -0.5),  # vertice 0
            (-0.6, -0.3),  # vertice 1
            (-0.4, -0.5),  # vertice 2

            # bigger roof
            (-0.9, -0.5),  # vertice 0 #3
            (-0.6, -0.2),  # vertice 1
            (-0.3, -0.5),  # vertice 2

            # house base
            (-0.8, -0.5),  # vertice 0 #6
            (-0.8, -0.9),  # vertice 3
            (-0.4, -0.5),  # vertice 1
            (-0.4, -0.9),  # vertice 2

            # house door
            (-0.6, -0.7),  # vertice 0 #10
            (-0.6, -0.9),  # vertice 3
            (-0.5, -0.7),  # vertice 1
            (-0.5, -0.9),  # vertice 2

        # sun
            # normal square
            (0.1, 0.6),  # vertice 0 #14
            (0.1, 0.4),  # vertice 1
            (-0.1, 0.6),  # vertice 3
            (-0.1, 0.4),  # vertice 2

            # diagonal square
            (0.0, 0.64),  # vertice 1
            (0.14, 0.5),  # vertice 2
            (-0.14, 0.5),  # vertice 0 #18
            (0.0, 0.36),  # vertice 3

        # bird
            # wing
            (-0.5, 0.0),  # vertice 0 #22
            (-0.53, 0.04),  # vertice 1
            (-0.52, 0.0),  # vertice 2

            # tail
            (-0.54, 0.0),  # vertice 0 #25
            (-0.55, 0.01),  # vertice 1
            
            (-0.54, 0.0),  # vertice 2
            (-0.54, 0.0),  # vertice 3
            
            (-0.54, 0.0),  # vertice 4
            (-0.55, -0.01),  # vertice 5

            # bird beak
            (-0.47, 0.025),  # vertice 0 #31
            (-0.47, -0.025),  # vertice 1
            (-0.45, 0.0),  # vertice 2
            
        # man
            # torso
            (0.01, -0.025),  # vertice 0 #34
            (0.01, 0.01),  # vertice 1
            (-0.01, -0.025),  # vertice 2
            (-0.01, 0.01),  # vertice 3

            # legs
            (0.01, -0.025),  # vertice 0 #38
            (-0.01, -0.025),  # vertice 1
            (0.01, -0.05),  # vertice 2
            (-0.01, -0.05),  # vertice 3

            (0.0, -0.025),  # vertice 6

            # right arm
            (-0.01, 0.01),  # vertice 0 #43
            (-0.01, -0.025),  # vertice 3
            (-0.015, 0.0),  # vertice 1
            (-0.015, -0.01),  # vertice 2

            # left arm
            (0.01, 0.01),  # vertice 0 #47
            (0.01, -0.025),  # vertice 3
            (0.015, 0.0),  # vertice 1
            (0.015, -0.01),  # vertice 2

            # hat
            (0.01, 0.02),  # vertice 0 #51
            (-0.01, 0.02),  # vertice 1
            (0.0, 0.04),  # vertice 2
            (0.01, 0.035),  # vertice 3
            (0.002, 0.036),  # vertice 4
            (0.01, 0.02),  # vertice 5

        # tree
            # trunk tree
            (0.8, -0.5),  # vertice 1 #57
            (0.8, -0.8),  # vertice 0 
            (0.6, -0.5),  # vertice 2
            (0.6, -0.8),  # vertice 3

            # tree top
            (0.45, -0.5),  # vertice 1 #61
            (0.7, 0.0),  # vertice 2
            (0.945, -0.5),  # vertice 3

            # birds house
                # rectangle
                (0.63, -0.35),  # vertice 1
                (0.63, -0.22),  # vertice 0 #64
                (0.77, -0.35),  # vertice 2
                (0.77, -0.22),  # vertice 3

                # roof
                (0.61, -0.22),  # vertice 0 #68
                (0.7, -0.15),  # vertice 1
                (0.79, -0.22),  # vertice 2
        
        # field
        (-1.0, 0.0), #71
        (-1.0, -1.0),
        (1.0, 0.0),
        (1.0, -1.0),

        # sky
        (-1.0, 0.0), #75
        (-1.0, 1.0),
        (1.0, 0.0),
        (1.0, 1.0)
    ]

    pi = 3.14
    counter = 0
    radius = 0.04
    angle = 1.0
    num_vertices = 64  # define the "quality" of the circle

    # bird's body
    for counter in range(num_vertices): #79
        angle += 2*pi/num_vertices
        x = math.cos(angle) * 0.04
        y = math.sin(angle) * 0.04
        vertices_list.append((x - 0.5, y))

    # bird's eye
    for counter in range(num_vertices): #143
        angle += 2*pi/num_vertices
        x = math.cos(angle) * 0.004
        y = math.sin(angle) * 0.004
        vertices_list.append((x - 0.485,y + 0.015))

    # bird's house entrance
    for counter in range(num_vertices): #207
        angle += 2*pi/num_vertices
        x = math.cos(angle) * 0.0546
        y = math.sin(angle) * 0.0546
        vertices_list.append((x + 0.7,y - 0.28))

    # bird's house entrance 2
    for counter in range(num_vertices): #271
        angle += 2*pi/num_vertices
        x = math.cos(angle) * 0.05
        y = math.sin(angle) * 0.05
        vertices_list.append((x + 0.7,y - 0.28))

    # man head
    for counter in range(num_vertices): #335
        angle += 2*pi/num_vertices
        x = math.cos(angle) * 0.01
        y = math.sin(angle) * 0.01
        vertices_list.append((x , y + 0.02))

    # first cloud
    for counter in range(num_vertices): #399
        angle += 2*pi/num_vertices
        x = math.cos(angle) * 0.084
        y = math.sin(angle) * 0.084
        vertices_list.append((x - 0.5, y + 0.8))

    for counter in range(num_vertices): #463
        angle += 2*pi/num_vertices
        x = math.cos(angle) * 0.094
        y = math.sin(angle) * 0.094
        vertices_list.append((x - 0.4 , y + 0.8))

    for counter in range(num_vertices): #527
        angle += 2*pi/num_vertices
        x = math.cos(angle) * 0.084
        y = math.sin(angle) * 0.084
        vertices_list.append((x - 0.3, y + 0.8))

    # second cloud
    for counter in range(num_vertices): #591
        angle += 2*pi/num_vertices
        x = math.cos(angle) * 0.084
        y = math.sin(angle) * 0.084
        vertices_list.append((x + 0.3, y + 0.8))

    for counter in range(num_vertices): #655
        angle += 2*pi/num_vertices
        x = math.cos(angle) * 0.09
        y = math.sin(angle) * 0.09
        vertices_list.append((x + 0.4 , y + 0.8))

    for counter in range(num_vertices): #719
        angle += 2*pi/num_vertices
        x = math.cos(angle) * 0.096
        y = math.sin(angle) * 0.096
        vertices_list.append((x + 0.5, y + 0.8))

    # moon
    for counter in range(num_vertices): #783
        angle += 2*pi/num_vertices
        x = math.cos(angle) * 0.1
        y = math.sin(angle) * 0.1
        vertices_list.append((x, y - 0.8))
    
    total_vertices = len(vertices_list)
    vertices = np.zeros(total_vertices, [("position", np.float32, 2)])
    vertices['position'] = np.array(vertices_list)

    return vertices


# Essa função envia o vetor de pontos pra GPU. 

# In[9]:


def send_to_gpu(vertices):

    # Request a buffer slot from GPU
    buffer = glGenBuffers(1)

    # Make this buffer the default one
    glBindBuffer(GL_ARRAY_BUFFER, buffer)

    # Upload data
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_DYNAMIC_DRAW)
    glBindBuffer(GL_ARRAY_BUFFER, buffer)

    return buffer


# Função responsável por fazer as nuvens se movimentarem na janela.

# In[10]:


def cloud_movement():
    global t_x_clouds, increase        

    # if the cloud touchs the screen right edge, 
    # starts to move backward
    if t_x_clouds >= 0.4: increase = False
    
    # if the cloud touchs the screen left edge, 
    # starts to move forward
    if t_x_clouds <= -0.4: increase = True
        
    if increase: t_x_clouds = t_x_clouds + 0.0001  # to move the cloud forward
    else: t_x_clouds = t_x_clouds - 0.0001         # to move the cloud backward


# Função responsável por fazer a "asa" do passarinho se movimentar. Fazemos isso modificando apenas 1 ponto, de forma a fazer o triângulo (que serve de asa) ficar de "cabeça pra baixo". Como estamos alterando o vetor de vértices após já o termos enviado para a GPU, precisamos atualizá-lo e, por isso, fazemos o glBufferData e o glBindBuffer.

# In[11]:


def bird_wings_swing(vertices,buffer):
    
    global wings
    
    if wings is True:
        vertices["position"][23] = (-0.53, vertices["position"][23][1] + 0.08)
        wings = False
    else:
        vertices["position"][23] = (-0.53, vertices["position"][23][1] - 0.08)
        wings = True
    
    # Update the vertices on GPU
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_DYNAMIC_DRAW)
    glBindBuffer(GL_ARRAY_BUFFER, buffer)


# Função que controla o laço principal da janela a ser exibida. É aqui que plotamos todos os pontos e os colorimos para criar o cenário.

# In[12]:


def show_window(window, program, loc, loc_color, vertices,buffer):
    
    R = 1.0
    G = 0.0
    B = 0.0

    glfw.show_window(window)

    while not glfw.window_should_close(window):

        global angle
        
        glfw.poll_events()

        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(1.0, 1.0, 1.0, 1.0)
        
        #########################
        ########## SKY ##########
        #########################
         
        # Transformation matrix
        mat_tranformation = scale(1,1)

        loc = glGetUniformLocation(program, "mat_transformation")
        glUniformMatrix4fv(loc, 1, GL_TRUE, mat_tranformation)
        
        # Checks if sun is between the 3rd and 4th quadrants or not
        # If so, we change the sky color to night 
        # (because the moon will be showing on)
        if int(angle) % 360 > 90 and int(angle) % 360 < 270:
            glUniform4f(loc_color, 0, 0.062, 0.478, 1.0)
        else:
            glUniform4f(loc_color, 0.098, 0.611, 0.921, 1.0)
        
        # Drawing
        glDrawArrays(GL_TRIANGLE_STRIP, 75, 4)
        
        #########################
        ########## MOON #########
        #########################

        # Transformation matrix
        mat_rotation_sol = rotation(angle)

        loc = glGetUniformLocation(program, "mat_transformation")
        glUniformMatrix4fv(loc, 1, GL_TRUE, mat_rotation_sol)

        # Drawing
        glUniform4f(loc_color,0.709, 0.717, 0.768, 1.0)
        glDrawArrays(GL_TRIANGLE_FAN, 783, 64)

        #########################
        ########## SUN ##########
        #########################

        # Transformation matrix
        mat_rotation_sol = rotation(angle)

        loc = glGetUniformLocation(program, "mat_transformation")
        glUniformMatrix4fv(loc, 1, GL_TRUE, mat_rotation_sol)

        # Drawing
        glUniform4f(loc_color, 0.960, 0.894, 0, 1.0) # first square
        glDrawArrays(GL_TRIANGLE_STRIP, 14, 4)
        
        glUniform4f(loc_color, 0.960, 0.894, 0, 1.0) # second square
        glDrawArrays(GL_TRIANGLE_STRIP, 18, 4)
        
        #########################
        ######### FIELD #########
        #########################

        # Transformation matrix
        mat_tranformation = scale(1,1)

        loc = glGetUniformLocation(program, "mat_transformation")
        glUniformMatrix4fv(loc, 1, GL_TRUE, mat_tranformation)

        # Drawing
        glUniform4f(loc_color, 0.368, 0.662, 0.356, 1.0)
        glDrawArrays(GL_TRIANGLE_STRIP, 71, 4)
        
        #########################
        ######### HOUSE #########
        #########################

        glUniform4f(loc_color, 0.858, 0.454, 0.101, 1.0) # bigger roof
        glDrawArrays(GL_TRIANGLES, 3, 3)

        glUniform4f(loc_color, 0.101, 0.207, 0.858, 1.0) # smaller roof
        glDrawArrays(GL_TRIANGLES, 0, 3)

        glUniform4f(loc_color, 0.101, 0.207, 0.858, 1.0) # base
        glDrawArrays(GL_TRIANGLE_STRIP, 6, 4)

        glUniform4f(loc_color, 0.721, 0.321, 0.196, 1.0) # door
        glDrawArrays(GL_TRIANGLE_STRIP, 10, 4)

        #########################
        ######### TREE ##########
        #########################
        
        glUniform4f(loc_color, 0.721, 0.321, 0.196, 1.0) # trunk
        glDrawArrays(GL_TRIANGLE_STRIP, 57, 4)

        glUniform4f(loc_color, 0.129, 0.270, 0.156, 1.0) # top
        glDrawArrays(GL_TRIANGLE_STRIP, 61, 3)

        #########################
        ###### BIRD HOUSE #######
        #########################

        glUniform4f(loc_color,  0.721, 0.321, 0.196, 1.0) # rectangle
        glDrawArrays(GL_TRIANGLE_STRIP, 64, 4)

        glUniform4f(loc_color, 0.0, 0.0, 0.0, 1.0) # roof
        glDrawArrays(GL_TRIANGLE_STRIP, 68, 3)

        glUniform4f(loc_color, 0.2, 0.2, 0.2, 1.0) # house's entrance
        glDrawArrays(GL_TRIANGLE_FAN, 207, 64)

        glUniform4f(loc_color, 0.0, 0.0, 0.0, 1.0) # house's entrance 2
        glDrawArrays(GL_TRIANGLE_FAN, 271, 64)

        #########################
        ######### MAN ###########
        #########################

        # Translation and Scale matrices
        man_translation_mat = translation(t_x_man, t_y_man)
        man_scale_mat = scale(e_x_man, e_y_man)

        mtm = man_translation_mat.reshape((4,4))
        msm = man_scale_mat.reshape((4,4))

        man_transformation_mat = np.matmul(mtm, msm).reshape((1,16))

        loc = glGetUniformLocation(program, "mat_transformation")
        glUniformMatrix4fv(loc, 1, GL_TRUE, man_transformation_mat)

        # Drawing
        glUniform4f(loc_color, 0.0, 0.0, 1.0, 1.0) # head
        glDrawArrays(GL_TRIANGLE_FAN, 335, 64)

        glUniform4f(loc_color, 0.960, 0.894, 0, 1.0) # torso
        glDrawArrays(GL_TRIANGLE_STRIP, 34, 4)

        glUniform4f(loc_color, 0.0, 0.894, 0.5, 1.0) # legs
        glDrawArrays(GL_TRIANGLE_STRIP, 38, 4)

        glUniform4f(loc_color, 0.0, 1.0, 0.0, 1.0) # right arm
        glDrawArrays(GL_TRIANGLE_STRIP, 43, 4)
        
        glUniform4f(loc_color, 0.0, 1.0, 0.0, 1.0) # left arm
        glDrawArrays(GL_TRIANGLE_STRIP, 47, 4)
        
        #########################
        ######### BIRD ##########
        #########################

        # Translation matrix
        bird_translation_mat = translation(t_x_bird, t_y_bird)

        loc = glGetUniformLocation(program, "mat_transformation")
        glUniformMatrix4fv(loc, 1, GL_TRUE, bird_translation_mat)

        # Drawing
        glUniform4f(loc_color, 0.960, 0.894, 0, 1.0) # body
        glDrawArrays(GL_TRIANGLE_FAN, 79, 64)
        
        glUniform4f(loc_color, 0.0, 0.0, 0.0, 1.0) # eye
        glDrawArrays(GL_TRIANGLE_FAN, 143, 64)

        bird_wings_swing(vertices,buffer)
        
        glUniform4f(loc_color, 0.858, 0.796, 0, 1.0) # wing
        glDrawArrays(GL_TRIANGLE_STRIP, 22, 4)

        glUniform4f(loc_color, 0.921, 0.603, 0.098, 1.0) # beak
        glDrawArrays(GL_TRIANGLES, 31, 3)

        glUniform4f(loc_color, 0.960, 0.894, 0, 1.0) # tail 1
        glDrawArrays(GL_LINE_STRIP, 25, 2)

        glUniform4f(loc_color, 0.960, 0.894, 0, 1.0) # tail 2
        glDrawArrays(GL_LINE_STRIP, 27, 2)
        
        glUniform4f(loc_color, 0.960, 0.894, 0, 1.0) # tail 3
        glDrawArrays(GL_LINE_STRIP, 29, 2)

        #########################
        ######## CLOUDS #########
        #########################

        cloud_movement()

        # Translation matrix
        clouds_translation_mat = translation(t_x_clouds, t_y_clouds)

        loc = glGetUniformLocation(program, "mat_transformation")
        glUniformMatrix4fv(loc, 1, GL_TRUE, clouds_translation_mat)

        # Changes clouds color according to the angle position
        # (if the angle is between the 3rd and 4th quadrants)
        if int(angle) % 360 > 90 and int(angle) % 360 < 270:
            glUniform4f(loc_color,0.529, 0.537, 0.592, 1.0)
        else:
            glUniform4f(loc_color, 1, 1, 1, 1.0)

        # first cloud
        glDrawArrays(GL_TRIANGLE_FAN, 399, 64)
        glDrawArrays(GL_TRIANGLE_FAN, 463, 64)
        glDrawArrays(GL_TRIANGLE_FAN, 527, 64)

        # second cloud
        glDrawArrays(GL_TRIANGLE_FAN, 591, 64)
        glDrawArrays(GL_TRIANGLE_FAN, 655, 64)
        glDrawArrays(GL_TRIANGLE_FAN, 719, 64)


        glfw.swap_buffers(window)

    glfw.terminate()


# Função principal do código. Ela é responsável por preparar a GPU e o OpenGL para a exibição da janela e dos objetos geométricos.

# In[13]:


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

    show_window(window, program, loc, loc_color, vertices, buffer)


# Ambiente global do código. Utilizamos principalmente para definir as variáveis utilizadas nas funções de transformação.

# In[14]:


# x-translation and y-translation for clouds
t_x_clouds = 0
t_y_clouds = 0

increase = True # controls the cloud movement

# x-translation and y-translation for the bird
t_x_bird = 0
t_y_bird = 0

# x-translation, y-translation, x-scale and y-scale for the man
t_x_man = 0
t_y_man = 0
e_x_man = 1
e_y_man = 1

angle = 0 # controls rotation angle to switch between "day" and "night" scenes

wings = False # controls the bird wings swing

init()

