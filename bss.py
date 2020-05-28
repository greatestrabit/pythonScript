import requests
import json
from prettytable import PrettyTable

username = ''
password = ''

dbname = 'qiyeDataBase'
schema_name = ''
row = 10000
sql = 'select 1'

quit_str = 'quit'
exit_str = 'exit'

show_str = 'show'
des_str = 'describe'
explain_str = 'explain'

login_url = 'http://ip:8082/bss/user/login'
logout_url = 'http://ip:8082/bss/user/logout'
query_url = 'http://ip:8082/bss/query/defineQuery'

welcome = '''mysql: [Warning] Using a password on the command line interface can be insecure.
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 2294397
Server version: 5.7.11-log MySQL Community Server (GPL)

Copyright (c) 2000, 2019, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
'''


def print_table(rows):
    row1 = rows[0]
    x = PrettyTable()
    x.field_names = row1.keys()
    for rowdata in rows:
        x.add_row(rowdata.values())
    print(x)


login_payload = {'username': username, 'password': password}
r = requests.get(login_url, login_payload)
result = json.loads(r.text)
print(welcome)
cookies = r.cookies

query_payload = {'sql': sql, 'rows': row, 'DBNAME': dbname, 'SCHEMANAME': schema_name}
new_sql = sql
while new_sql != quit_str and new_sql != exit_str:
    new_sql = input('mysql> ')
    if new_sql == quit_str or new_sql == exit_str:
        break

    new_sql = new_sql.replace(';', '')

    if new_sql.startswith('use'):
        schema_name = new_sql.split(' ')[1]
        query_payload['SCHEMANAME'] = schema_name
        print('Database changed')
        continue

    if new_sql.startswith(explain_str):
        new_sql = new_sql.replace(explain_str, des_str)

    if not (new_sql.startswith(show_str) or new_sql.startswith(des_str)):
        sql_item = new_sql.split(' ')
        if sql_item[len(sql_item) - 2] != 'limit':
            new_sql += ' limit 100'

    query_payload['sql'] = new_sql
    r = requests.post(query_url, query_payload, cookies=cookies)
    result = json.loads(r.text)
    success = result['success']
    if success:
        total = result['total']
        if total == 0:
            print('Empty set (0.00 sec)\n')
        else:
            rows = result['rows']
            print_table(rows)
            if total == 1:
                print(str(total) + ' row in set (0.00 sec)\n')
            else:
                print(str(total) + ' rows in set (0.00 sec)\n')
    else:
        print(result['message'])

requests.get(logout_url)
print('Bye')
