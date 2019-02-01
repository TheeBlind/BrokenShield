import sys
import psycopg2
import getpass
from colorama import init
from termcolor import colored
import progressbar
init(strip=not sys.stdout.isatty())  # strip colors if stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format

cprint(figlet_format('brokenshield!'))

shield = """
          ````````````````````````````````    
         /MyyyyyyyyyyyyyyyyyyyyyyyyyyyyydN    
         /M`:yyyyo       /yyyyyyyyyyyys +N    
         :M.+MMMMMd`     `dMMMMMMMMMMMN`oN    
         -M-:MMMMMMm-     `dMMMMMMMmyo/ sm    
         `M/.MMMMMMMM+     `hdyo/--/shh hh    
          ms NMMMMMMMMy      -shNMMMMMy ms    
          ym yMMMMMMMMMd.    `dMMMMMMM+`M/    
          :M.:MMMMMMNdyo-     `dMMMMMM./M.    
           ms mMMN/.:+o`    +yo`hMMMMd yd     
           +N`/MMMd`+MMm-   /MMs`++++-`N+     
            my hMMMm./MMM+   /MMmddmy sm`     
            -M/`mMMMm`:MMMh.  +MMMMN.-M/      
             +N-.mmo.+mMMMMN/  oMMM:`ms       
              +N:`.sNMMMMMMMMy` sN:.my        
               :No`oNMMMMMMMMMm- `:No         
                `ym/`omMMMMMMNy--hd-          
                  .sms:-+yy+:-odh:            
                     :sdhsyhds/`              
                         .`                                                


"""

print(shield)

QUIT_NUM = 0
USERNAME_NUM = 1
E_MAIL_NUM = 2
PASSWORD_NUM = 3
DOMAIN_NUM = 4
NUMERO_NUM = 5
WRITE_FROM_FILE = 6

total_options = 6 + 1



quit_ = False
wrong_answers_counter = 0

def create_table():
    trovata = True

    database_table = input("\n For be sure that the datas that you are going to insert are attendible \n"
                                   " you have to enter the link where you toke them: ")



    print(colored("\n -- CREATE TABLE --", "magenta"))
    columns_list = []
    counter = 1
    column_name = input("\n Insert the {0} Column name: ".format(counter))
    while column_name == "" or column_name == " ":
        column_name = input("\n Insert the {0} Column name: ".format(counter))
    column_type = input("\n Column Type [Text]?: ")
    prymary_key = input("\n Primary key [False]? <F/T>: ")
    not_null = input("\n Not null [False]? <F/T>: ")

    if column_type == " " or column_type == "":
        columns_list.append([column_name + " text"])
    else:
        columns_list.append([column_name + " " + column_type])

    if not_null.upper() == "TRUE" or not_null.upper() == "T":
        columns_list[len(columns_list) - 1].append(" not null")
    if prymary_key.upper() == "TRUE" or prymary_key.upper() == "T":
        columns_list[len(columns_list) - 1].append(" primary key")

    print(colored("[END] ", "red"), end="")
    quit = input(" do you need other columns? <Y/N>: ")

    while not (quit.upper() == "NO" or quit.upper() == "N"):
        counter += 1
        column_name = input("\n Insert the {0} Column name: ".format(counter))
        while column_name == "" or column_name == " ":
            column_name = input("\n Insert the {0} Column name: ".format(counter))
        column_type = input("\n Column Type? [Text]: ")
        prymary_key = input("\n Primary key? [False] <F/T>: ")
        not_null = input("\n Not null? [False] <F/T>: ")

        if column_type == " " or column_type == "":
            columns_list.append([column_name + " text"])
        else:
            columns_list.append([column_name + " " + column_type])

        if not_null.upper() == "TRUE" or not_null.upper() == "T":
            columns_list[len(columns_list) - 1].append(" not null")
        if prymary_key.upper() == "TRUE" or prymary_key.upper() == "T":
            columns_list[len(columns_list) - 1].append(" primary key")

        print(colored("[END] ", "red"), end="")
        quit = input(" do you need other columns? <y/n>: ")

    confirm = input(" \n Do you confirm the creation of the table? <Y/N>: ")

    if confirm.upper() == "YES" or confirm.upper() == "Y":
        query_string = "("
        for column in range(len(columns_list)):
            if column == len(columns_list) - 1:
                column_string = " ".join(columns_list[column])
                query_string += column_string
            else:
                column_string = " ".join(columns_list[column])
                query_string += column_string + ","
        query_string += ")"

        if database_table.isalpha():
            PostgreSQL_select_Query = "create table {0} {1}".format(database_table, query_string)
            print(PostgreSQL_select_Query)
        else:
            PostgreSQL_select_Query = 'create table "{0}" {1}'.format(database_table, query_string)
            print(PostgreSQL_select_Query)
        cursor.execute(PostgreSQL_select_Query)
        connection.commit()

        print(colored("\n Table created", "green"))
    else:
        exit()

    return database_table

