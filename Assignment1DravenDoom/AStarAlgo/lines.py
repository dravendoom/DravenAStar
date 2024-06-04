import pygame

def draw_custom_line(screen, tuple1, tuple2):
    color = (45, 45, 45)
    tuple1 = (tuple1[0]*10+5, tuple1[1]*10+5)
    tuple2 = (tuple2[0]*10+5, tuple2[1]*10+5)
    pygame.draw.line(screen, color, tuple1, tuple2, 5)

def draw_line_list(screen):
    draw_custom_line(screen, (6, 17), (6, 24))
    draw_custom_line(screen, (6, 24), (23, 24))
    draw_custom_line(screen, (23, 24), (23, 17))
    draw_custom_line(screen, (6, 17), (23, 17))
    draw_custom_line(screen, (6, 13), (11, 14))
    draw_custom_line(screen, (11, 14), (13, 8))
    draw_custom_line(screen, (13, 8), (10, 4))
    draw_custom_line(screen, (10, 4), (4, 8))
    draw_custom_line(screen, (4, 8), (6, 13))
    draw_custom_line(screen, (14, 14), (20, 14))
    draw_custom_line(screen, (20, 14), (17, 7))
    draw_custom_line(screen, (17, 7), (14, 14))
    draw_custom_line(screen, (20, 9), (27, 5))
    draw_custom_line(screen, (20, 9), (21, 3))
    draw_custom_line(screen, (21, 3), (25, 2))
    draw_custom_line(screen, (25, 2), (27, 5))
    draw_custom_line(screen, (24, 12), (27, 19))
    draw_custom_line(screen, (31, 16), (24, 12))
    draw_custom_line(screen, (27, 19), (31, 16))
    draw_custom_line(screen, (30, 12), (36, 12))
    draw_custom_line(screen, (36, 12), (36, 2))
    draw_custom_line(screen, (36, 2), (30, 2))
    draw_custom_line(screen, (30, 2), (30, 12))
    draw_custom_line(screen, (35, 16), (33, 18))
    draw_custom_line(screen, (33, 18), (33, 22))
    draw_custom_line(screen, (33, 22), (35, 24))
    draw_custom_line(screen, (35, 24), (41, 24))
    draw_custom_line(screen, (41, 24), (43, 22))
    draw_custom_line(screen, (43, 22), (43, 18))
    draw_custom_line(screen, (43, 18), (41, 16))
    draw_custom_line(screen, (41, 16), (35, 16))
    draw_custom_line(screen, (33, 22), (35, 24))
    draw_custom_line(screen, (44, 14), (39, 5))
    draw_custom_line(screen, (39, 5), (42, 3))
    draw_custom_line(screen, (42, 3), (45, 5))
    draw_custom_line(screen, (45, 5), (44, 14))









