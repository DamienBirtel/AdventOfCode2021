
def diff(nb):
    result = 0
    for i in range(nb + 1):
        result += i
    return result

def main():
    with open("input.txt") as file:
        input = file.read().split(",")

    input = [int(x) for x in input]

    #input = [16,1,2,0,4,2,7,1,2,14]
    input.sort()
    length = len(input)
    mean_average = round(sum(input) / length) - 1

    total_fuel = 0
    for nb in input:
        if nb < mean_average:
            total_fuel += diff(mean_average - nb)
        else:
            total_fuel += diff(nb - mean_average)
    print(total_fuel)
    

if __name__ == "__main__":
    main()