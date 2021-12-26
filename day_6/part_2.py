
def main():
    with open("input.txt") as file:
        input = file.read().split(",")
    
    fish_timer = [0] * 9
    for nb in input:
        fish_timer[int(nb)] += 1

    days = 256
    for day in range(days):
        idx = day % 9
        next_idx = (day + 7) % 9
        fish_timer[next_idx] += fish_timer[idx]
    
    print(sum(fish_timer))
    return

if __name__ == "__main__":
    main()