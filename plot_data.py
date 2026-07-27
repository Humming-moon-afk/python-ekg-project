import matplotlib.pyplot as plt

with open("ekg_daten.csv", "r") as file:
    times = []
    signals = []
    line = file.readline()
    for line in file:
        lineContent = line.split(",")
        timeContent = int(lineContent[0])
        signalContent = int(lineContent[1])
        times.append(timeContent)
        signals.append(signalContent)



plt.plot(times,signals,color="red")
plt.title("EKG Signalverlauf")
plt.xlabel("Zeit in (s)")
plt.ylabel("Herzfrequenz (bpm)")
plt.grid(True)
plt.show()