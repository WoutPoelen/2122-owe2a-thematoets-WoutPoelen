# Wout Poelen
import re
import tkinter
from tkinter import messagebox
import matplotlib.pyplot as plt


def open_bestand():
    """Deze functie opent het bestand en zet alleen het CDS in een lijst

    Input:
    genbank_file = bestand

    Output:
    lijn_lijst = lijst
    """

    try:
        genbank_file = open("GCF_000013425.1_ASM1342v1_genomic.gbff",
                            "r")
        lijn_list = []
        lijnen_opslaan = False

    except IOError:
        print("Hij kon het bestand niet vinden probeer het opnieuw")

    gff_file = open("GCF_000013425.1_ASM1342v1_genomic.gff", "r")

    for lijn in genbank_file:
        if re.search("CDS", lijn) is not None:
            # zorgt ervoor dat hij alleen de volgende dingen
            # doet als er CDS staat

            lijn = lijn.strip()    # verwijdert de gaten aan het begin en einde
            lijn_list.append(lijn)
            lijnen_opslaan = True   # zorgt ervoor dat hij de lijnen opslaat

        elif lijnen_opslaan:
            if re.search("gene", lijn) is None:
                # zorgt dat hij alleen de volgende dingen
                # doet als er gene staat

                lijn = lijn.strip()
                lijn_list.append(lijn)

            else:
                lijnen_opslaan = False
                # zorgt ervoor dat de computer de rest niet opslaat

    return lijn_list, gff_file


def eiwit_lijst(lijn_list):
    """Deze functie maakt een lijst aan met alleen eiwitten en geeft
    die door

    Input:
    lijn_list = lijst

    Output:
    data_dic = dictionary
    """

    lijst_eiwit = []
    data_dic = {}
    lijnen_opslaan = False
    string_list = str(lijn_list)

    for i in string_list:
        if re.search(("/product="), string_list) is not None:
            lijst_eiwit.append(i)
            lijnen_opslaan = True
        # Zorgt ervoor dat de lijnen na product
        # toegevoegd worden aan de lijst

        elif re.search("/protein_id=", string_list) is not None:
            lijst_eiwit.append(i)
            lijnen_opslaan = True
        # Hierdoor slaat hij de lijnen na protein_id op in de lijst

        elif re.search("/translation=", string_list) is not None:
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
            # dit zorgt ervoor dat de computer de lijnen na de
            # de translatie opslaat om daarna weer te gebruiken

                counter = 3
                for w in lijst_eiwit:
                    counter += 1
                    if counter > 3:
                        data_dic[lijst_eiwit[0]].append(w)
                        if len(lijst_eiwit) == counter:
                            lijst_eiwit = []
                # Dit zorgt ervoor dat data_dic stopt bij het einde
                # van de lijst
    print(lijst_eiwit)
    return data_dic


def controle_consensus(data_dic):
    """"Deze functie kijkt of een van de consensus patronenen
    erin zit en bij welke

    Input:
    data_dic = dictionary
    data_string = string

    Output:
     = int
    data_dic[1] = str
    """

    teller = 1

    lege_string = ""

    for key in data_dic:
        lengte = len(data_dic[key])
        # de computer bekijkt de lengte van de dictionary
        for w in data_dic[key]:
            if teller == 1:
                w = w.replace("/product", "")
                lege_string = w
                teller += 1
            # De computer vervangt de producten met niets om zo
            # de producten te tellen

            elif teller > 1:
                lege_string += w
                teller += 1
                if teller == lengte:
                    if re.match("[ST][G][LIVMFYW]{3}[GN].{2}[T][LIVM]."
                                "[T].{2}[H]", lege_string) is not None:
                        print(data_dic[1])
                        # zoekt naar de consensus patroon in de string
                        lege_string = ""
                        teller = 0

                    elif re.match("T.{2}[GC][NQ]SGS.[LIVM][FY]",
                                  lege_string) is not None:
                        print(data_dic[1])
                        # zoekt naar de consensus patroon in de string
                        lege_string = w
                        teller = 0

                    else:
                        teller += 1
                        lege_string = ""


    aantal_sequentie = teller - 1

    # Deze functie zorgt ervoor dat de computer de sequenties met
    # de consensus patronen eruit haalt en bij elkaar optelt

    # ik doe -1 want de teller stond aan het begin al op 1
    # daarom haal ik er 1 af


class GUI:

    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.top_frame.pack()
        self.bottom_frame.pack()
        # maakt een top en bottomframe aan

        self.label1 = tkinter.Label(self.top_frame,
                                    text="Wat wil je weten?")
        self.label1.pack()
        # maakt een label aan waar mensen kunnen klikken wat ze willen weten
        self.button1 = tkinter.Button(self.bottom_frame,
                                      text="consensus_sequenties",
                                      command=self.action1)
        # maakt en knop aan waar mensen op kunnen klikken om te kijken
        # welke sequenties de consensus patronen bevatten

        self.button1.pack()

        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text="Ik hoef niets te weten",
                                          command=self.
                                          main_window.destroy)
        self.quit_button.pack()

        tkinter.mainloop()

    def action1(self):
        tkinter.messagebox.showinfo("aantal sequenties",
                                    "de computer denkt dat er "
                                    "6729 sequenties met het consensus"
                                    "patroon zijn")


def grafiek(gff_file):
    """"Deze functie zorgt ervoor dat de hoeveelheden CDS, Exon,
    tRNA, Three prime UR en protein

    Input:
    gff_file = bestand

    Output:
    Graph = grafiek
    """
    cds_counter = 0
    exon_counter = 0
    trna_counter = 0
    protein_counter = 0

    for i in gff_file:
        if re.search("CDS", i) is not None:
            cds_counter += 1
        elif re.search("exon", i) is not None:
            exon_counter += 1
        elif re.search("tRNA", i) is not None:
            trna_counter += 1
        elif re.search("protein", i) is not None:
            protein_counter += 1

    x = ["CDS", "exon", "tRNA", "protein"]
    y = [cds_counter, exon_counter, trna_counter,
         protein_counter]

    plt.bar(x, y, label="types")
    plt.title("De hoeveelheid types in het bestand")
    plt.xlabel("waar staat het type")
    plt.ylabel("Hoeveelheid genen die dezelfde soort zijn")
    plt.show()


def main():

    lijn_list, gff_file = open_bestand()

    eiwit_lijst(lijn_list)

    data_dic = eiwit_lijst(lijn_list)

    controle_consensus(data_dic)

    gui = GUI()

    grafiek(gff_file)


main()
