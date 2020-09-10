import random
import time
import numpy as np
import pygame
from pygame import MOUSEBUTTONDOWN
from pygame.locals import QUIT


class Board(pygame.sprite.Sprite):
    def __init__(self, size=3, win_score=3, screen_width=400, screen_height=400,
                 screen_color=(255, 255, 255), line_color=(10, 10, 10)):
        super(Board, self).__init__()
        self.size = size
        self.win_score = win_score
        self.winner = None
        self.draw = False
        self.state = np.zeros((self.size, self.size))
        self.board_color = screen_color
        self.line_color = line_color

        # Adjusting screen
        self.screen_width = screen_width
        self.screen_heigth = screen_height
        self.cell_width = self.screen_width / self.size
        self.cell_height = self.screen_heigth / self.size
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.screen.fill(screen_color)
        self.draw_lines()

        # Handling images
        self.x_img = pygame.image.load('X.png')
        self.o_img = pygame.image.load('O.png')

        # Resizing images
        self.x_img = pygame.transform.scale(self.x_img, (int(self.cell_width * 0.8),
                                                         int(self.cell_height * 0.8)))
        self.o_img = pygame.transform.scale(self.o_img, (int(self.cell_width * 0.8),
                                                         int(self.cell_height * 0.8)))

        # Set running
        self.running = True

    def draw_lines(self):
        # For vertical lines
        for i in range(1, self.size):
            pygame.draw.line(self.screen, self.line_color, (self.cell_width * i, 0),
                             (self.cell_width * i, self.screen_heigth), 2)

        # For horizontal lines
        for i in range(1, self.size):
            pygame.draw.line(self.screen, self.line_color, (0, self.cell_height * i),
                             (self.screen_width, self.cell_height * i), 2)

    def plot_pic(self, img, posx, posy):
        self.screen.blit(img, (posx - (img.get_rect().size[0] / 2),
                               posy - (img.get_rect().size[1] / 2)))
        pygame.display.update()

    def check_win(self):
        value = self.goal_test(self.state)
        if value != 0:
            maps = {1: "Player", -1: "AI"}
            print(maps[value], "won!")
            self.winner = value
            self.running = False
        else:
            moves = self.get_possible_moves(self.state)
            if len(moves) == 0:
                print("Game draw!")
                self.draw = True
                self.running = False

    def player_move(self):
        x, y = pygame.mouse.get_pos()
        row, col = None, None
        posx, posy = None, None

        for i in range(1, self.size + 1):
            if x < self.cell_width * i:
                posx = (self.cell_width * i) - (self.cell_width / 2)
                col = i
                break

        for i in range(1, self.size + 1):
            if y < self.cell_height * i:
                posy = (self.cell_height * i) - (self.cell_height / 2)
                row = i
                break

        self.state[row - 1, col - 1] = 1
        self.plot_pic(self.x_img, posx, posy)
        self.check_win()

    def ai_move(self):
        x, y = None, None
        # (x, y), _ = self.minimax(self.state, "o")
        (x, y), _ = self.minimax_alpha_beta(self.state, "o", -np.inf, np.inf)
        # (x, y), _ = self.depth_limited_minimax(self.state, "o", 5)
        # (x, y), _ = self.depth_limited_alpha_beta(self.state, "o", 6, -np.inf, np.inf)
        print(f"---------> AI Choosed - Row: {x} and col: {y}")
        self.state[x, y] = -1
        posx = (self.cell_width * y) + (self.cell_width / 2)
        posy = (self.cell_height * x) + (self.cell_height / 2)
        self.plot_pic(self.o_img, posx, posy)
        self.check_win()

    def get_possible_moves(self, state):
        moves_list = list()
        for i in range(self.size):
            for j in range(self.size):
                if state[i][j] == 0:
                    moves_list.append((i, j))
        random.shuffle(moves_list)
        return moves_list

    def get_value(self, state, x, y):
        if x >= self.size:
            return 0
        if y < 0 or y >= self.size:
            return 0
        return state[x][y]

    def goal_test(self, state):
        for i in range(self.size):
            for j in range(self.size):
                east = south_east = south = south_west = state[i, j]
                for k in range(1, self.win_score):
                    east += self.get_value(state, i, j + k)
                    south_east += self.get_value(state, i + k, j + k)
                    south += self.get_value(state, i + k, j)
                    south_west += self.get_value(state, i + k, j - k)
                if self.win_score in [east, south_east, south, south_west]:
                    return 1
                elif -self.win_score in [east, south_east, south, south_west]:
                    return -1
        return 0

    def heuristic(self, state, player):
        """
        Heuristic function uses cosine similarity with respect to running sums
        """
        heuristic_score = 0
        for i in range(self.size):
            for j in range(self.size):
                east = south_east = south = south_west = state[i, j]
                for k in range(1, self.win_score):
                    east += self.get_value(state, i, j + k)
                    south_east += self.get_value(state, i + k, j + k)
                    south += self.get_value(state, i + k, j)
                    south_west += self.get_value(state, i + k, j - k)
                if player == 'x':
                    heuristic_score -= sum([east, south_east,
                                            south, south_west]) ** 2
                else:
                    heuristic_score += sum([east, south_east,
                                            south, south_west]) ** 2
        return heuristic_score

    def minimax(self, state, player):
        value = self.goal_test(state)

        if value != 0:
            return (-1, -1), value

        elif player == 'x':
            moves = self.get_possible_moves(state)
            if len(moves) == 0:  # No possible moves left
                return (-1, -1), 0

            current_value = -np.inf
            current_position = (-1, -1)

            for move in moves:
                state[move] = 1
                _, max_value = self.minimax(state, 'o')
                state[move] = 0
                if max_value > current_value:
                    current_value = max_value
                    current_position = move

            return current_position, current_value

        else:
            moves = self.get_possible_moves(state)
            if len(moves) == 0:  # No possible moves left
                return (-1, -1), 0

            current_value = np.inf
            current_position = (-1, -1)

            for move in moves:
                state[move] = -1
                _, min_value = self.minimax(state, 'x')
                state[move] = 0
                if min_value < current_value:
                    current_value = min_value
                    current_position = move

            return current_position, current_value

    def minimax_alpha_beta(self, state, player, alpha, beta):
        value = self.goal_test(state)

        if value != 0:
            return (-1, -1), value

        elif player == 'x':
            moves = self.get_possible_moves(state)
            if len(moves) == 0:  # No possible moves left
                return (-1, -1), 0

            current_value = -np.inf
            current_position = (-1, -1)

            for move in moves:
                state[move] = 1
                _, max_value = self.minimax_alpha_beta(
                    state, 'o', alpha, beta)
                state[move] = 0

                if max_value > current_value:
                    current_value = max_value
                    current_position = move
                if max_value < alpha:
                    alpha = max_value
                if alpha >= beta:
                    break

            return current_position, current_value

        else:
            moves = self.get_possible_moves(state)
            if len(moves) == 0:  # No possible moves left
                return (-1, -1), 0

            current_value = np.inf
            current_position = (-1, -1)

            for move in moves:
                state[move] = -1
                _, min_value = self.minimax_alpha_beta(
                    state, 'x', alpha, beta)
                state[move] = 0

                if min_value < current_value:
                    current_value = min_value
                    current_position = move
                if min_value < beta:
                    beta = min_value
                if alpha >= beta:
                    break

            return current_position, current_value

    def depth_limited_minimax(self, state, player, depth):

        if depth == 0:
            return (-1, -1), self.heuristic(state, player)
        value = self.goal_test(state)

        if value != 0:
            return (-1, -1), value
        elif player == 'x':
            moves = self.get_possible_moves(state)
            if len(moves) == 0:  # No possible moves left
                return (-1, -1), 0

            current_value = -np.inf
            current_position = (-1, -1)

            for move in moves:
                state[move] = 1
                _, max_value = self.depth_limited_minimax(
                    state, 'o', depth-1)
                state[move] = 0
                if max_value > current_value:
                    current_value = max_value
                    current_position = move

            return current_position, current_value

        else:
            moves = self.get_possible_moves(state)
            if len(moves) == 0:  # No possible moves left
                return (-1, -1), 0

            current_value = np.inf
            current_position = (-1, -1)

            for move in moves:
                state[move] = -1
                _, min_value = self.depth_limited_minimax(
                    state, 'x', depth-1)
                state[move] = 0
                if min_value < current_value:
                    current_value = min_value
                    current_position = move

            return current_position, current_value

    def depth_limited_alpha_beta(self, state, player, depth, alpha, beta):

        if depth == 0:
            return (-1, -1), self.heuristic(state, player)

        value = self.goal_test(state)

        if value != 0:
            return (-1, -1), value

        elif player == 'x':
            moves = self.get_possible_moves(state)
            if len(moves) == 0:
                return (-1, -1), 0

            current_value = -np.inf
            current_position = (-1, -1)

            for move in moves:
                state[move] = 1
                _, max_value = self.depth_limited_alpha_beta(
                    state, 'o', depth - 1, alpha, beta)
                state[move] = 0

                if max_value > current_value:
                    current_value = max_value
                    current_position = move
                if max_value > alpha:
                    alpha = max_value
                if alpha >= beta:
                    break

            return current_position, current_value

        else:
            moves = self.get_possible_moves(state)
            if len(moves) == 0:
                return (-1, -1), 0

            current_value = np.inf
            current_position = (-1, -1)

            for move in moves:
                state[move] = -1
                _, min_value = self.depth_limited_alpha_beta(
                    state, 'x', depth - 1, alpha, beta)
                state[move] = 0

                if min_value < current_value:
                    current_value = min_value
                    current_position = move
                if min_value < beta:
                    beta = min_value
                if alpha >= beta:
                    break

            return current_position, current_value


def main():
    pygame.init()
    pygame.display.set_caption("Tic Tac Toe")

    board = Board(size=3)
    print("Waiting for Player's Move")

    while board.running:
        for event in pygame.event.get():
            if event.type == QUIT:
                board.running = False

            elif event.type == MOUSEBUTTONDOWN:
                board.player_move()
                if board.winner or board.draw:
                    break

                print("Waiting for AI's move")
                board.ai_move()
                if board.winner or board.draw:
                    break

                print("Waiting for Player's Move")

        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    times = 100
    for count in range(times):
        time.sleep(3)
        main()

        print("\n\nStarting a new game - ")
