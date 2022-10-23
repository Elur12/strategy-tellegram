import sqlite3


def main():
    con = sqlite3.connect("main.db")
    cur = con.cursor()
    return con, cur


class users():
    con = None
    cur = None
    def __init__(self, conf) -> None:
        self.con = conf[0]
        self.cur = conf[1]

        self.cur.execute("""CREATE TABLE IF NOT EXISTS users(
           id INT PRIMARY KEY,
           name TEXT,
           chatID INT,
           score INT,
           campChange INT,
           accessLevel INT);
        """)
        self.con.commit()

class campChange():
    con = None
    cur = None
    def __init__(self, conf) -> None:
        self.con = conf[0]
        self.cur = conf[1]

        self.cur.execute("""CREATE TABLE IF NOT EXISTS campChange(
           id INT PRIMARY KEY,
           beginDate TEXT,
           finishDate TEXT,
           name TEXT,
           score INT);
        """)
        self.con.commit()

class timeTable():
    con = None
    cur = None
    def __init__(self, conf) -> None:
        self.con = conf[0]
        self.cur = conf[1]

        self.cur.execute("""CREATE TABLE IF NOT EXISTS timeTable(
           id INT PRIMARY KEY,
           date TEXT,
           timeTable BLOB,
           campChange INT);
        """)
        self.con.commit()

class personalHistory():
    con = None
    cur = None
    def __init__(self, conf) -> None:
        self.con = conf[0]
        self.cur = conf[1]

        self.cur.execute("""CREATE TABLE IF NOT EXISTS personalHistory(
           id INT PRIMARY KEY,
           fromWhom INT,
           toWhom INT,
           amount INT,
           cause INT,
           comment INT,
           dateTimeAdd TEXT);
        """)
        self.con.commit()

class commandHistory():
    con = None
    cur = None
    def __init__(self, conf) -> None:
        self.con = conf[0]
        self.cur = conf[1]

        self.cur.execute("""CREATE TABLE IF NOT EXISTS commandHistory(
           id INT PRIMARY KEY,
           fromWhom INT,
           toWhom INT,
           amount INT,
           cause INT,
           comment INT,
           dateTimeAdd TEXT);
        """)
        self.con.commit()

class causePersonal():
    con = None
    cur = None
    def __init__(self, conf) -> None:
        self.con = conf[0]
        self.cur = conf[1]

        self.cur.execute("""CREATE TABLE IF NOT EXISTS causePersonal(
           id INT PRIMARY KEY,
           accessLevel INT,
           title INT,
           maxScore INT);
        """)
        self.con.commit()

class causeCommand():
    con = None
    cur = None
    def __init__(self, conf) -> None:
        self.con = conf[0]
        self.cur = conf[1]

        self.cur.execute("""CREATE TABLE IF NOT EXISTS causeCommand(
           id INT PRIMARY KEY,
           accessLevel INT,
           title INT,
           maxScore INT);
        """)
        self.con.commit()

class achievements():
    con = None
    cur = None
    def __init__(self, conf) -> None:
        self.con = conf[0]
        self.cur = conf[1]

        self.cur.execute("""CREATE TABLE IF NOT EXISTS achievements(
           id INT PRIMARY KEY,
           title INT,
           description INT,
           mode TEXT,
           maxScore INT);
        """)
        self.con.commit()

