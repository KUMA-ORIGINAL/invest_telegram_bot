import datetime
import sqlite3


def sql_start():
    global base, cur
    base = sqlite3.connect('invest.db')
    cur = base.cursor()
    if base:
        print('База данных подключилась')
    base.execute('CREATE TABLE IF NOT EXISTS users('
                 'id INTEGER PRIMARY KEY, '
                 'user_id INTEGER UNIQUE NOT NULL, '
                 'created TEXT NOT NULL, '
                 'balance INTEGER DEFAULT 0 NOT NULL, '
                 'invest INTEGER DEFAULT 0 NOT NULL, '
                 'profit INTEGER DEFAULT 0 NOT NULL)')
    base.commit()
    base.execute('CREATE TABLE IF NOT EXISTS referal_users('
                 'id INTEGER PRIMARY KEY,'
                 'user_id INTEGER UNIQUE NOT NULL,'
                 'referrer_id INTEGER)')
    base.commit()


async def create_user(user_id):
    cur.execute(f'INSERT INTO users (user_id, created) VALUES ({user_id}, {str(datetime.date.today())})')
    base.commit()


async def get_user(user_id):
    return cur.execute(f'SELECT id, created, balance, invest, profit FROM users WHERE user_id={user_id}').fetchall()


async def add_user(user_id, referrer_id=None):
    if referrer_id:
        cur.execute(f'INSERT INTO referal_users (user_id, referrer_id) VALUES ({user_id}, {referrer_id})')
        base.commit()
    else:
        cur.execute(f'INSERT INTO referal_users (user_id) VALUES ({user_id})')
        base.commit()


async def count_referals(user_id):
    return cur.execute(f'SELECT COUNT(id) as count FROM referal_users WHERE referrer_id={user_id}').fetchone()[0]
