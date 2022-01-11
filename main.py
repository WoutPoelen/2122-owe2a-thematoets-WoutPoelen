#Wout Poelen

def open_bestand():
    """Deze functie opent het bestand"""
    counter = 0

    Genbank_file = open("GCF_000013425.1_ASM1342v1_genomic.gbff", "r")
    reading = str(Genbank_file.readlines())

    for read in reading:
        counter += 1

        if counter < 41:
            pass

    Genbank_split = reading.split("/")
    print(Genbank_split)







def main():
    open_bestand()


main()
