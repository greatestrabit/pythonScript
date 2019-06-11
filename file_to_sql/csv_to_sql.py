import os

from file_to_sql import list_to_sql_util as util

filepath = '/home/dugj/workspace/Enterprise-Registration-Data-of-Chinese-Mainland/Enterprise-Registration-Data/csv/1999/上海.csv'
separator = ','

if os.path.isfile(filepath):
    with open(filepath) as csvfile:
        headline = csvfile.readline()

        headlinelist = headline.split(separator)
        column_name_list = util.wordlist_to_pinyinlist(headlinelist)
        lengthlist = util.get_length_list(csvfile, len(headlinelist))

        create_tale_sql = util.create_table_sql(column_name_list, headlinelist, lengthlist)
        print(create_tale_sql)

        csvfile.seek(0, 0)
        next(csvfile)

        count = 0
        for line in csvfile.readlines():
            line = util.preproc(line)
            data_sql = util.insert_sql(line.split(separator), column_name_list)
            if data_sql:
                print(data_sql)
            else:
                count = count + 1
        print(count)
else:
    print(filepath)
