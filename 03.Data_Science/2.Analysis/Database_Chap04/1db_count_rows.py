#!/usr/bin/env python3
import sqlite3

# 메모리에 SQLite3 데이터베이스를 만든다.
# 네 가지 속성을 지닌 sales 테이블을 만든다.
con = sqlite3.connect(':memory:')
query = """CREATE TABLE sales
            (customer VARCHAR(20),
            product VARCHAR(40),
            amount FLOAT,
            date DATE);"""
con.execute(query)
con.commit()

# sales 테이블에 데이터를 삽입한다.
data = [('Richard Lucas', 'Notepad',2.50,'2014-01-02'),
        ('Jenny Kim','Binder',4.15,'2014-01-15'),
        ('Svetland Crow','Printer', 155.75,'2014-02-03'),
        ('Stephen Randolph','Computer', 679.40,'2014-02-20')]
statement = "INSERT INTO sales VALUES(?, ?, ?, ?)"
con.executemany(statement, data)
con.commit()

# sales 테이블에 질의한다.
cursor = con.execute("SELECT * FROM sales")
rows = cursor.fetchall()

# 출력된 데이터의 수를 센다.
row_counter = 0
for row in rows:
    print(row)
    row_counter += 1
print("Number of rows: {}".format(row_counter))