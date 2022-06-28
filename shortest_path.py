import curses
from curses import wrapper
import queue
import time


maze = [
    ["#", "#", "#", "#", "#", "#", "O", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]

def print_maze(maze, stdscr, path=[]):
    GREEN = curses.color_pair(1)
    MAGENTA = curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) in path:
                stdscr.addstr(i, j * 2, "X", MAGENTA)
            else:
                stdscr.addstr(i, j * 2, value, GREEN)


def findStart(maze, start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j
    return None


def findPath(maze, stdscr):
    start, end = "O", "x"
    startPos = findStart(maze, start)

    q = queue.Queue()
    q.put((startPos, [startPos]))

    visited = set()

    while not q.empty():
        currentPos, path = q.get()
        row, col = currentPos

        stdscr.clear()
        print_maze(maze, stdscr, path)
        time.sleep(0.2)
        stdscr.refresh()

        #find neighnbors of position and start to process them
        if maze[row][col] == end:
            return path


        neighbors = findNeighbors(maze, row, col)

        #loop through neighbor list
        for neighbor in neighbors:
            if neighbor in visited:
                continue

            #set row and column to neighbor
            r, c = neighbor
            if maze[r][c] == "#":
                continue

            new_path = path + [neighbor]
            q.put((neighbor, new_path))
            visited.add(neighbor)

def findNeighbors(maze, row, col):
    neighbors = []
    #up neighbor
    if row > 0:
        neighbors.append((row - 1, col))
    #dowm neighbor
    if row + 1 < len(maze):
        neighbors.append((row + 1, col))
    #left neighbor
    if col > 0:
        neighbors.append((row, col - 1))
    #right neighbor
    if col + 1 < len(maze[0]):
        neighbors.append((row, col + 1))

    return neighbors








def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_BLACK)


    findPath(maze, stdscr)
    stdscr.getch()


wrapper(main)
