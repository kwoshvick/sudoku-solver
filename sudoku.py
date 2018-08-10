from lib_sudoku import Sudoku_Solver


mylist= list()

mylist.append([0,0,0,0,0,0,0,0,8])
mylist.append([0,1,8,0,6,7,2,0,0])
mylist.append([0,5,0,9,0,0,0,0,0])
mylist.append([0,0,5,0,4,0,0,6,0])
mylist.append([0,6,0,3,0,0,7,4,9])
mylist.append([0,7,0,0,0,9,0,0,3])
mylist.append([0,9,0,0,2,0,0,0,0])
mylist.append([0,0,0,4,7,0,0,0,1])
mylist.append([4,0,0,0,9,5,0,2,0])

slib = Sudoku_Solver(mylist)

print(mylist[4][2])

# http://norvig.com/sudoku.html


print(slib.draw_suduko_grid())

