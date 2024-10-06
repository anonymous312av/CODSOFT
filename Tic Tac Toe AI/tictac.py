import sys
import pygame
import numpy as np

pygame.init()

WHITE = (255, 255, 255)
GRAY = (180, 180, 180)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
PINK = (255, 20, 147)

WIDTH = 300
HEIGHT = 400  
LINE_WIDTH = 5
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Glow Tic Tac Toe')
screen.fill(BLACK)

board = np.zeros((BOARD_ROWS, BOARD_COLS))

you_score = 0
ai_score = 0
draw_score = 0

font = pygame.font.Font(None, 36)

def draw_neon_lines(color=WHITE):
    for i in range(BOARD_ROWS + 1):
        pygame.draw.line(screen, color, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, color, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT - 100), LINE_WIDTH)

def draw_neon_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1: 
                pygame.draw.line(screen, PINK, (col * SQUARE_SIZE + SQUARE_SIZE // 4, row * SQUARE_SIZE + SQUARE_SIZE // 4),
                                 (col * SQUARE_SIZE + SQUARE_SIZE * 3 // 4, row * SQUARE_SIZE + SQUARE_SIZE * 3 // 4), CROSS_WIDTH + 5)
                pygame.draw.line(screen, PINK, (col * SQUARE_SIZE + SQUARE_SIZE // 4, row * SQUARE_SIZE + 3 * SQUARE_SIZE // 4),
                                 (col * SQUARE_SIZE + SQUARE_SIZE * 3 // 4, row * SQUARE_SIZE + SQUARE_SIZE // 4), CROSS_WIDTH + 5)
                
                pygame.draw.line(screen, PINK, (col * SQUARE_SIZE + SQUARE_SIZE // 4, row * SQUARE_SIZE + SQUARE_SIZE // 4),
                                 (col * SQUARE_SIZE + SQUARE_SIZE * 3 // 4, row * SQUARE_SIZE + SQUARE_SIZE * 3 // 4), CROSS_WIDTH)
                pygame.draw.line(screen, PINK, (col * SQUARE_SIZE + SQUARE_SIZE // 4, row * SQUARE_SIZE + 3 * SQUARE_SIZE // 4),
                                 (col * SQUARE_SIZE + SQUARE_SIZE * 3 // 4, row * SQUARE_SIZE + SQUARE_SIZE // 4), CROSS_WIDTH)
            elif board[row][col] == 2: 
                pygame.draw.circle(screen, BLUE, (int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)),
                                   CIRCLE_RADIUS + 5, CIRCLE_WIDTH + 5
                pygame.draw.circle(screen, BLUE, (int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)),
                                   CIRCLE_RADIUS, CIRCLE_WIDTH)

def draw_neon_button():
    button_text = font.render("Restart", True, WHITE)
    button_rect = button_text.get_rect(center=(WIDTH // 2, HEIGHT - 30)) 
    pygame.draw.rect(screen, GRAY, button_rect.inflate(10, 10), border_radius=5)
    pygame.draw.rect(screen, PINK, button_rect.inflate(12, 12), border_radius=5, width=2)
    screen.blit(button_text, button_rect)
    return button_rect

def draw_neon_scores():
    you_text = font.render(f"You: {you_score}", True, WHITE)
    screen.blit(you_text, (20, HEIGHT - 80))  
    ai_text = font.render(f"AI: {ai_score}", True, WHITE)
    screen.blit(ai_text, (WIDTH - ai_text.get_width() - 20, HEIGHT - 80)) 
    draw_text = font.render(f"Draws: {draw_score}", True, WHITE)
    screen.blit(draw_text, (WIDTH // 2 - draw_text.get_width() // 2, HEIGHT - 80)) 
def mark_square(row, col, player): 
    board[row][col] = player
    
def available_square(row, col):
    return board[row][col] == 0

def is_board_full():
    return np.all(board != 0)

def check_win(player):
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def minimax(minimax_board, depth, is_maximizing):
    if check_win(2):  
        return float('inf')
    elif check_win(1):
        return float('-inf')
    elif is_board_full():
        return 0
    
    if is_maximizing:
        best_score = -1000
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if minimax_board[row][col] == 0:
                    minimax_board[row][col] = 2
                    score = minimax(minimax_board, depth + 1, False)
                    minimax_board[row][col] = 0
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = 1000
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if minimax_board[row][col] == 0:
                    minimax_board[row][col] = 1
                    score = minimax(minimax_board, depth + 1, True)
                    minimax_board[row][col] = 0
                    best_score = min(score, best_score)
        return best_score

def best_move():
    best_score = -1000
    move = (-1, -1)
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                board[row][col] = 2
                score = minimax(board, 0, False)
                board[row][col] = 0
                if score > best_score:
                    best_score = score
                    move = (row, col)
                    
    if move != (-1, -1):
        mark_square(move[0], move[1], 2)
        return True
    return False

def restart_game():
    global board, you_score, ai_score, draw_score, player, game_over, winner
    screen.fill(BLACK)
    draw_neon_lines()
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0
    player = 1
    game_over = False
    winner = 0

draw_neon_lines()

player = 1
game_over = False
winner = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_X = event.pos[0] // SQUARE_SIZE
            mouse_Y = event.pos[1] // SQUARE_SIZE
            
            if 0 <= mouse_Y < BOARD_ROWS and 0 <= mouse_X < BOARD_COLS and available_square(mouse_Y, mouse_X):
                mark_square(mouse_Y, mouse_X, player)
                if check_win(player):
                    game_over = True
                    winner = player
                    you_score += 1 
                player = player % 2 + 1

                if not game_over:
                    if best_move():
                        if check_win(2):
                            game_over = True
                            winner = 2
                            ai_score += 1  
                        player = player % 2 + 1

                if not game_over and is_board_full():
                    game_over = True
                    draw_score += 1  

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart_game()

        if event.type == pygame.MOUSEBUTTONDOWN and game_over:
            button_rect = draw_neon_button()
            if button_rect.collidepoint(event.pos):
                restart_game()

    if not game_over:
        draw_neon_figures()
    else:
        draw_neon_figures()
        if winner == 1:
            draw_neon_lines(GREEN)
        elif winner == 2:
            draw_neon_lines(RED)
        elif draw_score > 0 and not winner: 
            draw_text = font.render("Draw!", True, GRAY)
            screen.blit(draw_text, (WIDTH // 2 - draw_text.get_width() // 2, HEIGHT // 2 - 20))

    draw_neon_scores()  
    button_rect = draw_neon_button() 

    pygame.display.update()
