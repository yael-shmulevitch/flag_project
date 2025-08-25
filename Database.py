import pandas as pd

my_list=[]
for i in range (9):
  my_list.append(None)


data = {
  "soldier_place": my_list,
  "grass_place": my_list,
  "mine_place": my_list
}

df = pd.DataFrame(data, index = [1, 2, 3, 4, 5 , 6 ,7 ,8, 9])