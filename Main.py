import pymysql as pms
from datetime import datetime as dt
password = ""
username = ""
connected = False
while not connected:
    username = input("enter username:")
    password = input("enter password:")
    c = pms.connect(host="localhost",port=3306,user="yodi555",password="yodi654",db="pybank")
    cu = c.cursor()
    cu.execute("select * from users")
    u = cu.fetchall()
    cu.close()
    c.close()
    for a in u:
        if a[1] == username and a[2] == password:
            connected = True
    if not connected:
        print("user not existed")
print("you success connected")
while True:
    action = input("enter an action:")
    if action == "withdraw":
        c = input("enter customer id:")
        wm = int(input("enter the amount of money to withdraw:"))
        co = pms.connect(host="localhost",port=3306,user="yodi555",password="yodi654",db="pybank")
        cu = co.cursor()
        cu.execute("select money from customers_mode where id=" + c)
        mo = cu.fetchall()
        m = int(mo[0][0])
        nm = m - wm
        cu.execute("update customers_mode set money = %s where id=%s",(nm,c))
        now = dt.now()
        cu.execute("insert into actions values(%s,%s,%s)",(c,"withdraw", now.strftime("%y-%m-%d")))
        cu.close()
        co.commit()
        co.close()
    elif action == "deposit":
        c = input("enter customer id:")
        wm = int(input("enter the amount of money to deposit:"))
        co = pms.connect(host="localhost", port=3306, user="yodi555", password="yodi654", db="pybank")
        cu = co.cursor()
        cu.execute("select money from customers_mode where id=" + c)
        mo = cu.fetchall()
        m = int(mo[0][0])
        nm = m + wm
        cu.execute("update customers_mode set money = %s where id=%s", (nm, c))
        now = dt.now()
        cu.execute("insert into actions values(%s,%s,%s)", (c, "deposit", now.strftime("%y-%m-%d")))
        cu.close()
        co.commit()
        co.close()
    elif action == "actions":
        c = input("enter customer id:")
        co = pms.connect(host="localhost", port=3306, user="yodi555", password="yodi654", db="pybank")
        cu = co.cursor()
        cu.execute("select action,date from actions where id = " + c)
        a = cu.fetchall()
        cu.close()
        co.close()
        for ac in a:
            print("action:",ac[0],"\ndate:",ac[1],"\n")
    elif action == "exit":
        break
    else:
        print("please enter a valid action")


