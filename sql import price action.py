import json
import pymysql.cursors


def create_table(live_schema, table_title):
    con1 = pymysql.connect(host="localhost",
                           user="jefferson",
                           passwd="1234",
                           db=live_schema)
    with con1.cursor() as cursor1:
        create_table_command = "CREATE TABLE " + table_title + "(id INT       AUTO_INCREMENT PRIMARY KEY)"
        cursor1.execute(create_table_command)
    con1.close()
# CREATED A COL W/ TITLE


def new_col(live_schema, live_table, new_column):
    con2 = pymysql.connect(host="localhost",
                           user="jefferson",
                           passwd="1234",
                           db=live_schema)
    with con2.cursor() as cursor2:
        # create new columns
        new_col_command = "ALTER TABLE `" + live_table + "` ADD `" + new_column + "` TEXT(100);"
        print(new_col_command)
        cursor2.execute(new_col_command)
    con2.close()


def new_row(live_schema, live_table, live_column, title_row):
    # def new_row(title_row):
    con3 = pymysql.connect(host="localhost",
                           user="jefferson",
                           passwd="1234",
                           db=live_schema)
    with con3.cursor() as cursor3:
        # create new rows
        # ini = []
        val = title_row
        new_row_command = "INSERT INTO `" + live_table + "` (`" + live_column + "`) VALUES  (%s) "
        # new_row_command_ini = "INSERT INTO `" + live_table + "` (`" + live_column + "`) VALUES (%s);"
        # ini.append(new_row_command_ini)
        # print(ini[0])
        # new_row_command = "INSERT INTO `tabletable` (`Statement`)VALUES(%s)"
        # test = "INSERT INTO `spy20190828` (`daydate`, `daytime`, `open_price`, `high_price`, `low_price`, `close_price`, `volume`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor3.execute(new_row_command, val)
        con3.commit()
    con3.close()
# good for entering initial column cell values. if applied to a populated table:
# id / newcol               / newcol2
# 1  /   x                  / NULL
# 2  /  new_row(title_row)  / NULL
# 3  /  NULL                / new_row(title_row)


# UPDATE `sp500`.`aapl_income_statement_master` SET `OperatingRevenue` = 'q' WHERE (`id` = '1');
def new_v(live_schema, live_table, live_column, value_d, id):
    con4 = pymysql.connect(host="localhost",
                           user="jefferson",
                           passwd="1234",
                           db=live_schema)
    with con4.cursor() as cursor4:
        # create new rows
        new_v_command = "UPDATE `" + live_table + "` SET `" + live_column + "` = '" + value_d + "' WHERE (`id` = '" + id + "');"
        cursor4.execute(new_v_command)
        con4.commit()
    con4.close()


def new_row_price_action_values(live_schema, live_table, list_of_val):
    con5 = pymysql.connect(host="localhost",
                           user="jefferson",
                           passwd="1234",
                           db=live_schema)
    with con5.cursor() as cursor5:
        # create new columns
        new_col_command = "INSERT INTO `" + live_table + "` (`date`, `open`, `high`, `low`, `close`, `volume`) VALUES  (%s, %s, %s, %s, %s, %s);"
        cursor5.execute(new_col_command, list_of_val)
        con5.commit()
    con5.close()


def table_template_price_action(live_schema, live_table):
    new_col(live_schema, live_table, "date")
    new_col(live_schema, live_table, "open")
    new_col(live_schema, live_table, "high")
    new_col(live_schema, live_table, "low")
    new_col(live_schema, live_table, "close")
    new_col(live_schema, live_table, "volume")


def build_list_of_list(list_mk1):
    len_list = len(list_mk1)
    ready_list = [[] for i in range(len_list)]
    return ready_list


def append_price_action_values(array_key, date):
    master[array_key].append(date_list[array_key])
    master[array_key].append(data["Time Series (Daily)"][date]["1. open"])
    master[array_key].append(data["Time Series (Daily)"][date]["2. high"])
    master[array_key].append(data["Time Series (Daily)"][date]["3. low"])
    master[array_key].append(data["Time Series (Daily)"][date]["4. close"])
    master[array_key].append(data["Time Series (Daily)"][date]["5. volume"])


