# Wout Poelen
import re


def open_bestand():
    """Deze functie opent het bestand"""

    # voeg een exception handeling toe
    genbank_file = open("GCF_000013425.1_ASM1342v1_genomic.gbff", "r")
    lijn_list = []
    lijnen_opslaan = False

    for lijn in genbank_file:
        if re.search("CDS", lijn) is not None:
        # zorgt ervoor dat hij alleen de volgende dingen doet als er CDS staat
            lijn = lijn.strip()    # verwijdert de gaten aan het begin en einde
            lijn_list.append(lijn)
            lijnen_opslaan = True   # zorgt ervoor dat hij de lijnen opslaat

        elif lijnen_opslaan:
            if re.search("gene", lijn) is None:
            # zorgt dat hij alleen de volgende dingen doet als er gene staat
                lijn = lijn.strip()
                lijn_list.append(lijn)

            else:
                lijnen_opslaan = False
                # zorgt ervoor dat de computer de rest niet opslaat

    return lijn_list


def eiwit_lijst(lijn_list):
    """Deze functie maakt een lijst aan met alleen eiwitten en geeft
    die door"""

    lijst_eiwit = []
    data_dic = {}
    lijnen_opslaan = False

    for i in lijn_list:
        if re.search(("/product="), i) is not None:
            lijst_eiwit.append(i)
        # Zorgt ervoor dat de lijnen na product toegevoegd worden aan de lijst

        elif re.search("/protein_id=", i) is not None:
            lijst_eiwit.append(i)
        # Hierdoor slaat hij de lijnen na protein_id op in de lijst

        elif re.search("/translation=", i) is not None:
            lijst_eiwit.append(i)
            lijnen_opslaan = True
        # Zorgt ervoor dat de computer de translatie eruit haalt en
        # opslaat in de lijst

        elif lijnen_opslaan:
            lijst_eiwit.append(i)
            if re.search("\"", i) is not None:
                lijnen_opslaan = False
                data_dic[lijst_eiwit[0]] = [lijst_eiwit[1],
                                            lijst_eiwit[2]]

                counter = 0
                for i in lijst_eiwit:
                    counter += 1
                    if counter > 3:
                        data_dic[lijst_eiwit[0]].append(i)
                        if len(lijst_eiwit) == counter:
                            lijst_eiwit = []

    print(data_dic)

    return data_dic


def controle_consensus():
    """"Deze functie kijkt of een van de consensus patronenen erin zit en
    bij welke en bij hoeveel"""

    counter = 0
    # if re.search("[S|T?]G[L|I|V|M|F|Y|W?][G|N?](\.)[2]T[L|I|V|M?].T"
                 # "(\.[2])H", eiwitlijst):

    # re.search("T(\.[2])[G|C][N|Q]SGS(\.)[L|I|V|M][F|Y]", eiwitlijst)


def main():

    lijn_list = open_bestand()

    eiwit_lijst(lijn_list)

    data_dic = controle_consensus()



main()
