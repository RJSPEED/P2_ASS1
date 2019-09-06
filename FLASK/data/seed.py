import os
import sqlite3

DIR = os.path.dirname(__file__)
DBFILENAME = 'p2a1.db'
DBPATH = os.path.join(DIR, DBFILENAME)

def seed(dbpath=DBPATH):
    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()

        #Branches inserts
        SQL = """INSERT INTO branch(name, city) VALUES (?,?);"""

        branches = [
            ("Nottingham Smiths Bank", "Nottingham"),
            ("Nottingham City", "Nottingham"),
            ("Basford", "Nottingham"),
            ("Beeston", "Nottingham"),
            ("Arnold", "Nottingham"),
            ("Ilkeston", "Nottingham"),
            ("West Bridgford", "Nottingham"),
            ("Bulwell & Hucknall", "Nottingham"),
            ("Long Eaton", "Nottingham"),
            ("Bingham", "Nottingham"),
            ("City","Birmingham"),
            ("Grand Central","Birmingham"),
            ("Edgbaston","Birmingham"),
            ("Perry Barr","Birmingham"),
            ("Harbourne","Birmingham"),
            ("Kings Heath","Birmingham"),
            ("Smethwick","Birmingham"),
            ("Acocks Green","Birmingham"),
            ("West Bromwich","Birmingham"),
            ("Solihull","Birmingham")
        ]

        for branch in branches:
            cur.execute(SQL, branch)

        #Employees inserts
        SQL = """INSERT INTO employee(branch_pk, first_name, last_name) VALUES (?,?,?);"""

        employees = [
            (1,"Stuart","Head"),
            (1,"Timmy","Morrisey"),
            (1,"Barbar","Halsey"),
            (1,"Bobbye","Brumbaugh"),
            (1,"Lorie","Forsman"),
            (5,"Deandre","Marro"),
            (5,"Shyla","Nevitt"),
            (5,"Majorie","Sack"),
            (5,"Jestine","Brocious"),
            (5,"Bianca","Groman"),
            (2,"Cassidy","Dawson"),
            (2,"Serafina","Grullon"),
            (2,"Reinaldo","Glazer"),
            (2,"Emeline","Arterburn"),
            (2,"Santina","Statler"),
            (6,"Jenette","Newhall"),
            (6,"Eleanora","Fitch"),
            (6,"Sierra","Clickner"),
            (6,"Evelina","Schaper"),
            (6,"Zaida","Benfield"),
            (3,"Norberto","Rasch"),
            (3,"Giuseppe","Scheidler"),
            (3,"Nga","Wall"),
            (3,"Rudolph","Rakowski"),
            (3,"Kaci","Culberson"),
            (4,"Dewitt","Olivas"),
            (4,"Shira","Madera"),
            (4,"Eleanore","Hough"),
            (4,"Tonisha","Tuma"),
            (4,"Major","Blanche"),
            (7,"Terrell","Walburn"),
            (7,"Jann","Manson"),
            (7,"Judie","Clardy"),
            (7,"Beaulah","Beckett"),
            (7,"Carline","Rank"),
            (7,"Louann","Wescott"),
            (8,"Clare","Forsyth"),
            (8,"Sherley","Bascom"),
            (8,"Lovella","Ell"),
            (8,"Jaleesa","Manion"),
            (8,"Willodean","Silvas"),
            (9,"Veronica","Puzo"),
            (9,"Simone","Milbourn"),
            (9,"Marnie","Suits"),
            (9,"Hai","Cantin"),
            (9,"Latosha","Baumgardner"),
            (10,"Yoko","Ravenell"),
            (10,"Wendolyn","Dan"),
            (10,"Tonia","Hagstrom"),
            (10,"Desire","Riney"),
            (10,"Lupita","Noren"),
            (11,"Maybell","Damato"),
            (11,"Katharyn","Duchesne"),
            (11,"Lucie","Troia"),
            (11,"Trang","Hoback"),
            (11,"So","Devereux"),
            (12,"Tad","Schaller"),
            (12,"Tatyana","Streett"),
            (12,"Inger","Waddle"),
            (12,"Ellamae","Hendershot"),
            (12,"Eugene","Bella"),
            (13,"Thersa","Cowens"),
            (13,"Verona","Winchester"),
            (13,"Abel","Sykes"),
            (13,"Claude","Deerman"),
            (13,"Georgine","Ivey"),
            (14,"Basil","Lena"),
            (14,"Eduardo","Lanz"),
            (14,"Lavonia","Korus"),
            (14,"Fritz","Kopf"),
            (14,"Sook","Ahart"),
            (15,"Mercedes","Pinette"),
            (15,"Magali","Suchan"),
            (15,"Lilla","Doolin"),
            (15,"Samatha","Lauer"),
            (15,"Marylyn","Rieder"),
            (16,"Lashunda","Witherspoon"),
            (16,"Cristie","Doll"),
            (16,"Graciela","Tanksley"),
            (16,"Chantel","Franzen"),
            (16,"Jared","Grasser"),
            (17,"Melany","Napoles"),
            (17,"Errol","Windle"),
            (17,"Anton","Pidgeon"),
            (17,"Carie","Shows"),
            (17,"Charolette","Dupras"),
            (18,"Mittie","Fagin"),
            (18,"Aida","Debartolo"),
            (18,"Marlys","Herbst"),
            (18,"Rose","Arguelles"),
            (19,"Nakesha","Cooperman"),
            (19,"Lyn","Plemmons"),
            (19,"Tonita","Roberds"),
            (19,"Drew","Gaiter"),
            (19,"Mee","Cofield"),
            (20,"Syble","Chapel"),
            (20,"Antionette","Dolson"),
            (20,"Sharen","Tavares"),
            (20,"Vance","Broadwater"),
            (20,"Beryl","Trybus")
        ]

        for employee in employees:
            cur.execute(SQL, employee)

if __name__ == "__main__":
    seed()
