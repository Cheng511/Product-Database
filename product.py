# coding=utf-8
import mariadb
from pwDB import UseDataBase
import datetime
import tkinter as tk


def InsertProduct(name, web, time_in, time_out):
    dbconfig = {
        "host": "127.0.0.1",
        "user": "jc",
        "password": "0426",
        "database": "productDB",
    }
    try:
        with UseDataBase(dbconfig) as cursor:
            insert_product = """insert into product (品名 , 網站, 借入時間, 預計歸還時間, 實際歸還時間, 上刊時間)
                   values (%s, %s, %s, %s, "", "")"""
            cursor.execute(insert_product, (name, web, time_in, time_out))
    except (Exception, mariadb.Error) as err:
        print(err)


def InsertReturn(name, time):
    dbconfig = {
        "host": "127.0.0.1",
        "user": "jc",
        "password": "0426",
        "database": "productDB",
    }
    try:
        with UseDataBase(dbconfig) as cursor:
            insert_return_time = """ update product set 實際歸還時間 = '""" + \
                time + "'"""" where 品名 =  '""" + name + "'"
            cursor.execute(insert_return_time)
    except (Exception, mariadb.Error) as err:
        print(str(err))


def InsertLaunch(name, time):
    dbconfig = {
        "host": "127.0.0.1",
        "user": "jc",
        "password": "0426",
        "database": "productDB",
    }
    try:
        with UseDataBase(dbconfig) as cursor:
            insert_launch_time = """ update product set 上刊時間 = '""" + \
                time + "'"""" where 品名 =  '""" + name + "'"
            cursor.execute(insert_launch_time)

    except (Exception, mariadb.Error) as err:
        print(str(err))


def Ask():
    print()
    print("="*29)
    print("="*10 + " 想來點？" + "="*10 + "\n"
          "1. 新增產品到資料庫建檔" + "\n"
          "2. 產品歸還" + "\n"
          "3. 新增文章上刊時間" + "\n"
          "4. 離開" + "\n")
    q = input("")
    if q == "1":
        name = str(input("請輸入產品名稱: "))
        web = str(input("請輸入對應網站: "))
        time_in = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        time_out = (datetime.datetime.now()+datetime.timedelta(days=14)
                    ).strftime("%Y-%m-%d %H:%M")
        InsertProduct(name, web, time_in, time_out)
        print("已成功將 " + name + " 建檔，預計 " + time_out + " 歸還")
        Ask()
    elif q == "2":
        name = input("請輸入產品名: ")
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        InsertReturn(name, time)
        print("已確認 " + name + " 歸還時間為 " + time)
        Ask()
    elif q == "3":
        name = input("請輸入產品名: ")
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        InsertLaunch(name, time)
        print("已確認 " + name + " 上刊時間為 " + time)
        Ask()
    elif q == "4":
        print("ByeBye~")
        pass

    else:
        print("錯誤指令")


Ask()
