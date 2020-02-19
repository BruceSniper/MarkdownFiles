#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Bruce Zhang

from pymysql import connect


class JD(object):
    def __init__(self):
        pass

    def show_all_items(self):
        conn = connect(host='localhost', port=3306, user='root', password='1892', database='jing_dong', charset='utf8')
        # 获得Cusor对象
        cursor = conn.cursor()
        sql = "select * from goods;"
        cursor.execute(sql)
        for temp in cursor.fetchall():
            print(temp)
        cursor.close()
        conn.close()

    def show_cates(self):
        conn = connect(host='localhost', port=3306, user='root', password='1892', database='jing_dong', charset='utf8')
        # 获得Cusor对象
        cursor = conn.cursor()
        sql = "select name from goods_cates;"
        cursor.execute(sql)
        for temp in cursor.fetchall():
            print(temp)
        cursor.close()
        conn.close()

    def show_brands(self):
        conn = connect(host='localhost', port=3306, user='root', password='1892', database='jing_dong', charset='utf8')
        # 获得Cusor对象
        cursor = conn.cursor()
        sql = "select name from goods_brands;"
        cursor.execute(sql)
        for temp in cursor.fetchall():
            print(temp)
        cursor.close()
        conn.close()

    def print_menu(self):
        print("------------京东商城-----------")
        print("1:所有的商品")
        print("2:所有的商品分类")
        print("3:所有的品牌分类")
        return input("请输入功能对应的序号：")

    def run(self):
        while True:
            num = self.print_menu()

            if num == "1":
                # 查询所有商品
                self.show_all_items()
            elif num == "2":
                # 查询所有商品分类
                pass
            elif num == "3":
                pass
            else:
                print("请重新输入")

def main():
    jd = JD()
    jd.run

if __name__ == "__main__":
    main()