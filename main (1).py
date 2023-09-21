import pygame
import sys
import math

# Inicialização do Pygame
pygame.init()

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Configurações da tela
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Desenhe Formas")

# Lista para armazenar as formas
shapes = []

# Variáveis para desenhar
drawing = False
shape = "square"  # Começa desenhando quadrados
start_pos = None
end_pos = None

# Função para desenhar uma forma na tela
def draw_shape(surface, shape_info):
    shape_type, color, rect = shape_info
    if shape_type == "rectangle":
        pygame.draw.rect(surface, color, rect)
    elif shape_type == "square":
        pygame.draw.rect(surface, color, rect)
    elif shape_type == "circle":
        pygame.draw.circle(surface, color, rect[0], rect[1])

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                shape = "rectangle"
            elif event.key == pygame.K_q:
                shape = "square"
            elif event.key == pygame.K_c:
                shape = "circle"
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not drawing:
                drawing = True
                start_pos = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP:
            if drawing:
                drawing = False
                end_pos = pygame.mouse.get_pos()
                if shape == "rectangle":
                    shapes.append(("rectangle", BLACK, (start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))))
                elif shape == "square":
                    size = max(end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])
                    shapes.append(("square", BLACK, (start_pos, (size, size))))
                elif shape == "circle":
                    radius = int(math.hypot(end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
                    shapes.append(("circle", BLACK, (start_pos, radius)))

    screen.fill(WHITE)
   
    for shape_info in shapes:
        draw_shape(screen, shape_info)

    if drawing:
        if shape == "rectangle":
            pygame.draw.rect(screen, BLACK, (start_pos, (pygame.mouse.get_pos()[0] - start_pos[0], pygame.mouse.get_pos()[1] - start_pos[1])))
        elif shape == "square":
            size = max(pygame.mouse.get_pos()[0] - start_pos[0], pygame.mouse.get_pos()[1] - start_pos[1])
            pygame.draw.rect(screen, BLACK, (start_pos, (size, size)))
        elif shape == "circle":
            radius = int(math.hypot(pygame.mouse.get_pos()[0] - start_pos[0], pygame.mouse.get_pos()[1] - start_pos[1]))
            pygame.draw.circle(screen, BLACK, start_pos, radius)

    pygame.display.flip()

# Encerrando o Pygame
pygame.quit()
sys.exit()

fiz juntamente de alguns colegas tendo em vista que faltei alguns dias letivos correspondente as aulas do senhor, professor Ricart