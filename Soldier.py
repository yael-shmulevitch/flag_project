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
        if event.type == K_RIGHT and state["soldier_place"][1] != 49:
            state["solidier_place"][1] += 1

        elif event.type == K_LEFT and state["soldier_place"][1] != 0:
            state["solidier_place"][1] -= 1

        elif event.type == K_DOWN and state["solidier_place"][0] != 24:
            state["solidier_place"][0] -= 1

        elif event.type == K_UP and state["solidier_place"][0] != 0:
            state["solidier_place"][0] += 1

        elif event.type == K_ESCAPE:
            state["window_open"] = False

        # if event.type == K_KP_ENTER:
        #     is_ok= False
        #     state["show"] = False
        #
        # else:
        #     state['show'] = True

keyboard((0,0))


def check(soldier_place, mine_places):
    body, legs = soldier_parts(soldier_place)
    for i in body:
        print(i)
        if i in FLAG_PLACES:
             state["is_winning"] = 1

    for j in legs:
        if j in mine_places:
            state['is_winning'] = 2






