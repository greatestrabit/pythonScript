from pypinyin import pinyin, lazy_pinyin, Style


def word_to_pinyin(word: str):
    pinyin_list = pinyin(word.strip(), style=Style.FIRST_LETTER)

    final_pinyin = ''
    for pinyin_str in pinyin_list:
        final_pinyin = final_pinyin + pinyin_str[0]

    return final_pinyin


def wordlist_to_pinyinlist(wordlist):
    pinyinlist = []
    for word in wordlist:
        pinyin_str = word_to_pinyin(word)
        pinyinlist.append(pinyin_str)
    return pinyinlist


def create_table_sql(columnlist, headlist, lengthlist):
    if len(columnlist) != len(headlist):
        return

    table_name = ''
    for column in columnlist:
        table_name = table_name + column[0]

    sql = 'CREATE TABLE `' + table_name + '` ('
    for index, value in enumerate(columnlist):
        if index < len(columnlist) - 1:
            sql = sql + '`' + value + "` varchar(" + str(lengthlist[index]) + ") DEFAULT NULL COMMENT '" + headlist[
                index] + "',"
        else:
            sql = sql + '`' + value + "` varchar(" + str(lengthlist[index]) + ") DEFAULT NULL COMMENT '" + str(
                headlist[index]).strip() + "')"

    return sql


def insert_sql(datalist, columnlist):
    if len(datalist) != len(columnlist):
        return

    table_name = ''
    for column in columnlist:
        table_name = table_name + column[0]

    sql = 'INSERT INTO  `' + table_name + '` VALUES ('
    for index, value in enumerate(datalist):
        if index < len(columnlist) - 1:
            sql = sql + '"' + value + '",'
        else:
            sql = sql + '"' + value + '")'

    return sql


def preproc(line: str):
    final_line = ''

    prelist = line.split('"')
    for index, value in enumerate(prelist):
        if index % 2:
            final_line = final_line + value.strip().replace(',', '')
        else:
            final_line = final_line + value.strip()

    return final_line


def get_length_list(csvfile, length):
    length_list = []
    for x in range(length):
        length_list.append(0)

    for line in csvfile.readlines():
        line = preproc(line)
        data_list = line.split(',')
        for index, value in enumerate(data_list):
            if len(value) > length_list[index]:
                length_list[index] = len(value)

    return length_list
