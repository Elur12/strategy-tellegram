import sqlite3


def main():
    con = sqlite3.connect("main.db")
    cur = con.cursor()
    return con, cur


class users():
    con = None
    cur = None
    def __init__(self, con, cur) -> None:
        self.con = con
        self.cur = cur

        self.cur.execute("""CREATE TABLE IF NOT EXISTS users(
           id INT PRIMARY KEY,
           name TEXT,
           chatID INT,
           score INT,
           campChange INT,
           accessLevel INT);
        """)
        con.commit()

class campChange():
    con = None
    cur = None
    def __init__(self, con, cur) -> None:
        self.con = con
        self.cur = cur

        self.cur.execute("""CREATE TABLE IF NOT EXISTS campChange(
           id INT PRIMARY KEY,
           beginDate TEXT,
           finishDate TEXT,
           name TEXT,
           score INT);
        """)
        con.commit()

class timeTable():
    con = None
    cur = None
    def __init__(self, con, cur) -> None:
        self.con = con
        self.cur = cur

        self.cur.execute("""CREATE TABLE IF NOT EXISTS campChange(
           id INT PRIMARY KEY,
           date TEXT,
           timeTable BLOB,
           campChange INT);
        """)
        con.commit()

class personalHistory():
    con = None
    cur = None
    def __init__(self, con, cur) -> None:
        self.con = con
        self.cur = cur

        self.cur.execute("""CREATE TABLE IF NOT EXISTS campChange(
           id INT PRIMARY KEY,
           from INT,
           to INT,
           amount INT,
           cause INT,
           comment INT);
        """)
        con.commit()

class commandHistory():
    con = None
    cur = None
    def __init__(self, con, cur) -> None:
        self.con = con
        self.cur = cur

        self.cur.execute("""CREATE TABLE IF NOT EXISTS campChange(
           id INT PRIMARY KEY,
           from INT,
           to INT,
           amount INT,
           cause INT,
           comment INT);
        """)
        con.commit()

class causePersonal():
    con = None
    cur = None
    def __init__(self, con, cur) -> None:
        self.con = con
        self.cur = cur

        self.cur.execute("""CREATE TABLE IF NOT EXISTS campChange(
           id INT PRIMARY KEY,
           accessLevel INT,
           title INT,
           maxScore INT);
        """)
        con.commit()

class causeCommand():
    con = None
    cur = None
    def __init__(self, con, cur) -> None:
        self.con = con
        self.cur = cur

        self.cur.execute("""CREATE TABLE IF NOT EXISTS campChange(
           id INT PRIMARY KEY,
           accessLevel INT,
           title INT,
           maxScore INT);
        """)
        con.commit()

class achievements():
    con = None
    cur = None
    def __init__(self, con, cur) -> None:
        self.con = con
        self.cur = cur

        self.cur.execute("""CREATE TABLE IF NOT EXISTS campChange(
           id INT PRIMARY KEY,
           title INT,
           description INT,
           mode TEXT,
           maxScore INT);
        """)
        con.commit()