symbols = ["AAPL", "AMZN", "BAC", "C", "CMCSA", "CSCO", "CVX", "FB", "GE", "GOOG", "GOOGL", "HD", "INTC", "JNJ", "JPM", 'KO', 'MRK', 'MSFT', 'PFE', 'PG', 'PM', 'T', 'V', 'VZ', 'WFC', 'XOM', 'BRKB', 'UNH', 'DIS', 'PEP', 'MO', 'IBM', 'ORCL', 'AMGN', 'MMM', 'MCD', 'MDT', 'WMT', 'MA', 'ABBV', 'BA', 'HON', 'SLB', 'CELG', 'PCLN', 'BMY', 'UNP', 'AVGO', 'UTX', 'SBUX', 'GILD', 'GS', 'USB', 'CVS', 'AGN', 'QCOM', 'TXN', 'COST', 'LLY', 'ABT', 'ACN', 'LOW', 'UPS', 'WBA', 'NKE', 'CHTR', 'DOW', 'MDLZ', 'DD', 'LMT', 'NFLX', 'ADBE', 'TMO', 'CB', 'CL', 'MS', 'NEE', 'NVDA', 'AXP', 'PNC', 'CAT', 'BIIB', 'COP', 'DUK', 'AIG', 'MET', 'CRM', 'GD', 'PYPL', 'AMT', 'KHC', "SPG", "EOG", "TJX", "DHR", "BK", "SCHW", "SO", "D", "CSX", "ANTM", "BLK", "PRU", "FDX", "OXY", "RTN", "GM", "KMB", "AMAT", "ADP", "F", "ITW", "NOC", "SYK", "CI", "CME", "COF", "HAL", "BDX", "JCI", "KMI", "EMR", "MMC", "CTSH", "ATVI", "BSX", "ICE", "LUV", "BBT", "DAL", "PSX", "SPGI", "ETN", "NSC", "PCG", "TRV", "CCI", "EBAY", "HUM", "AEP", "ECL", "EQIX", "GIS", "DE", "TGT", "HPQ", "AON", "EXC", "APD", "ISRG", "REGN", "ALL", "HPE", "PSA", "MAR", "INTU", "FOXA", "STT", "STZ", "AFL", "VRTX", "WM", "MCK", "ALXN", "VLO", "EA", "MU", "PXD", "STI", "PLD", "PPG", "SRE", "ADI", "ILMN", "ZTS", "FIS", "BAX", "KR", "SHW", "MPC", "LYB", "GLW", "TEL", "SYY", "CCL", "AVB", "PPL", "WDC", "EIX", "ROST", "FISV", "WMB", "WY", "CMI", "MTB", "LRCX", "ED", "ZBH", "HCA", "PCAR", "DFS", "CBS", "ADM", "EQR", "DLPH", "PGR", "EW", "IR", "YUM", "CAH", "ORLY", "XEL", "SYF", "AAL", "VTR", "PEG", "ROP", "APH", "DXC", "NWL", "IP", "PH", "UAL", "SWK", "INCY", "EL", "KEY", "DVN", "AMP", "AZO", "ROK", "MCO", "NTRS", "OMC", "DLTR", "CXO", "NUE", "BXP", "WEC", "FTV", "CERN", "CFG", "DG", "SWKS", "ES", "DTE", "PAYX", "APA", "FITB", "HIG", "RCL", "ADSK", "A", "MNST", "TSN", "DLR", "VFC", "PFG", "NEM", "TROW", "K", "WLTW", "RF", "MYL", "ULTA", "VMC", "CLX", "EXPE", "TAP", "EFX", "ESS", "MCHP", "VNO", "FCX", "O", "KLAC", "CAG", "XLNX", "MLM", "HSY", "LNC", "DGX", "BEN", "SJM", "XRAY", "FTI", "MHK", "RSG", "HBAN", "LH", "ADS", "MSI", "IDXX", "CTL", "BBY", "AWK", "HSIC", "ETR", "WHR", "WAT", "VIAB", "FOX", "NBL", "CMG", "DISH", "AME", "NLSN", "GPC", "CTXS", "ABC", "WRK", "HST", "MTD", "BLL", "FAST", "AEE", "IVZ", "L", "CNC", "NOV", "FE", "CMA", "CMS", "LB", "HES", "TXT", "MRO", "CHD", "HOLX", "STX", "GPN", "TDG", "ALB", "DOV", "CNP", "ARNC", "VRSK", "MAS", "COG", "JNPR", "EMN", "XEC", "MKC", "HAS", "SNPS", "MAA", "OKE", "DHI", "UHS", "IFF", "CPB", "KMX", "DRI", "NTAP", "PNR", "ALK", "UNM", "CINF", "SLG", "CTAS", "AAP", "CHRW", "PRGO", "GWW", "DVA", "EQT", "IT", "LEN", "FL", "ARE", "ETFC", "COO", "WYNN", "UDR", "TIF", "RJF", "LKQ", "EXPD", "HOG", "AJG", "FBHS", "SNA", "FRT", "FMC", "KSU", "IPG", "PNW", "HRL", "AKAM", "REG", "WU", "EXR", "URI", "XYL", "LNT", "GT", "AMG", "M", "SEE", "QRVO", "KIM", "VAR", "COTY", "IRM", "MOS", "BWA", "FFIV", "TSCO", "ZION", "AMD", "VRSN", "NDAQ", "PVH", "JBHT", "HBI", "NI", "AYI", "AVY", "CBOE", "MAC", "ALLE", "AES", "MAT", "SRCL", "FLR", "LEG", "KSS", "JEC", "HP", "FLS", "PKI", "PHM", "XRX", "PBCT", "CF", "RHI", "GRMN", "AIZ", "JWN", "GPS", "DISCK", "BBBY", "TGNA", "PWR", "HRB", "TRIP", "FLIR", "RRC", "NWSA", "NRG", "MNK", "SIG", "RL", "NAVI", "CHK", "RIG", "MUR", "DISCA", "TDC", "UAA", "PDCO", "R", "UA", "AN", "NWS", "AIV", "BKNG"]

