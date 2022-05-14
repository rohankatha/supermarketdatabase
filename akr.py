import subprocess as sp
import pymysql
import pymysql.cursors
import tabulate

def option2():
     
     try:
      
        row = {}
        print("Enter departement details ")

        row["DEPARTMENT_ID"] = input("Dep_ID :")
        row["EMPLOYEE_IN_DEPT"] = input("EDep_ID :")
        

        query = "INSERT INTO  DEPARTMENT(DEPARTMENT_ID,EMPLOYEE_IN_DEPT) VALUES('%s', '%s')" % (
            row["DEPARTMENT_ID"], row["EMPLOYEE_IN_DEPT"])

        
        cur.execute(query)
        con.commit()

        

     except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

     return
    
   


def option3():
   
     try:
      
        row = {}
        print("Enter branch  details ")

        row["BRANCH_ID"] = input("B_ID ")
        row["ADDRESS"] = input("ADDRESS ")
        row["EMPLOYEES"] = input("EmpINbranch")
        

        query = "INSERT INTO  BRANCH(BRANCH_ID,ADDRESS,EMPLOYEES) VALUES('%s', '%s' ,'%s')" % (
            row["BRANCH_ID"], row["ADDRESS"],row["EMPLOYEES"])

        
        cur.execute(query)
        con.commit()

        
     except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

     return

def option4():
    try:
      
        row = {}
        print("Enter customer_with_card   details ")

        row["USER_ID"] = input("U_ID  : ")
        row["NAME"] = input("NAME_OF_THE_CUSTOMER :")
        row["RATING"] = input("RATING :")
        row["PRODUCTS"] = input("PRODUCTS : ")
        

        query = "INSERT INTO CUSTOMER_WITH_CARD (USER_ID,NAME,RATING,PRODUCTS) VALUES('%s', '%s' ,'%s','%s')" % (
            row["USER_ID"], row["NAME"],row["RATING"],row["PRODUCTS"])

        
        cur.execute(query)
        con.commit()

        
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return
def option5():
     try:
      
        row = {}
        print("Enter Table details ")
        row["TABLE"] = input("Enter the table :")
        row["ATTRIBUTE"] = input("Enter attribute that you chose to delete :")
        row["ATTRIBUTE_VAL"] = input("Enter attributevalue of the attribute you chose  :")
        query = "DELETE FROM %s WHERE %s = %s" % (row["TABLE"],row["ATTRIBUTE"],row["ATTRIBUTE_VAL"])
        
        cur.execute(query)
        con.commit()

        
     except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)

     return
def option6():
     try:
      
        row = {}
        print("Enter Table details ")
        row["TABLE"] = input("Enter the table :")
        row["ATTRIBUTE"] = input("Enter attribute :")
        row["ATTRIBUTE_VAL"] = input("Enter attributeval :")
        row["CHANG_ATTR"] = input("Which attr you wanna change : ")
        row["ATTR_NEW_VAL"] = input("Enter new value :")
        
        query = "UPDATE  %s  SET %s = '%s'  WHERE %s = %s" % (row["TABLE"],row["CHANG_ATTR"],row["ATTR_NEW_VAL"],row["ATTRIBUTE"],row["ATTRIBUTE_VAL"])
       
        cur.execute(query)
        con.commit()

        
     except Exception as e:
        con.rollback()
        print("Failed to update into database")
        print(">>>>>>>>>>>>>", e)

     return
def option7():
     try:
      
        row = {}
        print("Enter Table details ")
        row["TABLE"] = input("Enter the table :")
        row["ATTRIBUTE"] = input("Enter attribute that you wanna select from :")
        
        query = "SELECT %s FROM %s" % (row["ATTRIBUTE"],row["TABLE"])
        
        cur.execute(query)
        
        
        result = cur.fetchall()
        
        header = result[0].keys()
        rows =  [x.values() for x in result]
        print(tabulate.tabulate(rows, header,tablefmt = 'grid'))
        con.commit()
        
     except Exception as e:
        con.rollback()
        print("Failed to select from database")
        print(">>>>>>>>>>>>>", e)

     return
def option8():
     try:
      
        row = {}
        print("Enter Table details ")
        row["TABLE"] = input("Enter the table :")
        row["ATTRIBUTE"] = input("Enter attribute :")
        row["OPERATION"] = input("Select the operation you wanna perform :")

        query = "SELECT %s(%s) FROM %s " % (row["OPERATION"],row["ATTRIBUTE"], row["TABLE"])
        
        cur.execute(query)
        result = cur.fetchall()
        
        header = result[0].keys()
        rows =  [x.values() for x in result]
        print(tabulate.tabulate(rows, header,tablefmt = 'grid'))

     except Exception as e:
        con.rollback()
        print("Failed to aggrgate into database")
        print(">>>>>>>>>>>>>", e)

     return
def option9():
     try:
      
        row = {}
        row["Table"]  = input("Enter table :")
        row["attintab"] = input("Enter attribute :")
        row["ATTRIBUTE"] = input("Enter text:")
        
        
        query = "SELECT * FROM %s WHERE %s LIKE '%%%s%%'" % (row["Table"],row["attintab"],row["ATTRIBUTE"])
        
        cur.execute(query)
        result = cur.fetchall()
        
        header = result[0].keys()
        rows =  [x.values() for x in result]
        print(tabulate.tabulate(rows, header,tablefmt = 'grid'))
        

     except Exception as e:
        con.rollback()
        print("Failed to search into database")
        print(">>>>>>>>>>>>>", e)

     return
def option10():
     try:
      
        row = {}
        print("Analysis functional requirement satisfied using inner join :")
        
        

        query = "SELECT * FROM PRODUCT INNER JOIN DEPARTMENT ON DEPARTMENT.DEPARTMENT_ID = PRODUCT.PRODUCT_IN_DEPT"
        
        cur.execute(query)
        result = cur.fetchall()
        
        header = result[0].keys()
        rows =  [x.values() for x in result]
        print(tabulate.tabulate(rows, header,tablefmt = 'grid'))
            #print(x)
        
        con.commit()

        

     except Exception as e:
        con.rollback()
        print("Failed to analyse database")
        print(">>>>>>>>>>>>>", e)

     return
def option11():
     try:
      
        row = {}
        row["table"] = input("Enter your table :")
        
        row["attr"]  = input("Enter the attr you want to project :")
        row["input"] = input("Enter your minimum quanity value :")
        
        

        query = "SELECT *  FROM %s WHERE %s >= %s" % (row["table"],row["attr"],row["input"])
        
        cur.execute(query)
        result = cur.fetchall()
        
        header = result[0].keys()
        rows =  [x.values() for x in result]
        print(tabulate.tabulate(rows, header,tablefmt = 'grid'))
            #print(x)
        
        con.commit()

        

     except Exception as e:
        con.rollback()
        print("Failed to project into database")
        print(">>>>>>>>>>>>>", e)

     return
def hireAnEmployee():
    
    try:
        # Takes emplyee details as input
        row = {}
        print("Enter new employee's details: ")
        name = (input("Name (Fname Minit Lname): ")).split(' ')
        row["FNAME"] = name[0]
        row["MINIT"] = name[1]
        row["LNAME"] = name[2]
        row["DOB"] = input("DOB : ")
        row["ADDRESS"] = input("ADDRESS INPUT :")
        row["EMPLOYEE_ID"] = input("Enter Emp id : ")
       
        query = "INSERT INTO EMPLOYEE(FNAME, MINIT, LNAME, DOB,ADDRESS,EMPLOYEE_ID ) VALUES('%s', '%s', '%s', '%s','%s', '%s')" % (
            row["FNAME"], row["MINIT"], row["LNAME"], row["DOB"],row["ADDRESS"],row["EMPLOYEE_ID"])

        
        cur.execute(query)
        con.commit()

       
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return


def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """

    if(ch == 1):
        hireAnEmployee()
    elif(ch == 2):
        option2()
    elif(ch == 3):
        option3()
    elif(ch == 4):
        option4()
    elif(ch == 5):
        option5()
    elif(ch == 6):
        option6()
    elif(ch == 7):
        option7()
    elif(ch == 8):
        option8()
    elif(ch == 9):
        option9()
    elif(ch == 10):
        option10()
    elif(ch == 11):
        option11()
    else:
        print("Error: Invalid Option")


# Global
while(1):
    tmp = sp.call('clear', shell=True)
    
    # Can be skipped if you want to hardcode username and password
    username = input("Username: ")
    password = input("Password: ")

    try:
        # Set db name accordingly which have been create by you
        # Set host to the server's address if you don't want to use local SQL server 
        con = pymysql.connect(host='localhost',
                              port=30306,
                              user="root",
                              password="akr",
                              db='SUPERMARKETS',
                              cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear', shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")

        tmp = input("Enter any key to CONTINUE>")

        with con.cursor() as cur:
            while(1):
                tmp = sp.call('clear', shell=True)
                # Here taking example of Employee Mini-world
                print("1. Hire an employee")  # Hire an Employee
                print("2. Add a department")  # Insert an departement
                print("3. Add a branch to our supermarket")  # Insert a branch of supermarket
                print("4. Add customers data")  # Insert customers data
                print("5. Delete operations ")  # delete query
                print("6. Update operations")  # update query
                print("7. Read and select")  # select query
                print("8. Aggregate operations")  # aggregate query
                print("9. Partial text searching") # search
                print("10. Analysis operation")  # analysis query
                print("11. Project operation")
                print("12. exit option") #project query
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear', shell=True)
                if ch == 12:
                    exit()
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")

    except Exception as e:
        tmp = sp.call('clear', shell=True)
        print(e)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
