# Wout Poelen
import re
import tkinter


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

    return data_dic


def controle_consensus(data_dic):
    """"Deze functie kijkt of een van de consensus patronenen erin zit en
    bij welke en bij hoeveel"""

    counter = 0

    data_string = str(data_dic)
    for i in data_string:
        if re.search("[ST]G[LIVMFYW{3}][GN].{2}T[LIVM?].T.{2}H",
                     data_string) is not None:
            counter += 1
            print(data_dic[0][1][2])

    for i in data_string:
        if re.search("T.{2} [GC][NQ]SGS.[LIVM][FY]",
                     data_string) is not None:

            counter += 1
            print(data_dic[0][1][2])

    print(counter)


class GUI:

    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.top_frame.pack()
        self.bottom_frame.pack()

        self.label1 = tkinter.Label(self.top_frame,
                                    text="Wat wil je weten?")
        self.label1.pack()

        self.button1 = tkinter.Button(self.bottom_frame,
                                      text="consensus_aantal",
                                      command=self.action1)

        self.button2 = tkinter.Button(self.bottom_frame,
                                      text="protein_id",
                                      command=self.action2)

        self.button3 = tkinter.Button(self.bottom_frame,
                                      text="eiwit product",
                                      command=self.action3)

        self.button1.pack()
        self.button2.pack()
        self.button3.pack()

        tkinter.mainloop()

    def action1(self):
        tkinter.messagebox.showinfo()



def main():

    lijn_list = open_bestand()

    eiwit_lijst(lijn_list)

    data_dic = eiwit_lijst(lijn_list)

    controle_consensus(data_dic)

    gui = GUI()



main()
