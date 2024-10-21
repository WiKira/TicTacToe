
class Table():

    def __init__(self):
        self.table = self.generate_table()


    def generate_table(self):
        table_dict = {
            (0, 0): 0,
            (0, 1): 0,
            (0, 2): 0,
            (1, 0): 0,
            (1, 1): 0,
            (1, 2): 0,
            (2, 0): 0,
            (2, 1): 0,
            (2, 2): 0
        }
        return table_dict



    def print_table(self):

        for r in range(0,3):
            row = ""
            for c in range(0,3):
                value = "  "

                if self.table.get((r, c)) == -1:
                    value = "O"
                elif self.table.get((r, c)) == 1:
                    value = " X "
                row = row + f" {value} "
                if c == 2:
                    continue
                row = row + "|"
            print(row)
            if r == 2:
                continue
            print("--------------")

    def verify_winner(self, x, y):
        result = 0

        for c in range(0, 3):
            result = result + self.table.get((x, c))

        if result == 3 or result == -3:
            return True

        result = 0

        for r in range(0, 3):
            result = result + self.table.get((r, y))

        if result == 3 or result == -3:
            return True

        result = 0
        if (x, y) == (0, 0) or (x, y) == (1, 1) or (x, y) == (2, 2):
            result = self.table.get((0, 0)) + self.table.get((1, 1)) + self.table.get((2, 2))

        if result == 3 or result == -3:
            return True

        result = 0
        if (x, y) == (0, 2) or (x, y) == (1, 1) or (x, y) == (2, 0):
            result = self.table.get((0, 2)) + self.table.get((1, 1)) + self.table.get((2, 0))

        if result == 3 or result == -3:
            return True

        return False


    def update_position(self, x, y, value):
        if (x, y) not in self.table.keys():
            return False, "Posição Inexistente. Tente novamente."

        if self.table.get((x, y)) == 0:
            self.table[(x, y)] = value
            return True, ""
        else:
            return False, "Posição já ocupada, tente novamente."