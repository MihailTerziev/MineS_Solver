class FieldGenerator:
    def __init__(self, map_size: int):
        self.__map_size = map_size
        self.__field = [['0' for _ in range(self.__map_size)] for _ in range(self.__map_size)]

    def __str__(self):
        output = ""
        for row in self.__field:
            output += f"{' '.join(row)}\n"
        return output.strip()

    def load_mines(self, mine_count: int):
        if mine_count <= 0:
            raise Exception("Number of mines must be non-zero positive number!")

        while not mine_count == 0:
            mine_count -= 1
            try:
                bomb_x, bomb_y = eval(input("Enter coordinates of mine (x, y): "))
                self.__field[bomb_x][bomb_y] = 'X'
            except IndexError:
                print("Mine must be in the field!")
                mine_count += 1

    def __fill(self, map_size: int, delimiter: str):
        self.__field.clear()
        for _ in range(map_size):
            row = input().split(delimiter)
            # if len(row) == map_size:
            self.__field.append(row)

    def customize(self, map_size=0, delimiter=' '):
        if not map_size == 0:
            self.__fill(map_size, delimiter)
        else:
            self.__fill(self.__map_size, delimiter)

    def resize(self, new_size):
        if new_size < self.__map_size:
            self.__field = [[x for x in row[:new_size]] for row in self.__field[:new_size]]
        elif new_size > self.__map_size:
            diff = new_size - self.__map_size
            [row.extend(['0' for _ in range(diff)]) for row in self.__field]
            [self.__field.append(['0' for _ in range(new_size)]) for _ in range(diff)]

    def save(self, path):
        with open(path, 'w') as file:
            file.write(self.__str__())
