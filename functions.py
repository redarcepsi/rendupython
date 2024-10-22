def several_zeros():
    return [0,0,0,0,0,0,0,0,0,0]
def several_zeros_custom(nb_zeros = 10):
    liste = []
    for i in range(nb_zeros):
        liste.append(0)
    return liste
def matrix(rows, cols):
    result = []
    for i in range(rows):
        result.append([])
        for j in range(cols):
            result[i].append(0)
    return result
class Matrix():
    def __init__(self,rows,cols):
        self.__rows = rows
        self.__cols = cols
        self.__matrix = matrix(self.__rows,self.__cols)
    def get_value(self,row,col):
        return self.__matrix[row][col]
    def __eq__(self, other: object) -> bool:
        return self.__matrix == other.__matrix

def my_sort(my_list: [int])-> [int]:
   liste = my_list
   for i in range(len(liste)-1) :
        for j in range(len(liste)-1-i):
            if liste[j+1] < liste[j] :
                liste[j+1], liste[j] = liste[j], liste[j+1]
   return liste

if __name__ == '__main__':
    several_zeros()
    several_zeros_custom(5)
    matrix(2,3)
    m1 = Matrix(2,3)
    m2 = Matrix(2,3)
    m1.get_value(1,2)
    # print(m1 == m2)
    x = [3,5,7,4,1,8]
    my_sort(x)