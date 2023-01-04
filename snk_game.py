import curses
import random

screen = curses.initscr()
curses.curs_set(0)

screen_height, screen_width = screen.getmaxyx()

game_window = curses.newwin(screen_height, screen_width, 0, 0)
game_window.keypad(1)
game_window.timeout(100)

snake_x = screen_width//4
snake_y = screen_height//2
snake = [
    [snake_y, snake_x],
    [snake_y, snake_x-1],
    [snake_y, snake_x-2]
]
food = [screen_height//2, screen_width//2]
game_window.addch(int(food[0]), int(food[1]), curses.ACS_PI)
key = curses.KEY_RIGHT

while True:
    next_key = game_window.getch()
    key = key if next_key == -1 else next_key
    snake_y, snake_x = snake[0]
    if key == curses.KEY_DOWN:
        snake_y += 1
    elif key == curses.KEY_UP:
        snake_y -= 1
    elif key == curses.KEY_LEFT:
        snake_x -= 1
    elif key == curses.KEY_RIGHT:
        snake_x += 1
    if snake_x == screen_width or snake_x == 0 or snake_y == screen_height or snake_y == 0:
        curses.endwin()
        quit()
    if snake[0] in snake[1:]:
        curses.endwin()
        quit()
    if snake[0] == food:
        food = None
        while food is None:
            new_food = [
                random.randint(1, screen_height-1),
                random.randint(1, screen_width-1)
            ]
            food = new_food if new_food not in snake else None
        game_window.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        game_window.addch(int(tail[0]), int(tail[1]), ' ')

    snake.insert(0, [snake_y, snake_x])
    game_window.addch(int(snake_y), int(snake_x), curses.ACS_CKBOARD)