def get_table_datas(table_name):

    if table_name.isalpha():
        pass
    else:
        table_name = '"' + table_name + '"'

    print(colored("\n you are now working on the table {0}".format(table_name), "yellow"))
    count_query = 'SELECT COUNT(*) from %s' % table_name
    cursor.execute(count_query)
    count_answer = cursor.fetchall()
    for row in count_answer:
        row = str(row)
        elements = row.strip("()'[],")
    print(colored("\n There are " + str(elements) + " elemets", "green"))

    if table_name.isalpha():
        PostgreSQL_select_Query = \
            """ 
        SELECT COLUMN_NAME
        FROM
            information_schema.COLUMNS
        WHERE
            TABLE_NAME = '{0}';
        """.format(table_name)
    else:
        name = table_name[1:len(table_name)-1]
        PostgreSQL_select_Query = \
            """ 
        SELECT COLUMN_NAME
        FROM
            information_schema.COLUMNS
        WHERE
            TABLE_NAME = '{0}';
        """.format(name)

    cursor.execute(PostgreSQL_select_Query)
    columns_name = cursor.fetchall()
    column_counter = 0
    columns_dict = dict()

    INPUT_STRING = ""
    for column_name in columns_name:
        column_name = str(column_name)
        column_name = column_name.strip("()'[],")
        columns_dict[column_counter] = [column_name.upper(), False]
        column_counter += 1
    columns_dict[len(columns_dict)] = ["WRITE FROM FILE", False]
    columns_dict[len(columns_dict)] = ["CHANGE TABLE", False]
    columns_dict[len(columns_dict)] = ["QUIT", False]


    for key in columns_dict:
        INPUT_STRING += "\n {0}) {1}".format(key, columns_dict[key][0])
    INPUT_STRING += "\n  choice: "
    return table_name, columns_dict, INPUT_STRING

