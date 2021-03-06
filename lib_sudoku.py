
class Sudoku_Solver:
    def __init__(self,sudoku_puzzle):
        self.puzzle = sudoku_puzzle
        self.possibilities = dict()
        self.po = 0

    def get_row(self,position):
        row = self.puzzle[position[0]]
        return row

    def get_column(self,position):
        column = list()
        for col_list in self.puzzle:
            column.append(col_list[position[1]])
        return column

    def get_posibilities(self,position):
        posible_values = [0,1,2,3,4,5,6,7,8,9]
        row = self.get_row(position)
        column = self.get_column(position)
        values = list(set(row).union(column))
        s = self.get_square_values(position)
        me = list(set(values).union(s))
        for value in me:
            posible_values.remove(value)

        return posible_values

    def get_square_values(self,position):
        square_values = list()
        start_value = self.get_start_bounding_values(position[0])
        end_value = self.get_start_bounding_values(position[0]) + 3
        for cell in self.puzzle[start_value:end_value]:
            values = cell[self.get_end_bounding_values(position[1])-3:self.get_end_bounding_values(position[1])]
            square_values += values
        return square_values

    def get_start_bounding_values(self,value):
        if value == 0 or value == 1 or value == 2:
            return 0
        elif value == 3 or value == 4 or value == 5:
            return 3
        elif value == 6 or value == 7 or value == 8:
            return 6

    def get_end_bounding_values(self,value):
        if value == 0 or value == 1 or value == 2:
            return 2+1
        elif value == 3 or value == 4 or value == 5:
            return 5+1
        elif value == 6 or value == 7 or value == 8:
            return 8+1

    def draw_sudoku_grid(self):
        counter = 1
        print(" ")
        for i in self.puzzle:
            print(" {} {} {}|{} {} {}|{} {} {}|".format(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]))
            if counter == 3 or counter == 6:
                print(" -----+-----+------")
            counter += 1

    def populate_get_all_possibilities(self):
        m = [0,1,2,3,4,5,6,7,8]
        for i in m:
            for b in m:
                if(self.puzzle[i][b] == 0):
                    self.possibilities[i,b] = self.get_posibilities([i,b])

        print(self.possibilities)

    def update_sudoku_puzzle(self,position,value):
        # print(type(value))
        self.puzzle[position[0]][position[1]] = value[0]
        self.draw_sudoku_grid()


    def get_v(self):
        for k,v in self.possibilities.items():
            if len(v) == 1:
                # pass
                # print(str(v))
                # p =
                self.update_sudoku_puzzle(k,v)
                self.po = 1
        # return self.po



    def brain(self):
        # print("-------",self.po)
        self.populate_get_all_possibilities()
        self.get_v()


        # while(self.po != 0):
        # print("-------", self.po)
        self.po = 0
        self.populate_get_all_possibilities()
        self.get_v()
        print("-------end", self.po)







