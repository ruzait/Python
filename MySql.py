import mysql.connector
from tabulate import tabulate


def insert(class_ID,class_name,class_teacher_name):
    cursor = conn.cursor()
    sql = "insert into class_dtls (class_ID,class_name,class_teacher_name) values(%s, %s, %s)"
    user = (class_ID, class_name, class_teacher_name)
    cursor.execute(sql, user)
    conn.commit()
    print("Ahh... \n Ungada DATA Sethaachi ok!!")

def update(class_ID,class_name,class_teacher_name):
    cursor = conn.cursor()
    sql = "update class_dtls set class_name=%s,class_teacher_name=%s where class_ID=%s"
    user = (class_name, class_teacher_name, class_ID)
    cursor.execute(sql, user)
    conn.commit()
    print("Ahh... \n Ungada DATA Mathiyachi ok!!")

def select():
    cursor = conn.cursor()
    sql = "select * from class_dtls"
    cursor.execute(sql)
    result=cursor.fetchall()
    #result=cursor.fetchone()
    #result = cursor.fetchmany(3)
    #print(result)
    print(tabulate(result, headers=("class_ID","class_name","class_teacher_name")))

def delet(class_ID):
    cursor = conn.cursor()
    sql = "delete from class_dtls where class_ID=%s"
    user = (class_ID,)
    cursor.execute(sql, user)
    conn.commit()
    print("Ahh... \n Ungada DATA Delete panniyachi ok!!")


try:
    conn = mysql.connector.connect(host="localhost", port="3306", user="root", password="", database="school")

    while True:
        print("1.Insert")
        print("2.Update")
        print("3.Select")
        print("4.Delete")
        print("0.Exit")
        cho = int(input("Enter your choice: "))

        if cho == 1:
            class_ID = int(input("Enter class id: "))
            class_name = input("Enter class name: ")
            class_teacher_name = input("Enter teacher name: ")
            insert(class_ID, class_name, class_teacher_name)

        elif cho == 2:
            class_ID = int(input("Enter class id: "))
            class_name = input("Enter class name: ")
            class_teacher_name = input("Enter teacher name: ")
            update(class_ID, class_name, class_teacher_name)

        elif cho == 3:
            select()

        elif cho == 4:
            class_ID = int(input("Enter class id: "))
            delet(class_ID)

        elif cho == 0:
            quit()

        else:
            print("Pooda peyaa!!!")
except Exception as e:
    print("\n")
    print("-"*120)
    print("              Oh.! YOU GOT ERROR:", e)
    print("-" * 120)