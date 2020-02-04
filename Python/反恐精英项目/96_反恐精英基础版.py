#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Bruce Zhang
'''
演示反恐精英案例
对一个匪徒
分析：
1.定义人类，描述公共属性 life：100 name：姓名 要传参
2.定义出英雄与恐怖分子类
3.定义主函数描述枪战过程 main, 创建两个对象
4.定义开枪方法，分成两个方法，Hero Is 都有
    定义的方法要传入被射击的对象
    被射击对象的生命值要进行减少
5.主程序中调用开枪操作
6.开枪操作后，要在主程序中显示每个人的状态信息
7.定义Person类的__str__方法，用于显示每个人的状态
8.设置开枪操作为反复操作
    再设置停止条件：一方生命值<=0
    停止循环使用break
'''

class Person:
    def __init__(self, name):
        self.name = name
        self.life = 100

    def __str__(self):
        return "%s当前的生命值为：%d" % (self.name, self.life)


class Hero(Person):
    def fire(self, p):
        damage = 40
        print("%s向%s开枪，造成了%d伤害" % (self.name, p.name, damage))
        p.life -= damage

class Is(Person):
    def fire(self, p):
        damage = 10
        print("%s向%s开枪，造成了%d伤害" % (self.name, p.name, damage))
        p.life -= damage

def main():
    h = Hero("【英雄】")
    is1 = Is("【不要命】")

    while True:
        h.fire(is1)
        is1.fire(h)
        print(h)
        print(is1)
        # 设置结束条件
        if h.life <= 0:
            print("%s死亡，枪战结束" % h.name)
            break

        if is1.life <= 0:
            print("所有恐怖分子全部死亡，枪战结束")
            break

main()