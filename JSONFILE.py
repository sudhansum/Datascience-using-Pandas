import csv
import json
import matplotlib.pyplot as plt

with open("medical.json") as fr:
    data = json.load(fr)
    men =[]
    women =[]
    for i in data["medical"]["men"]:
        men.append(i["level"])
    print(men)
    for i in data ["medical"]["women"]:
        women.append(i["level"])
    print(women)
plt.hist([men,women],bins=[80,125,150,180,195],rwidth=0.85,color=["green","orange"],label=['men','women'])
plt.legend()
plt.title("Blood Sugar Chart")
plt.xlabel("sugar level")
plt.ylabel("no of persons")
plt.show() 