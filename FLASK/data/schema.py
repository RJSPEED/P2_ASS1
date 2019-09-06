import sqlite3
import os

DIR = os.path.dirname(__file__)
DBFILENAME = "p2a1.db"
DBPATH = os.path.join(DIR, DBFILENAME)

def schema(dbpath=DBPATH):
    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()
        DROPSQL = "DROP TABLE IF EXISTS {tablename};"

        cur.execute(DROPSQL.format(tablename="branch"))

        # SQL = """CREATE TABLE campuses(
        #         pk INTEGER PRIMARY KEY AUTOINCREMENT,
        #         city VARCHAR(20) NOT NULL,
        #         state VARCHAR(20),
        #         UNIQUE(city, state)
        #     );"""

        SQL = """CREATE TABLE branch(
                pk INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(50) NOT NULL,
                city VARCHAR(20) NOT NULL,
                UNIQUE(name, city)
            );"""

        cur.execute(SQL)
        
        cur.execute(DROPSQL.format(tablename="employee"))

        # SQL = """CREATE TABLE students(
        #     pk INTEGER PRIMARY KEY AUTOINCREMENT,
        #     campuses_pk INT,
        #     first_name VARCHAR(20) NOT NULL,
        #     last_name VARCHAR(20) NOT NULL,
        #     id VARCHAR(20) NOT NULL,
        #     gpa FLOAT,
        #     FOREIGN KEY(campuses_pk) REFERENCES campuses(pk)
        #     );"""

        SQL = """CREATE TABLE employee(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            branch_pk INT,
            first_name VARCHAR(20) NOT NULL,
            last_name VARCHAR(20) NOT NULL,
            FOREIGN KEY(branch_pk) REFERENCES branch(pk)
            );"""
        
        cur.execute(SQL)

if __name__ == "__main__":
    schema()

