import pygame

def draw(board,screen, score):
    for coordinates, value in board.items():
        if value == "Snakehead":
            head_x = coordinates[0] * 20 # 0 bo jest to od pierwszego elementu
            head_y = coordinates[1] * 20
            head_rect = pygame.Rect(head_x, head_y, 20, 20)
            pygame.draw.rect(screen, (128, 128, 128),head_rect)
        elif value is None:
            head_x = coordinates[0] * 20  # 0 bo jest to od pierwszego elementu
            head_y = coordinates[1] * 20
            head_rect = pygame.Rect(head_x, head_y, 20, 20)
            pygame.draw.rect(screen, (148, 200, 170), head_rect) # wartosci od zera do 255 red, gree, blue czyli RGB

        elif value == "Apple":
            head_x = coordinates[0] * 20  # 0 bo jest to od pierwszego elementu
            head_y = coordinates[1] * 20
            head_rect = pygame.Rect(head_x, head_y, 25, 25)
            pygame.draw.rect(screen, (255, 0, 0), head_rect) # wartosci od zera do 255 red, gree, blue czyli RGB

    font = pygame.font.Font(pygame.font.get_default_font(), 20)
    text = font.render(str(score), True, (255, 255, 0))
    screen.blit(text, dest=(10, 10))