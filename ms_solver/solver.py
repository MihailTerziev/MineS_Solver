from ms_generate.generator import FieldGenerator


class FieldSolver:
    def count_bombs_around(self, f: FieldGenerator, x_cor: int, y_cor: int) -> int:
        counter = 0

        if not x_cor == 0 and f.field[x_cor - 1][y_cor] == '*':
            counter += 1
        if not x_cor == f.map_size - 1 and f.field[x_cor + 1][y_cor] == '*':
            counter += 1
        if not y_cor == 0 and f.field[x_cor][y_cor - 1] == '*':
            counter += 1
        if not y_cor == f.map_size - 1 and f.field[x_cor][y_cor + 1] == '*':
            counter += 1
        if not x_cor == 0 and not y_cor == size - 1 and f.field[x_cor - 1][y_cor + 1] == '*':
            counter += 1
        if not x_cor == 0 and not y_cor == 0 and f.field[x_cor - 1][y_cor - 1] == '*':
            counter += 1
        if not x_cor == size - 1 and not y_cor == size - 1 and f.field[x_cor + 1][y_cor + 1] == '*':
            counter += 1
        if not x_cor == size - 1 and not y_cor == 0 and f.field[x_cor + 1][y_cor - 1] == '*':
            counter += 1

        return counter
