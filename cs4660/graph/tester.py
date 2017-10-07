from io import open
from operator import itemgetter


def testOpenFile():
    with open('../test/fixtures/graph-1.txt') as f:
        line1 = f.readlines()
        x = int(line1[0])
        print(x+1)
        line1.pop(0)
        print(line1)
        for i in line1:
            i = i.split(":")
            i[2] = i[2].split("\n")[0]
            print(i[0])
        # line1 = int(line1) + 4
        # print(line1)
        # # for line in f:
        #     print(line)


def main():
    print("MAIN!")
    testOpenFile()


if __name__ == '__main__':
    main()
