#!/usr/bin/env python3
import csv
import sqlite3
import sys

# CSV 입력 파일의 경로와 파일명
input_file = sys.argv[1]

# 메모리에 SQLite3 데이터베이스를 만든다.
# 다섯가지 속성을 지닌 Supplier 테이블을 만든다.
con = sqlite3.connect('Suppliers.db')
c = con.cursor()

# Suplliers 테이블에 데이터를 삭제시킨다.
statement = "DELETE FROM Suppliers WHERE Supplier_Name = 'Supplier Z'"
c.execute(statement)
con.commit()

# Suppliers 테이블에 질의한다.
output = c.execute("SELECT * FROM Suppliers")
# con.commit()
rows = output.fetchall()
for row in rows:
    output = []
    for column_index in range(len(row)):
        output.append(str(row[column_index]))
    print(output)