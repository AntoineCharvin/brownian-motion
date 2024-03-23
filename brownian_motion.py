import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

# Paramètres de la simulation
np.random.seed(0)
T = 1.0  # Temps total de la simulation
N = 10000  # Nombre de pas de temps
dt = T / N  # Intervalle de temps entre les pas
num_particles = 500  # Nombre de particules
mu = np.zeros((num_particles, 3))  # Drift (moyenne) en 3D pour chaque particule
sigma = np.ones((num_particles, 3))  # Volatilité (écart type) en 3D pour chaque particule

# Générez des positions initiales aléatoires pour chaque particule
initial_positions = np.random.normal(0, 5, size=(num_particles, 3))

# Créez un tableau pour stocker les valeurs du mouvement brownien en 3D pour chaque particule
t = np.linspace(0.0, T, N + 1)
W = np.zeros((num_particles, N + 1, 3))

# Appliquez les positions initiales aux trajectoires
W[:, 0, :] = initial_positions

# Simulation du mouvement brownien pour chaque particule
for i in range(1, N + 1):
    dW = np.random.normal(loc=mu * dt, scale=sigma * np.sqrt(dt))
    W[:, i, :] = W[:, i - 1, :] + dW

# Initialisation de Pygame
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
pygame.display.set_caption('Mouvement Brownien en 3D avec Pygame')

# Angle de vue initial
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(50, (display[0] / display[1]), 0, 50.0)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()
glTranslatef(0.0, 0.0, 0)

# Fonction pour dessiner une sphère
def draw_sphere(radius, slices, stacks):
    quadric = gluNewQuadric()
    gluQuadricNormals(quadric, GLU_SMOOTH)
    gluSphere(quadric, radius, slices, stacks)
    gluDeleteQuadric(quadric)

running = True
frame = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    glRotatef(1, 3, 1, 1)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    for particle_id in range(num_particles):
        particle_position = W[particle_id, frame]
        print(particle_position)
        glPushMatrix()
        glColor3fv((0, 0, 1))
        glTranslate(*particle_position)
        draw_sphere(0.1, 20, 20)  # Dessinez les particules sous forme de sphères
        glPopMatrix()

    pygame.display.flip()
    pygame.time.wait(10)

    frame += 1

    if frame >= N:
        running = False

pygame.quit()
