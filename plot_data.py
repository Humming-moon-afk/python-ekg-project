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


    summe = sum(signals)
    maximum= max(signals)
    minimum = min(signals)
    anzahl = len(signals)
    durchschnitt = (summe / anzahl)
    durchschnitt = round(durchschnitt, 2)

print(f"Maximaler Wert: {maximum} (bpm)\n")
print(f"Minimaler Wert: {minimum} (bpm)\n")
print(f"Durchschnittlicher Wert: {durchschnitt} (bpm)")

plt.plot(times,signals,color="red")
plt.title("EKG Signalverlauf")
plt.xlabel("Zeit in (s)")
plt.ylabel("Herzfrequenz (bpm)")
plt.grid(True)
plt.show()