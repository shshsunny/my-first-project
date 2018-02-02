# -*- coding: utf-8 -*-
import math
class BinaryHeap:#使用二叉堆实现
    def __init__(self):
        self.heap = []#创建存储的列表
    #其他操作
    def push(self, e):
        self.heap.append(e)#添加到最后一个位置
        if len(self.heap) == 1:#只有一个元素了，不需要重新排列
            return
        e_loc = len(self.heap) - 1
        #按照序号n来算，第n个元素的父节点序号是： (n - 1) // 2
        #开始换位置
        while True:
            if e_loc == 0 or self.heap[(e_loc - 1) // 2] >= e:#已经到达顶端或者父节点不再比e小
                break
            self.heap[(e_loc - 1) // 2], self.heap[e_loc] = e, self.heap[(e_loc - 1) // 2] 
            e_loc = (e_loc - 1) // 2

    def popMax(self):#弹出最大的元素
        if len(self.heap) == 0:#没有元素，直接返回
            return
        Biggest = self.heap[0]#取出最大元素
        e = self.heap[0] = self.heap.pop(-1)#把最小元素放到这个位置上，让它慢慢沉下去
        e_loc = 0#初始化为零，第一个位置
        #开始换位置 按照序号n来算，第n个元素的左子节点和右子节点分别是：2n+1, 2n+2
        if len(self.heap) <= 1:#没有排序的必要
            return Biggest
        while True:
            
            
            #排序
            child_l = self.heap[2*e_loc + 1] if len(self.heap) - 1 >= 2*e_loc + 1 else None#左子节点
            child_r = self.heap[2*e_loc + 2] if len(self.heap) - 1 >= 2*e_loc + 2 else None#右子节点
            if child_l != None and child_r != None:m = max((child_l, child_r, e))#看看三个节点中哪个是最大（如果有节点值相等，就优先考虑不让e换位）
            elif child_l != None and child_r == None:m = max((child_l, e))#看看左子节点与本节点哪个更大
            elif child_l == None and child_r == None:m = e
            #print "eloc-%s | e, %s, l, %s, r, %s, m, %s" %(e_loc, e, child_l, child_r, m)
            if m == e:#e最大，就没有继续下沉的必要了
                break
            elif m == child_l:#左子节点更大，e与l交换位置
                self.heap[2*e_loc + 1], self.heap[e_loc] = e, child_l
                e_loc = 2*e_loc + 1
                
                
            elif m == child_r:#右子节点更大,e与r交换位置
                self.heap[2*e_loc + 2], self.heap[e_loc] = e, child_r
                e_loc = 2*e_loc + 2
            #看看有没有执行下去的必要
            if e_loc >= len(self.heap) - 1:#到最后一个位置，不用继续下沉
                break
        return Biggest
    ######################################
    def __str__(self):
        self.printAsTree()
        return "<BinaryHeap Data: %s; Lines: %s>"%(self.heap, int(math.log(len(self.heap),2) + 1))
    def __repr__(self):
        return "<BinaryHeap %s>"%self.heap
    def printAsTree(self):
        lineNum = 1
        lines = int(math.log(len(self.heap),2) + 1)
        spaceNum = int(2**lines - 1)
        for i in range(1, len(self.heap)+1):
            i -= 1
            for j in range(2**(lineNum - 1), min(len(self.heap), 2**lineNum)):
                print " "*spaceNum,
                print str(self.heap[j - 1]),
                print "" ,
                print " "*spaceNum,
                i+=1
            lineNum += 1
            
            spaceNum = (spaceNum-2)  // 2
            print
            print
    def peak(self):
        return self.heap[0]

a = BinaryHeap()
for i in range(10):
    a.push(i)
print a
a.popMax()
print a
print a.peak()
