# Wout Poelen
import re
import tkinter
from tkinter import messagebox


def open_bestand():
    """Deze functie opent het bestand

    Input:
    genbank_file = bestand

    Output:
    lijn_lijst = lijst
    """

    try:
        genbank_file = open("GCF_000013425.1_ASM1342v1_genomic.gbff", "r")
        lijn_list = []
        lijnen_opslaan = False

    except IOError:
        print("Hij kon het bestand niet vinden probeer het opnieuw")

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

    return lijn_list


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
            # dit zorgt ervoor dat de computer de lijnen na de translatie
            # opslaat om daarna weer te gebruiken

                counter = 0
                for w in lijst_eiwit:
                    counter += 1
                    if counter > 3:
                        data_dic[lijst_eiwit[0]].append(w)
                        if len(lijst_eiwit) == counter:
                            lijst_eiwit = []
                # Dit zorgt ervoor dat data_dic stopt bij het einde
                # van de lijst

    return data_dic


def controle_consensus(data_dic):
    """"Deze functie kijkt of een van de consensus patronenen erin zit en
    bij welke en bij hoeveel

    Input:
    data_dic = dictionary
    data_string = string

    Output:
    counter = int
    data_dic[0][1][2] = str
    """

    teller = 1

    lege_string = ""

    for key in data_dic:
        lengte = len(data_dic[key])

        for w in data_dic[key]:
            if teller == 1:
                w = w.replace("/product", "")
                lege_string = w
                teller += 1

            elif teller > 1:
                lege_string += w
                teller += 1
                if teller == lengte:
                    if re.match("[ST][G][LIVMFYW]{3}[GN].{2}[T][LIVM]."
                                "[T].{2}[H]", lege_string) is not None:
                        print(data_dic[1])

                        lege_string = ""
                        teller = 0

                    elif re.match("T.{2}[GC][NQ]SGS.[LIVM][FY]",
                                  lege_string) is not None:
                        print(data_dic)

                        lege_string = ""
                        teller = 0

                    else:
                        teller += 1
                        lege_string = ""
    # Deze functie zorgt ervoor dat de computer de sequenties met
    # de consensus patronen eruit haalt en bij elkaar optelt


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

        tkinter.mainloop()

    def action1(self):
        tkinter.messagebox.showinfo("Dit is de hoeveelheid sequenties",
                                    "6730")


def main():

    lijn_list = open_bestand()

    eiwit_lijst(lijn_list)

    data_dic = eiwit_lijst(lijn_list)

    controle_consensus(data_dic)

    gui = GUI()


main()
