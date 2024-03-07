import pygame
import math


pygame.init()

window_size = (600, 600)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Sześciokąt Foremny")


background_color = (0, 0, 0)
polygon_color = (0, 255, 0)


radius = 100


center_x, center_y = window_size[0] // 2, window_size[1] // 2


reference_vertices = [(center_x + int(radius * math.cos(2 * math.pi * i / 6)),
                       center_y + int(radius * math.sin(2 * math.pi * i / 6)))
                      for i in range(6)]


vertices = reference_vertices.copy()


running = True
display_polygon = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                vertices = reference_vertices.copy()
                display_polygon = True
            elif event.key == pygame.K_2:
                vertices = [(2 * x - center_x, 2 * y - center_y) for x, y in reference_vertices]
                angle = math.radians(45)
                vertices = [(int((x - center_x) * math.cos(angle) - (y - center_y) * math.sin(angle) + center_x),
                             int((x - center_x) * math.sin(angle) + (y - center_y) * math.cos(angle) + center_y))
                            for x, y in vertices]
                display_polygon = True
            elif event.key == pygame.K_3:
                vertices = [(x, 2 * center_y - y) for x, y in reference_vertices]
                vertices = [(x, int(2 * (y - center_y) + center_y)) for x, y in vertices]
                display_polygon = True
            elif event.key == pygame.K_4:
                shear_factor = 0.4
                vertices = [(x + shear_factor * y, y) for x, y in reference_vertices]

                min_x = min(vertices, key=lambda point: point[0])[0]
                max_x = max(vertices, key=lambda point: point[0])[0]
                shift_x = (min_x + max_x) / 2 - center_x
                vertices = [(x - shift_x, y) for x, y in vertices]

                display_polygon = True
            elif event.key == pygame.K_5:
                scale_factor_x = 2
                scale_factor_y = 1
                translation_y = -213

                vertices = [(scale_factor_x * x, scale_factor_y * y) for x, y in reference_vertices]

                vertices = [(x, y + translation_y) for x, y in vertices]

                min_x = min(vertices, key=lambda point: point[0])[0]
                max_x = max(vertices, key=lambda point: point[0])[0]
                shift_x = (min_x + max_x) / 2 - center_x
                vertices = [(x - shift_x, y) for x, y in vertices]

                display_polygon = True
            elif event.key == pygame.K_6:
                shear_factor_y = -0.4
                angle_rotation = 0

                vertices = [(x, x * shear_factor_y + y) for x, y in reference_vertices]

                angle_rad = math.radians(angle_rotation)
                vertices = [
                    (int((x - center_x) * math.cos(angle_rad) - (y - center_y) * math.sin(angle_rad) + center_x),
                     int((x - center_x) * math.sin(angle_rad) + (y - center_y) * math.cos(angle_rad) + center_y))
                    for x, y in vertices]

                min_y = min(vertices, key=lambda point: point[1])[1]
                max_y = max(vertices, key=lambda point: point[1])[1]
                shift_y = (min_y + max_y) / 2 - center_y
                vertices = [(x, y - shift_y) for x, y in vertices]

                display_polygon = True
            elif event.key == pygame.K_7:
                vertices = [(x, 2 * center_y - y) for x, y in reference_vertices]
                vertices = [(x, int(2 * (y - center_y) + center_y)) for x, y in vertices]
                display_polygon = True
            elif event.key == pygame.K_8:

                scale_factor = 0.5
                vertices = [(2 * x - center_x, 2 * y - center_y) for x, y in reference_vertices]
                angle = math.radians(77)
                vertices = [(int(scale_factor * ((x - center_x) * math.cos(angle) - (y - center_y) * math.sin(angle)) + center_x),
                             int(scale_factor * ((x - center_x) * math.sin(angle) + (y - center_y) * math.cos(angle)) + center_y + 200))
                            for x, y in vertices]
                display_polygon = True

            elif event.key==pygame.K_9:
                angle_rotation = 180
                shear_factor = 0.3
                translation_x = 195

                angle_rad = math.radians(angle_rotation)
                reference_vertices = [(x, y) for x, y in
                                      reference_vertices]

                vertices = [
                    (int((x - center_x) * math.cos(angle_rad) - (y - center_y) * math.sin(angle_rad) + center_x
                        ),
                    int((x - center_x) * math.sin(angle_rad) + (y - center_y) * math.cos(angle_rad) + center_y
                        ),
                    )
                    for x, y in reference_vertices
                ]
                vertices = [(x, x * shear_factor + y) for x, y in vertices]
                vertices = [(x + translation_x, y) for x, y in vertices]
                display_polygon = True


    window.fill(background_color)

    pygame.draw.polygon(window, polygon_color, vertices)

    pygame.display.flip()

pygame.quit()