from lib_sudoku import Sudoku_Solver


mylist= list()
mylist2= list()

#first
mylist.append([0,0,0,0,0,0,0,0,8])
mylist.append([0,1,8,0,6,7,2,0,0])
mylist.append([0,5,0,9,0,0,0,0,0])
mylist.append([0,0,5,0,4,0,0,6,0])
mylist.append([0,6,0,3,0,0,7,4,9])
mylist.append([0,7,0,0,0,9,0,0,3])
mylist.append([0,9,0,0,2,0,0,0,0])
mylist.append([0,0,0,4,7,0,0,0,1])
mylist.append([4,0,0,0,9,5,0,2,0])

#second
mylist2.append([0,0,0,0,0,0,0,0,0])
mylist2.append([0,0,0,5,0,6,0,0,0])
mylist2.append([0,9,0,0,0,0,0,7,0])
mylist2.append([0,0,5,0,0,0,1,0,0])
mylist2.append([0,3,0,8,0,2,0,6,0])
mylist2.append([0,2,1,0,0,0,8,4,0])
mylist2.append([2,1,0,0,7,0,0,3,8])
mylist2.append([7,0,3,0,2,0,6,0,9])
mylist2.append([0,5,0,1,0,3,0,2,0])


slib = Sudoku_Solver(mylist2)

# print(mylist[4][2])

# print(slib.populate_get_all_possibilities())
slib.brain()




# http://norvig.com/sudoku.html