def work_on_table(table_name, main=False):

    table_name, columns_dict, INPUT_STRING = get_table_datas(table_name)

    while not quit_:
        try:
            finish = False
            stop = False
            print("\nSelect what you want to search or press q for quit",
                  colored("[" + table_name + "]", "yellow"), end="")
            option = input(INPUT_STRING)
            try:
                option = int(option)
                columns_dict[option][1] = True
            except Exception:
                for key in columns_dict:
                    stringa = columns_dict[key][0]
                    if stringa == option.upper() or stringa[0] == option.upper():
                        option = key
                        columns_dict[option][1] = True
                        break

            entro = columns_dict[option][1]
            opzione = columns_dict[option][0]

            if entro and opzione == "CHANGE TABLE":
                database_table = input(" Select the table: ")
                if table_name == '"'+database_table+'"' or table_name == database_table:
                    print(colored("\n You are already working on {0}".format(database_table), "red"))
                else:
                    work_on_table(database_table, True)

            elif entro and opzione == "QUIT":
                break

            elif entro and opzione != "" and opzione != "WRITE FROM FILE" and opzione != "QUIT":
                to_find = input("insert what to searc in the column {0}: ".format(opzione))

                PostgreSQL_select_Query = "SELECT FROM {0} WHERE {1} like '{2}'".format(table_name, opzione,
                                                                                            to_find)

                cursor.execute(PostgreSQL_select_Query)
                datas = cursor.fetchall()
                if len(datas) == 0:
                    print(colored("\nNothing found", "red"))
                else:
                    print(colored("I have found this:", "green"))
                    for row in range(len(datas)):
                        username = datas[row][0]
                        domain = datas[row][1]
                        password = datas[row][2]
                        print(colored("\nusername: " + str(username), "blue") + colored(
                            "\ne-mail: " + str(username) + "@" + str(
                                domain), "yellow") + colored("\npassword: " + str(password), "red"))


            elif entro and opzione == "WRITE FROM FILE":
                if main:
                    database_table = create_table()
                    work_on_table(database_table)
                else:
                    bar = progressbar.ProgressBar(maxval=100, \
                                    widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])

                    check_correct_format = input("\nDo you confirm that the file is in this format\n"
                                                 "   <column1>┊<column2>┊<column3>..... ? <Y/N> : ")

                    if check_correct_format.upper() == "Y" or check_correct_format.upper() == "YES":
                        file_path = input("\nWrite your file path: ")
                        list(file_path)
                        for elem in file_path:
                            if elem == "\\":
                                elem = "/"
                        elements_to_insert = []
                        with open(file_path, "r", encoding="utf-8") as file:
                            for line in file.readlines():
                                line = line.strip()
                                if line == "":
                                    continue
                                else:
                                    line = line.split("┊")
                                    for elem in line:
                                        if elem in """ !#$%&'()*+,-./:;<=>?@[]^_`{|}~" """:
                                            line.remove(elem)
                                        elif elem == "\ufeff":
                                            line.remove(elem)
                                        else:
                                            elem = "'" + elem + "'"

                                    elements_to_insert.append(line)
                        print()
                        bar.start()
                        total = 0
                        for row in range(len(elements_to_insert)):
                            PostgreSQL_select_Query = 'INSERT INTO {0} VALUES{1}'.format\
                                (table_name, tuple(elements_to_insert[row]))
                            cursor.execute(PostgreSQL_select_Query)
                            connection.commit()
                            status = (row * 100) / len(elements_to_insert)
                            if status > 1:
                                bar.update(round(status))
                                total += round(status)
                        bar.update(100)
                        print(colored("\nsuccessfully Done", "green"))

                    elif check_correct_format.upper() == "N" or check_correct_format.upper() == "NO":
                        print(colored("\nfor a correct injection of the data in our db the file is required in the"
                                      " following format:\n ┊username┊domain.ccTLD┊password┊"
                                      "\n\nCheck our github ", "red") +
                              colored("https://github.com/TheeBlind/BrokenShield_Project_x  for more info", "blue"))

                    for key in columns_dict:
                        columns_dict[key][1] = False

        except Exception as error:
            print(colored("\n\n\nERROR ---\n\n\n", "red"))
            print(colored(error, "red"))
            print(colored("\n\n\nERROR ---\n\n\n", "red"))




database_host = input(" Insert Host [localhost]: ")
database_name = input(" Insert Database Name [postgres]: ")
database_port = input(" Insert Port [5432]: ")
database_usern_name = input(" Insert User-name [postgres]: ")
database_password = getpass.getpass(" Insert Password: ")

if database_host == "" or database_host == " ":
    database_host = "localhost"

if database_port == "" or database_port == " ":
    database_port = "5432"

if database_name == "" or database_name == " ":
    database_name = "postgres"

if database_usern_name == "" or database_usern_name == " ":
    database_usern_name = "postgres"

try:

    connection = psycopg2.connect(user=database_usern_name,
                                  password=database_password,
                                  host=database_host,
                                  port=database_port,
                                  database=database_name)
    cursor = connection.cursor()

    database_table = input(" Select the table: ")

    work_on_table(database_table, main=True)





except Exception as error:
    print(colored("\n\n\nERROR ---\n\n\n", "red"))
    print(colored(error, "red"))
    print(colored("\n\n\nERROR ---\n\n\n", "red"))
finally:
    # closing database connection.
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
