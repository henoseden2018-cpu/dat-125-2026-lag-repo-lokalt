import csv
import matplotlib.pyplot as plt

FILNAVN = "timestrafikk_sykkelmotorveien_juni_2026 (1).csv"

dato = input("Skriv inn dato (YYYY-MM-DD): ")

timer = []
sandnes = []
stavanger = []

with open(FILNAVN, encoding="UTF-8") as f:
    reader = csv.reader(f, delimiter=";")
    next(reader)  # hopp over header

    for rad in reader:
        rad_dato = rad[5]          # Dato
        rad_time = rad[6]          # Fra tidspunkt
        rad_felt = rad[8]          # Felt-navn
        rad_mengde = rad[9]        # Trafikkmengde

        # hopp over linjer uten tall
        try:
            rad_mengde = int(rad_mengde)
        except ValueError:
            continue

        if rad_dato == dato:
            # Totalt i retning Sandnes
            if rad_felt == "Totalt i retning Sandnes":
                sandnes.append(rad_mengde)
                timer.append(rad_time)

            # Totalt i retning Stavanger
            if rad_felt == "Totalt i retning Stavanger":
                stavanger.append(rad_mengde)

if len(timer) == 0:
    print("Fant ingen data for denne datoen.")
else:
    plt.plot(timer, sandnes, label="Mot Sandnes")
    plt.plot(timer, stavanger, label="Mot Stavanger")

    plt.xlabel("Tid")
    plt.ylabel("Antall passeringer")
    plt.title("Sykkeltrafikk " + dato)
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()
