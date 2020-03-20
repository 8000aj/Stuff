import pymysql.cursors


def pull_table(live_schema, table_title):
    con1 = pymysql.connect(host="localhost",
                           user="jefferson",
                           passwd="1234",
                           db=live_schema)
    with con1.cursor() as cursor1:
        # pull_table_command = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        pull_table_command = "SELECT * FROM " + table_title
        cursor1.execute(pull_table_command)
        result = cursor1.fetchall()

        # name, type_code, display_size, internal_size, precision, scale, null_ok
        # col = cursor1.description

        # for r in result:
        #     print(r)
        # for c in col:
        #     print(c)

        return (result)
        cursor1.close()


def percentage_change(v1, v2):
    cal = ((v2 - v1) / abs(v1)) * 100
    result_pc = round(cal, 2)
    return result_pc


def value_change(v1, v2):
    result_vc = (v2 - v1)
    return result_vc


def conv(x):
    if ((x[-1]) == "M"):

        conv_m = ((float(x[:-1])) * 1000000)
        return (conv_m)

    elif ((x[-1]) == "B"):
        conv_m = ((float(x[:-1])) * 1000000000)
        return (conv_m)
    else:
        pass


# print(percentage_change(117, 34))

# print(percentage_change(44, 18))


# print(percentage_change(60, 12000))

# print(percentage_change(46, 50))
# print(percentage_change(43.26, 50))
# print(percentage_change(43.26, 47))

# print(percentage_change(600, 503))
# print("BAC, 20.51 - 23 / " + str(percentage_change(20.51, 23)))
# print("C, 43.26 - 49 / " + str(percentage_change(43.26, 49)))
# print("JPM, 88.05 - 100 / " + str(percentage_change(88.05, 100)))

print(percentage_change(269.32, 259))
print(percentage_change(269.32, 234.3))
# result = pull_table("sp500", "JPM_income_statement_master")
# print(len(result))
# for r in result:
#     print(r)

# 20200113 01:30
# for now lets just do a simple exercise
# q / q performance in operating revenue for aapl income statement
# percentage change & value change

# v1 = conv(result[152][2])
# v2 = conv(result[151][2])

# v3 = conv(result[151][2])
# v4 = conv(result[150][2])

master_analysis_pc = []
master_analysis_vc = []
master_time = []

# for x in range(128, 0, -1):

#     v1 = conv(result[x][2])
#     v2 = conv(result[x - 1][2])

#     result_one = percentage_change(v1, v2)
#     result_two = value_change(v1, v2)
#     period_one = result[x][1] + "-" + result[x - 1][1]

#     master_analysis_pc.append(result_one)
#     master_analysis_vc.append(result_two)
#     master_time.append(period_one)

# for x in range(0, 128, 1):
#     print(master_analysis_pc[x])
#     print(master_analysis_vc[x])
#     print(master_time[x])
#     print('')


# print(v1)
# print(v2)

# result_one = percentage_change(v1, v2)

# print(result_one)


# how to add new financials? or how to flip, then append.

# ALTER TABLE `20190822db`.`users`
# DROP COLUMN `id`,
# DROP PRIMARY KEY;
# ;

# ORDER ALPHABETICALLY
# SELECT * FROM table_name ORDER BY col_name;

# DROP COL
# ALTER TABLE table_name DROP COLUMN col_name;

# REBUILD ID PK
# ALTER TABLE users ADD id int UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST;


# program the statement for comparative analysis
# percentage change
# value change
# so what do you want to see?
# growth rate over time

# the colour of their financials
# the health of the company
# the margin of safety

# ratios:


# visualization


# need to add in some understanding of the data.
# some values are not present, esp in the earlier statements.
# check for values
# grab the scope of available data
# perform analysis on the scope
