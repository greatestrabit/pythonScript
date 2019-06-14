import pymysql
from decimal import Decimal

"""
pip install pymysql
pymysql操作简单,性能较低,生产环境推荐mysqlclient
"""

print('\ndelete from common_sl;\n')
db = pymysql.connect(host="fatdb", port=5688, user='root', passwd='root123456', db='accounting_common')
cursor = db.cursor()
sql = 'select distinct(k_xzqhid) as xzqh from common_sl'
cursor.execute(sql)
data = cursor.fetchall()
for item in data:
    item_sql = 'select K_XZQHID,K_SLMC,K_SL,K_QYRQ,K_TYRQ,K_XH from common_sl where k_xzqhid=' + item[
        0] + ' order by k_sl desc'
    cursor.execute(item_sql)
    item_data = cursor.fetchall()

    for index, row_data in enumerate(item_data):
        new_sql = 'insert into common_sl(K_XZQHID,K_SLMC,K_SL,K_QYRQ,K_TYRQ,K_XH) values ('
        for column_index in range(len(row_data) - 1):
            if (type(row_data[column_index]) is Decimal):
                new_sql = new_sql + str(row_data[column_index]) + ','
            else:
                new_sql = new_sql + "'" + str(row_data[column_index]) + "',"
        new_sql += str(index + 1) + ');'
        print(new_sql)