# symbols = ["AAPL", "AMZN"]

for sym in symbols:

    file_title = sym + " daily.json"

    sql_title = sym + "_price_action"

    # rotation = ["1. open", "2. high", "3. low", "4. close", "5. volume"]

    # eventually wrap this in a loop, iterating over the symbols
    with open(file_title) as f:
        data = json.load(f)
        # # #
        # SCRAP CODE
        # for d in data.items():
        #     print(d[0])  # First Branch # Meta Data // Time Series (Daily)
        # #     # print(d[1]) # Second Branch #
        # for d in data.values():
        #     # print(d)  # second branch
        #     print(d[0])  # KeyError
        # print(data["Time Series (Daily)"].keys()) # all dates
        # print(data["2020-01-14"].items())
        # print(data["Time Series (Daily)"]) # a dict of dates and values
        # END OF SCRAP CODE
        # # #

        d = data["Time Series (Daily)"].keys()  # dates

        date_list = []
        for q in d:
            # print(q)
            date_list.append(q)
        master = []
        master = build_list_of_list(date_list)

        for x in range(0, (len(date_list)), 1):
            append_price_action_values(x, date_list[x])

        # for m in master:
        #     print(m)

        f.close()

    # create_table(live_schema, table_title):
    create_table("sp500", sql_title)

    # table_template_price_action(live_schema, live_table):
    table_template_price_action("sp500", sql_title)

    print(len(master))
    for x in range((len(master) - 1), -1, -1):
        # (live_schema, live_table, list_of_val)
        new_row_price_action_values("sp500", sql_title, master[x])

    print("d")
    # for x in dates:
    #     print(x)

    # 500ish files
    # iterate and open
    #     create mysql table; price action
    #     create columns

    #     iterate over the contents of the file
    #     isolate the values

    #     migrate to mysql
    #     migrate packs of data instead of individual cells
    #
    #     build list:

    #     cols in mysql
    #     date / open / high / low / close / volume

    #     list in py:
    #     date, open, high, low, close, volume

    #     isolate values
    #     append values

    #     then build a sql command:
