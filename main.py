#Wout Poelen
import re


def open_bestand():
    """Deze functie opent het bestand"""
    counter = 0
    #voeg een exception handeling toe
    Genbank_file = open("GCF_000013425.1_ASM1342v1_genomic.gbff", "r")
    reading = str(Genbank_file.readlines())

    for read in reading:
        counter += 1

        if counter < 41:
            pass

    Genbank_split = reading.split("\t")
    #print(Genbank_split)

    return(Genbank_split)


def Translate_dictionary():
    """"Deze functie maakt een dictionary aan om te kunnen transleren"""
    # verander de hoge komma's in dubbele hoge komma's

    translatie_dictionary = {
        "ATA": "I", "ATC": "I", "ATT": "I", "ATG": "M",
        "ACA": "T", "ACC": "T", "ACG": "T", "ACT": "T",
        'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
        'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
        'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
        'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
        'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
        'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
        'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
        'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
        'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_',
        'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W',
    }

    return(translatie_dictionary)


def eiwit_lijst(file):
    """Deze functie maakt een lijst aan met alleen eiwitten en geeft
    die door"""

    eiwit_lijst = []

    letters = str(file)

    for i in letters:
        if re.search(["/translation="], letters) == None:
            eiwit_lijst.append()
    print(eiwit_lijst)

    return eiwit_lijst



def controle_consensus():
    """"Deze functie kijkt of een van de consensus patronenen erin zit en
    bij welke en bij hoeveel"""

    counter = 0
    #re.search("[ST?]-G-(LIVMFYW?)-(GN?)-(\.[2]-T-[LIVM?]-.-T-\.[2]-H", eiwit_lijst)
    #re.search("T-\.[2]-[GC]-[NQ]-S-G-S-\.-[LIVM]-[FY]", eiwit_lijst)
    #k


def main():
    open_bestand()

    file = open_bestand()
    eiwit_lijst(file)
    Translate_dictionary()


main()
