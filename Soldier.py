#קבל ROW, COL
def soldier_parts(soldier_place):
    my_legs=[(soldier_place[0]+3,soldier_place[1]),(soldier_place[0]+3,soldier_place[1]+1)]

    my_body=[(soldier_place[0],soldier_place[1]),
             (soldier_place[0],soldier_place[1]+1),
             (soldier_place[0]+1, soldier_place[1]),
             (soldier_place[0]+2, soldier_place[1]),
             (soldier_place[0]+2, soldier_place[1] + 1),
             (soldier_place[0] + 1, soldier_place[1]+1)

             ]
    return my_body,my_legs

def check(soldier_place):
    body,legs= soldier_parts(soldier_place)
    for i in body:
        if i in flag_places:
            state["is_winning"]=1
