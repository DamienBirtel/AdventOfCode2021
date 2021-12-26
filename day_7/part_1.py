def main():
    with open("input.txt") as file:
        input = file.read().split(",")

    input = [int(x) for x in input]
    input.sort()
    length = len(input)
    geometric_median = 0
    if length % 2 != 0:
        geometric_median = input[length // 2]
    else:
        geometric_median = (input[length // 2] + input[length // 2 - 1]) // 2

    fuel = 0
    for nb in input:
        if nb < geometric_median:
            fuel += geometric_median - nb
        else:
            fuel += nb - geometric_median
    
    print(fuel)

if __name__ == "__main__":
    main()