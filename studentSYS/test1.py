# Author: Dawei Xu
# Version:
# CreateTime: 2022/7/19 22:25

"""pip install psycopg2
postgre
"""
import psycopg2


def main():
    conn = psycopg2.connect(
        host="work-samples-db.cx4wctygygyq.us-east-1.rds.amazonaws.com",
        port='5432',
        database='work_samples',
        user='readonly',
        password='w2UIO@#bg532!'
    )
    cursor = conn.cursor()
    cursor.execute("select * from pg_tables where schemaname = 'public'")
    print(cursor.fetchall())
    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()
