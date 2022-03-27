

class HeightMap():
    height_map = None
    max_i = 0
    max_j = 0

    def lower_than_up_down(self, nb: int, i: int, j: int) -> bool:
        if i < 0 or i >= self.max_i:
            return True
        if (nb < self.height_map[i][j]):
            return True
        return False

    def lower_than_left_right(self, nb: int, i: int, j: int) -> bool:
        if j < 0 or j >= self.max_j:
            return True
        if (nb < self.height_map[i][j]):
            return True
        return False

    def is_lowest(self, nb: int, i: int, j: int) -> bool:

        if not self.lower_than_up_down(nb, i - 1, j):
            return False
        if not self.lower_than_up_down(nb, i + 1, j):
            return False
        if not self.lower_than_left_right(nb, i, j - 1):
            return False
        if not self.lower_than_left_right(nb, i, j + 1):
            return False
        return True

    def risk_sum(self) -> int:
        risk = 0
        for i, column in enumerate(self.height_map):
            for j, nb in enumerate(column):
                if self.is_lowest(nb, i, j):
                    risk += 1 + nb
        return risk


def main():

    with open("input.txt") as file:
        input = file.read().split("\n")
    mappy = HeightMap()
    mappy.height_map = [[int(x) for x in y] for y in input]
    mappy.max_i = len(mappy.height_map)
    mappy.max_j = len(mappy.height_map[0])

    print(mappy.risk_sum())
    return


if __name__ == "__main__":
    main()
