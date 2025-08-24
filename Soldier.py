
def body(matrix):
    my_soldier=[]
    for i in range (len(matrix)):
        for j in range (len(matrix[i])):
            if matrix[i][j]=="soldier":
                my_soldier.append(j,i)