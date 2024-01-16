import sqlite3 as sq


class Database(object):

    def __init__(self, path):
        self.connection = sq.connect(path)
        self.connection.execute('pragma foreign_keys = on')
        self.connection.commit()
        self.cur = self.connection.cursor()
        self.last_inserted_id = None

    def create_tables(self):
        self.query('CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY UNIQUE, '
                   'user_name TEXT,'
                   'type_subscripion TEXT,'
                   'start_subscription DATE,'
                   'end_subscription DATE,'
                   'registration DATE,'
                   'sum_buy REAL)')
        self.query('CREATE TABLE IF NOT EXISTS subscription (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INT, '
                   'subscription TEXT, '
                   'start_subscription DATE, end_subscription DATE, '
                   'FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE)')

    def query(self, arg, values=None):
        if values is None:
            self.cur.execute(arg)
        else:
            self.cur.execute(arg, values)
        self.connection.commit()

    def fetchone(self, arg, values=None):
        if values is None:
            self.cur.execute(arg)
        else:
            self.cur.execute(arg, values)
        return self.cur.fetchone()

    def fetchall(self, arg, values=None):
        if values is None:
            self.cur.execute(arg)
        else:
            self.cur.execute(arg, values)
        return self.cur.fetchall()

    def __del__(self):
        self.connection.close()