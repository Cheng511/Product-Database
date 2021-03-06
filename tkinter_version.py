# coding=utf-8
import mariadb
from pwDB import UseDataBase
import datetime
from tkinter import *

root = Tk()
root.title("產品資料庫")
root.geometry("300x300")


def Insert():
    # 加入新產品名稱、對應網站和借入時間，預計歸還時間自動定在2個禮拜後
    name = p_name.get()
    web = web_name.get()
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    future = (datetime.datetime.now()+datetime.timedelta(days=14)
              ).strftime("%Y-%m-%d %H:%M")
    conn = mariadb.connect(host="127.0.0.1", user="jc",
                           password="0426", database="productDB")
    cursor = conn.cursor()
    insert = """insert into product (品名 , 網站, 借入時間, 預計歸還時間)
                   values (%s, %s, %s, %s )"""
    cursor.execute(insert, (name, web, time, future))
    cursor.execute("commit")
    p_name.delete(0, "end")
    web_name.delete(0, "end")
    in_time.delete(0, "end")
    future_time.delete(0, "end")
    actual_time.delete(0, "end")
    real_launch_time.delete(0, "end")
    conn.close()


def Return():
    # 對應產品名稱後，將輸入時間更新到資料庫中該產品的實際歸還時間
    name = p_name.get()
    time = actual_time.get()
    conn = mariadb.connect(host="127.0.0.1", user="jc",
                           password="0426", database="productDB")
    cursor = conn.cursor()
    update_return = """update product set 實際歸還時間 = '""" + \
        time + "'"""" where 品名 =  '""" + name + "'"
    cursor.execute(update_return, (time))
    cursor.execute("commit")
    p_name.delete(0, "end")
    web_name.delete(0, "end")
    in_time.delete(0, "end")
    future_time.delete(0, "end")
    actual_time.delete(0, "end")
    real_launch_time.delete(0, "end")
    conn.close()


def Launch():
    # 對應產品名，將現在時間更新到資料庫中該產品的上刊時間
    name = p_name.get()
    time = real_launch_time.get()
    conn = mariadb.connect(host="127.0.0.1", user="jc",
                           password="0426", database="productDB")
    cursor = conn.cursor()
    update_return = """update product set 上刊時間 = '""" + \
        time + "'"""" where 品名 =  '""" + name + "'"
    cursor.execute(update_return, (time))
    cursor.execute("commit")
    p_name.delete(0, "end")
    web_name.delete(0, "end")
    in_time.delete(0, "end")
    future_time.delete(0, "end")
    actual_time.delete(0, "end")
    real_launch_time.delete(0, "end")
    conn.close()


# 建立GUI登記格文字
p_name_label = Label(root, text="產品名稱")
p_name_label.place(x=30, y=30)
web_name_label = Label(root, text="網站")
web_name_label.place(x=30, y=60)
in_time_label = Label(root, text="借入時間")
in_time_label.place(x=30, y=90)
future_time_label = Label(root, text="預計歸還時間")
future_time_label.place(x=30, y=120)
actual_time_label = Label(root, text="實際歸還時間")
actual_time_label.place(x=30, y=150)
real_launch_time_label = Label(root, text="上刊時間")
real_launch_time_label.place(x=30, y=180)

# 建立登記格
p_name = Entry(root, width=30)
p_name.place(x=150, y=30)
web_name = Entry(root, width=30)
web_name.place(x=150, y=60)
in_time = Entry(root, width=30)
in_time.place(x=150, y=90)
future_time = Entry(root, width=30)
future_time.place(x=150, y=120)
actual_time = Entry(root, width=30)
actual_time.place(x=150, y=150)
real_launch_time = Entry(root, width=30)
real_launch_time.place(x=150, y=180)
# 建立GUI按鈕
submit_btn = Button(root, text="加入資料庫", command=Insert)
submit_btn.place(x=20, y=250)
# 建立GUI更新歸還時間按鈕
return_btn = Button(root, text="更新歸還時間", command=Return)
return_btn.place(x=100, y=250)
# 建立GUI更新歸還時間按鈕
launch_btn = Button(root, text="更新上刊時間", command=Launch)
launch_btn.place(x=195, y=250)

root.mainloop()
