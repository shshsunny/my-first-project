# -*- coding: utf-8 -*-
import math
class BinaryHeap:#使用二叉堆实现
    def __init__(self):
        self.heap = []#创建存储的列表
    #其他操作
    def push(self, e):
        self.append(e)#添加到最后一个位置
        if self.DonotNeedReplace():#只有一个元素了，不需要重新排列
            return
        e_loc = len(self.heap) - 1#初始化e的位置：最末尾
        #按照序号n来算，第n个元素的父节点序号是： (n - 1) // 2
        #开始换位置
        while self.NeedPopUp(e_loc, e):#需要换位时
            self.SwitchPos(pos1 = self.Parent(e_loc), pos2 = e_loc, value1 = e, value2 = self.ParentValue(e_loc))#往上交换
            
            e_loc = self.Parent(e_loc)#重新设定e的位置
    def popMax(self):#弹出最大的元素
        if self.DonotNeedReplace():#没有元素，直接返回
            return
        Biggest = self[0]#取出最大元素
        e = self.SetMinToMax()#把最小元素放到这个位置上，让它慢慢沉下去
        e_loc = 0#初始化为零，第一个位置
        #开始换位置 按照序号n来算，第n个元素的左子节点和右子节点分别是：2n+1, 2n+2
        if self.DonotNeedReplace():#没有排序的必要
            return Biggest
        while e_loc < len(self.heap) - 1:#只有还没沉底的时候才会继续下沉
            child_l, child_r = self.ChildrenValue(e_loc)#获取子节点的值
            m = self.MaxThreeNodes(e, child_l, child_r)#获取最大的节点值
            if m == e:#e最大，就没有继续下沉的必要了
                break
            elif m == child_l:#左子节点更大，e与l交换位置
                self.SwitchPos(self.Children(e_loc)[0], e_loc, e, child_l)#换位置
                e_loc = self.Children(e_loc)[0]#变成自己左子节点的子节点
                
                
            elif m == child_r:#右子节点更大,e与r交换位置
                self.SwitchPos(self.Children(e_loc)[1], e_loc, e, child_r)#换位置
                e_loc = self.Children(e_loc)[1]#变成自己右子节点的子节点
        return Biggest
    ######################################特殊方法定义
    def __str__(self):
        return "<BinaryHeap Data: %s; Lines: %s>"%(self.heap, int(math.log(len(self.heap),2) + 1))
    def __repr__(self):
        return "<BinaryHeap Data: %s; Lines: %s>"%(self.heap, int(math.log(len(self.heap),2) + 1))
    def __getitem__(self, pos):
        return self.heap[pos]
    def __setitem__(self, pos, item):
        self.heap[pos] = item
    def __len__(self):
        return len(self.heap)
    #########
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

    #------------------子算法方法区
    def append(self, e):
        self.heap.append(e)
    def DonotNeedReplace(self):#适用于push和popMax，判断需不需要进行移位
        return len(self.heap) <= 1#只有有两个及以上元素时，才有换位的可能性
    def NeedPopUp(self, e_loc, e):#适用于push，看看需不需要继续让e上浮
        return e_loc > 0 and self[self.Parent(e_loc)] < e#只有e没有到达顶端且父节点比自己小的时候，才能继续上浮
    def SwitchPos(self, pos1, pos2, value1, value2):#换位置
        self[pos1], self[pos2] = value1, value2
    def Parent(self, e_loc):#计算一个序号位的父节点
        return (e_loc - 1) // 2 if e_loc > 0 else None#如果不是顶端，返回父节点位置，否则返回None
    def ParentValue(self, e_loc):
        return self[(e_loc - 1) // 2] if e_loc > 0 else None#如果不是顶端，返回父节点，否则返回None
    def Children(self, e_loc):#获取两个子节点的位置
        child_l = 2*e_loc + 1
        child_r = 2*e_loc + 2
        return child_l ,child_r
    def ChildrenValue(self, e_loc):#获取两个子节点的值（如果没有子节点，将以None值代替）
        child_l = self[2*e_loc + 1] if len(self) - 1 >= 2*e_loc + 1 else None#左子节点
        child_r = self[2*e_loc + 2] if len(self) - 1 >= 2*e_loc + 2 else None#右子节点
        return child_l, child_r
    def SetMinToMax(self):
        e = self.heap.pop()#取出最小的元素
        self[0] = e#同时将e的值赋予第一位元素（根节点）
        return e
    def MaxThreeNodes(self, node1, node2, node3):#在父节点和两个子节点中选出最大的节点（可以处理子节点无值情况）可以直接使用max()，因为 0 > None 且max支持此功能
        return max(node1, node2, node3)
#-------test-------#
a = BinaryHeap()
for i in range(10):
    a.push(i)
print a
a.popMax()
print a
print a.peak()
a.printAsTree()
