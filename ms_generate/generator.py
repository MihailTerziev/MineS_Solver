class FieldGenerator:
    def __init__(self, map_size: int):
        self.map_size = map_size
        self.field = [['0' for _ in range(self.map_size)] for _ in range(self.map_size)]

    def __str__(self):
        output = ""
        for row in self.field:
            output += f"{' '.join(row)}\n"
        return output

    def load_mines(self, mine_count: int):
        if mine_count < 0:
            return "Number of mines must be non-zero positive number!"

        while not mine_count == 0:
            mine_count -= 1
            try:
                bomb_x, bomb_y = eval(input("Enter coordinates of mine (x, y): "))
                self.field[bomb_x][bomb_y] = 'X'
            except IndexError:
                print("Mine must be in the field!")
                mine_count += 1

    def save_field(self, file_path: str):
        with open(file_path, 'w') as file:
            file.write(self.__str__())
