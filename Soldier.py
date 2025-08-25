from pygame import *
from consts import *
from main import *


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


def keyboard(state):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_RIGHT and state["soldier_place"][1] != 47:
                print("Hi")
                x=state["soldier_place"][0]
                y=state["soldier_place"][1]+1
                state["soldier_place"]= (x,y)

            elif event.key == K_LEFT and state["soldier_place"][1] != 0:
                x=state["soldier_place"][0]
                y=state["soldier_place"][1] -1
                state["soldier_place"] = (x,y)

            elif event.key == K_DOWN and state["soldier_place"][0] != 21:
                x=state["soldier_place"][0]+1
                y=state["soldier_place"][1]
                state["soldier_place"]=(x,y)

            elif event.key == K_UP and state["soldier_place"][0] != 0:
                x=state["soldier_place"][0]-1
                y=state["soldier_place"][1]
                state["soldier_place"]= (x,y)

            elif event.key == K_KP_ENTER:
                state["show"] = True
                print("hi")

            else:
                state['show'] = False



def check(soldier_place, mine_places):
    body, legs = soldier_parts(soldier_place)
    for i in body:
        if i in FLAG_PLACES:
             state["is_winning"] = 1

    for j in legs:
        if j in mine_places:
            state['is_winning'] = 2






