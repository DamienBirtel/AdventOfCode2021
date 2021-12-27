

def is_lowest(height_map, i, j):
    return True

def main():

    with open("input.txt") as file:
        input = file.read().split("\n")
    input = "2199943210\n3987894921\n9856789892\n8767896789\n9899965678".split("\n")
    height_map = [[int(x) for x in y] for y in input]

    risk_sum = 0
    for i, column in enumerate(height_map):
        for j, nb in enumerate(column):
            if is_lowest(height_map, i, j):
                risk_sum += 1 + nb
    print(risk_sum)
    return

if __name__ == "__main__":
    main()