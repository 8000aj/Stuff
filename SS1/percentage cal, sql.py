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
    return (result_pc)


def value_change(v1, v2):
    result_vc = (v2 - v1)
    return (result_vc)

# conversion of shorthand to numerial (200M TO 200,000,000, 200B TO 200,000,000,000)


def conv(x):
    if ((x[-1]) == "M"):

        conv_m = ((float(x[:-1])) * 1000000)
        return (conv_m)

    elif ((x[-1]) == "B"):
        conv_m = ((float(x[:-1])) * 1000000000)
        return (conv_m)
    else:
        pass


def conv_list(x):
    l = []
    for v in x:
        if ((v[-1]) == "M"):

            conv_m = ((float(v[:-1])) * 1000000)
            l.append(conv_m)

        elif ((v[-1]) == "B"):
            conv_m = ((float(v[:-1])) * 1000000000)
            l.append(conv_m)
        else:
            pass
    return (l)


result = pull_table("sp500", "AAPL_income_statement_master")
# print(len(result))
# for r in result:
#     print(r)


# APPENDING RESULTS TO MASTER LISTS
# master_analysis_pc = []
# master_analysis_vc = []
# master_time = []
# for x in range(128, 0, -1):

#     v1 = conv(result[x][2])
#     v2 = conv(result[x - 1][2])

#     result_one = percentage_change(v1, v2)
#     result_two = value_change(v1, v2)
#     period_one = result[x][1] + "-" + result[x - 1][1]

#     master_analysis_pc.append(result_one)
#     master_analysis_vc.append(result_two)
#     master_time.append(period_one)

# PRINTING OF RESULTS
# for x in range(0, 128, 1):
#     print(master_analysis_pc[x])
#     print(master_analysis_vc[x])
#     print(master_time[x])
#     print('')


# print(v1)
# print(v2)

# result_one = percentage_change(v1, v2)

# print(result_one)


def value_presence_gate(n):
    v = []
    for x in range(0, (len(result)), 1):
        if ((result[x][n]) == ""):
            pass
        else:
            v.append(result[x][n])

    return (v)


# for x in cleaned_values:
#     print(x)


"""
TODO
build function:

enter symbol
store in master

    pull price action values
        get length of days
        get date range
        isolate
            perform analysis
        store in master

    pull income / profit values
        use date range of price action; from year
        isolate
            perform analysis
        store in master
"""


def symbol_price_action_pull(sym):
    symbol_price_action_title = sym + "_price_action"
    result_price_action = pull_table("sp500", symbol_price_action_title)
    return (result_price_action)


def symbol_income_statement_pull(sym):
    symbol_income_statement_title = sym + "_income_statement_master"
    result_income_statement = pull_table("sp500", symbol_income_statement_title)
    return (result_income_statement)


def income_statement_isolation(sym):
    result = symbol_income_statement_pull(sym)
    isolated_values = value_presence_gate(2)  # value_presence_gate(x) where x = the position in result (2 = income)
    return (isolated_values)


def operating_revenue_pull(sym):
    iv = income_statement_isolation(sym)
    cl = conv_list(iv)
    return (cl)

# jpm_price_action = symbol_price_action_pull("JPM")
# for x in jpm_price_action:
#     print(x)


# print("length of jpm_price_action: " + str(len(jpm_price_action)))

# id / date / open / high / low / close / volume
# 0     1      2      3      4      5       6
# from open of the first day, jpm_price_action[0][3]
# to close of the last day, jpm_price_action[5031][6]

# feed in the full list
def price_action_analysis(sym):
    spap = symbol_price_action_pull(sym)
    v1 = float(spap[0][2])
    print("price action analysis v1: " + str(v1))
    v2 = float(spap[5031][5])
    print("price action analysis v2: " + str(v2))
    result_price_action_analysis = percentage_change(v1, v2)

    return (result_price_action_analysis)

# feed in the isolated data


def income_analysis(sym):
    v = operating_revenue_pull(sym)
    v1 = float(v[(len(v) - 1)])
    print("income analysis v1: " + str(v1))
    v2 = float(v[0])
    print("income analysis v2: " + str(v2))

    result_income_analysis = percentage_change(v1, v2)

    return (result_income_analysis)


def sp500_analysis(sym):
    rpaa = price_action_analysis(sym)
    ria = income_analysis(sym)
    r = []
    r.append(sym)
    r.append(rpaa)
    r.append(ria)

    return (r)


master_analysis_list = []

test = sp500_analysis("AAPL")

print(test)

# need to code in detection for net income in order to perform analysis; the position of net income differs across symbols

# need to code in storage logic
# is it as simple as appending a list to an empty list?
