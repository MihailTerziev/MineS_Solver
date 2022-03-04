from ms_generate.generator import FieldGenerator


class FieldSolver:
    def __init__(self):
        self.field = []

    def mine_count(self, f: FieldGenerator, x_cor: int, y_cor: int):
        counter = 0

        if not x_cor == 0 and f.field[x_cor - 1][y_cor] == 'X':
            counter += 1
        if not x_cor == f.__map_size - 1 and f.field[x_cor + 1][y_cor] == 'X':
            counter += 1
        if not y_cor == 0 and f.field[x_cor][y_cor - 1] == 'X':
            counter += 1
        if not y_cor == f.__map_size - 1 and f.field[x_cor][y_cor + 1] == 'X':
            counter += 1
        if not x_cor == 0 and not y_cor == f.__map_size - 1 and f.field[x_cor - 1][y_cor + 1] == 'X':
            counter += 1
        if not x_cor == 0 and not y_cor == 0 and f.field[x_cor - 1][y_cor - 1] == 'X':
            counter += 1
        if not x_cor == f.__map_size - 1 and not y_cor == f.__map_size - 1 and f.field[x_cor + 1][y_cor + 1] == 'X':
            counter += 1
        if not x_cor == f.__map_size - 1 and not y_cor == 0 and f.field[x_cor + 1][y_cor - 1] == 'X':
            counter += 1

        return counter

    def load_field(self, path):
        with open(path, 'r') as file:
            for line in file.readlines():
                self.field.append([x for x in line.strip()])
