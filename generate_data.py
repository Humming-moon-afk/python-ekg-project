import random

with open("ekg_daten.csv", "w") as file:
    file.write("time,signal\n")
    for i in range(0,61):
        signal = random.randint(60, 120)
        file.write(f"{i},{signal}\n")