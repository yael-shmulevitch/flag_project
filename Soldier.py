
def soldier_parts(matrix):
    my_soldier=[]
    for i in range (len(matrix)):
        for j in range (len(matrix[i])):
            if matrix[i][j]=="soldier":
                my_soldier.append(j,i)
    my_soldier=sorted(my_soldier, key=lambda tup: tup[0])
    my_legs=[my_soldier[-1],my_soldier[-2]]
    my_body=my_soldier.copy()
    for i in my_legs:
        my_body.remove(i)
    return my_legs,my_body

def