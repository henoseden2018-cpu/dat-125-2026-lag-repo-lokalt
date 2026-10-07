def main():
    inputfil = "responstider_ms"
    loggfil = "logg.txt"
    rapportfil = "rapport.txt"

    gyldige = []
    ignorert = 0
    feil = 0

    try:
        with open(inputfil, "r") as f, open(loggfil, "w") as logg:
            linjenr = 0

            for linje in f:
                linjenr += 1
                original = linje.rstrip("\n")
                linje = linje.strip()

                if linje == "":
                    ignorert += 1
                    continue

                if linje.startswith("#"):
                    ignorert += 1
                    continue

                linje = linje.replace(",", ".")

                deler = linje.split()

                if len(deler) == 1:
                    tall_str = deler[0]
                elif len(deler) == 2:
                    tall_str, enhet = deler
                    if enhet != "ms":
                        logg.write(f"{linjenr}: {original} – feil enhet\n")
                        feil += 1
                        continue
                else:
                    logg.write(f"{linjenr}: {original} – feil format\n")
                    feil += 1
                    continue

                try:
                    verdi = float(tall_str)
                except:
                    logg.write(f"{linjenr}: {original} – ikke tall\n")
                    feil += 1
                    continue

                gyldige.append(verdi)

            if len(gyldige) > 0:
                total = sum(gyldige)
                min_val = min(gyldige)
                max_val = max(gyldige)
                avg = total / len(gyldige)
            else:
                total = 0
                min_val = None
                max_val = None
                avg = None

            logg.write("\n--- Oppsummering ---\n")
            logg.write(f"Gyldige målinger: {len(gyldige)}\n")
            logg.write(f"Ignorerte linjer: {ignorert}\n")
            logg.write(f"Feil linjer: {feil}\n")
            if avg is not None:
                logg.write(f"Min: {min_val:.2f} ms\n")
                logg.write(f"Max: {max_val:.2f} ms\n")
                logg.write(f"Gjennomsnitt: {avg:.2f} ms\n")

    except FileNotFoundError:
        with open(loggfil, "w") as logg:
            logg.write("Inputfil ikke funnet.\n")

    if len(gyldige) > 0:
        with open(rapportfil, "w") as r:
            r.write("Rapport for responstider\n")
            r.write("------------------------\n")
            r.write(f"Gyldige målinger: {len(gyldige)}\n")
            r.write(f"Total: {total:.2f} ms\n")
            r.write(f"Min: {min_val:.2f} ms\n")
            r.write(f"Max: {max_val:.2f} ms\n")
            r.write(f"Gjennomsnitt: {avg:.2f} ms\n")
