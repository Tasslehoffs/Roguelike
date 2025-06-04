import curses

def main(stdscr):
    curses.curs_set(0)
    stdscr.keypad(True)
    max_y, max_x = stdscr.getmaxyx()
    height, width = 20, 40
    offset_y = max((max_y - height) // 2, 0)
    offset_x = max((max_x - width) // 2, 0)
    player_y, player_x = height // 2, width // 2

    while True:
        stdscr.clear()
        for y in range(height):
            for x in range(width):
                ch = '.'
                if y == 0 or y == height - 1 or x == 0 or x == width - 1:
                    ch = '#'
                if y == player_y and x == player_x:
                    ch = '@'
                stdscr.addch(offset_y + y, offset_x + x, ch)
        stdscr.refresh()

        key = stdscr.getch()
        if key in (ord('q'), 27):
            break
        elif key == curses.KEY_UP and player_y > 1:
            player_y -= 1
        elif key == curses.KEY_DOWN and player_y < height - 2:
            player_y += 1
        elif key == curses.KEY_LEFT and player_x > 1:
            player_x -= 1
        elif key == curses.KEY_RIGHT and player_x < width - 2:
            player_x += 1


if __name__ == "__main__":
    curses.wrapper(main)
