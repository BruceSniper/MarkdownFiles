#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Bruce Zhang
'''
演示反恐精英加强版案例
对三个匪徒
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

----------------------- 修复版 --------------------------------
9.修复英雄的信息显示模式
    状态描述 0 - 1 - 70 - 99 - 100

10.修复生命值为负的问题
    射击值如果生命值 < 伤害值， 生命值 = 0，否则正常减life

----------------------- 加强版 --------------------------------
11.创建三个恐怖分子对象
    三个对象都要开枪，三个对象都要打印状态
12.修复结束条件为三个恐怖分子都死亡
    三个满足同时死亡
13.解决向三个恐怖分子开枪的问题
    随机数：random
    步骤1：使用random    import random
    步骤2：使用random.randint(1,3) 可以产生1到3的随机数
    产生一个随机数，判断是几就向几号敌人开枪

'''



import random
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
        if p.life <= damage:
            p.life = 0
        else:
            p.life -= damage

    def __str__(self):
        state = ""
        if self.life == 100:
            state = "无伤"
        elif self.life >= 70 and self.life < 100:
            state = "轻伤"
        elif self.life >= 1 and self.life < 70:
            state = "重伤"
        elif self.life <= 0:
            state = "挂了"
        return "%s当前的状态为：%s" % (self.name, state)

class Is(Person):
    def fire(self, p):
        damage = 1
        print("%s向%s开枪，造成了%d伤害" % (self.name, p.name, damage))
        if p.life <= damage:
            p.life = 0
        else:
            p.life -= damage


def main():
    h = Hero("【英雄】")
    is1 = Is("【不要命】")
    is2 = Is("【不怕死】")
    is3 = Is("【还有谁】")
    while True:
        # 产生1到3的随机数
        x = random.randint(1, 3)
        if x == 1:
            h.fire(is1)
        elif x == 2:
            h.fire(is2)
        else:
            h.fire(is3)

        is1.fire(h)
        is2.fire(h)
        is3.fire(h)
        print(h)
        print(is1)
        print(is2)
        print(is3)
        # 设置结束条件
        if h.life <= 0:
            print("%s死亡，枪战结束" % h.name)
            break

        if is1.life <= 0 and is2.life <= 0 and is3.life <= 0:
            print("所有恐怖分子全部死亡，枪战结束")
            break

main()