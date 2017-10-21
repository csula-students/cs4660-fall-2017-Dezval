from io import open
from operator import itemgetter


def testOpenFile():
    with open('../test/fixtures/grid-1.txt') as f:
        lines = f.readlines()
        lines.pop(0)
        str = []
        grid = []
        for i in range(len(lines) - 1):
            lines[i] = lines[i][1:-2]
            for j in range(0, len(lines)-1, 2):
                tile = lines[i][j] + lines[i][j+1]
                str.append(tile)
            grid.append(str)
            str = []

        print("Going to print grid")
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                print(grid[i][j])

        # for i in range(len(grid)):
        #         print(grid[i])

def main():
    print("MAIN!")
    testOpenFile()


if __name__ == '__main__':
    main()
