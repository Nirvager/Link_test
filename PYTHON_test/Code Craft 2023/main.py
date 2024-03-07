"""文件声明 参加2024华为软件精英挑战赛初赛源码
需解决的问题(解决后建议删除)
    1. 三人之间的交流
        个人认为就以在源码中注释的形式进行，风格见下
    2. 源码注释的风格
        首先是正常的代码说明注释，比如下面几行的“定义全局变量”，按照原有的来就行
        然后是上面提到的交流注释，采用姓名+时间+交流内容，比如下面的Robot类中的move函数
        再后来，交流注释经过三人统一后，建议更改为正常的代码注释，不然看着难受
    3. 文件更新
        另开一段注释，建议修改人模仿上面提到的交流注释，比如我现在修改了Init初始化函数中的地图符号读取问题，我可能会在源码更新日志中
    另起一行，写上fmy 3.7 16:19 修改Init函数中的地图符号读取 line110
    这个line100也就是个大概的样子，文档内容更新会使其位移，无需很精确，方便他人寻找就OK了
        同时，文件更新内容如果经过三人统一后，也建议删除无用部分，避免代码看起来很难绷
    
    4. 机器人移动策略 line50
    5. 地图信息的读取和翻译以及机器人如何利用地图信息来移动 line110
    X. To be continued...
    
-------------------------------------------------------------------------------------------
""""""|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
-------------------------------------------------------------------------------------------
源码更新日志
name姓名  time修改时间  content修改内容  position大致修改位置

"""
#------------------------------------------------------------------------------------------

import sys
import random

# 定义全局变量
n = 200  # 地图的尺寸
robot_num = 10  # 机器人的数量
berth_num = 10  # 泊位的数量
N = 210  # 用于创建二维数组时的尺寸，略大于n，可能是为了处理边界情况

# 机器人Robot类定义
class Robot:
    # 初始化机器人的属性：位置、携带的货物、状态、目标泊位的坐标
    def __init__(self, startX=0, startY=0, goods=0, status=0, mbx=0, mby=0):
        self.x = startX
        self.y = startY
        self.goods = goods
        self.status = status
        self.mbx = mbx
        self.mby = mby

    #move 机器人的移动策略
    #ljr 3.7  15:50尝试思路1：尽量往一个泊位靠
    def move(self,direction):
        delta_x = self.x-berth[0].x
        delta_y = self.y-berth[0].y


        # 根据差异的绝对值比较，确定主要的移动方向
        if abs(delta_x) > abs(delta_y) :
            # 如果x方向的差异大于y方向的，优先左右移动
            return 0 if delta_x > 0 else 1
        else:
            # 否则优先上下移动
            return 2 if delta_y > 0 else 3



# 创建机器人实例列表
robot = [Robot() for _ in range(robot_num + 10)]

class Berth:
    # 初始化泊位的属性：位置、运输时间、装载速度
    def __init__(self, x=0, y=0, transport_time=0, loading_speed=0):
        self.x = x
        self.y = y
        self.transport_time = transport_time
        self.loading_speed = loading_speed


# 创建泊位实例列表
berth = [Berth() for _ in range(berth_num + 10)]

# 初始化船的属性：编号、位置、状态
class Boat:
    def __init__(self, num=0, pos=0, status=0):
        self.num = num
        self.pos = pos
        self.status = status

    #go 船装完货离开
    def go(self,berth_id):
        print(1)

    #ship  船选择泊位停靠 策略？
    def ship(self,berth_id):
        print(2)


# 创建船实例列表
boat = [Boat() for _ in range(10)]

# 更多全局变量定义
money = 0  # 赚的钱 the more the better

"""局部讨论和任务书第七页内容显示每一艘船的容量是相等的
所有有一个就行了 故建议删除boat_capacity=[int for _ in range(10)]"""
boat_capacity = 0  # 船的容量
#boat_capacity=[int for _ in range(10)]
id = 0 # 全局及Input函数中代表帧序号 Init函数中代表泊位的ID
ch = [] # 可能用于存储地图信息   可以修改感觉
gds = [[0 for _ in range(N)] for _ in range(N)]  # 存储每个位置的货物信息，0代表没有货物，正数代表有多少价值的货物

def Init():
    # 初始化函数，用于从输入读取初始配置
    # 地图读取
    for i in range(0, n):
        line = input()
        #fmy0307 下述split用于按空格分割输入的一整行符号 但是官方地图文件符号之间没有空格 所以用list(line)代替
        ch.append(list(line))
        #ch.append([c for c in line.split(sep=" ")])
    # 泊位信息
    for i in range(berth_num):
        line = input()  # 从输入中读取一行数据id x y time velocity
        berth_list = [int(c) for c in line.split(sep=" ")]  # 分割整行数据并填入列表
        id = berth_list[0]  # 列表的第一个元素，泊位的ID
        berth[id].x = berth_list[1]  # 第二个元素，泊位对象的x坐标
        berth[id].y = berth_list[2]  # 第三个元素，泊位对象的y坐标
        berth[id].transport_time = berth_list[3]  # 第四个元素，泊位对象的transport_time属性
        berth[id].loading_speed = berth_list[4]  # 第五个元素，泊位对象的loading_speed属性
    boat_capacity = int(input())  # 船的容积，代表能装的最大物品数(与各个物品价值无关)
    okk = input()  # 输入结束时的OK
    print("OK")  #输入结束后给判题器打一个OK手势
    sys.stdout.flush()

# 输入函数，用于在每一"帧"读取新的输入数据并更新系统状态
def Input():
    id, money = map(int, input().split(" "))  # 更新id和money值
    num = int(input())  # 读取一个整数num，表示需要输入的num个新生成的货物的信息
    
    # 读取并更新货物信息
    for i in range(num):
        x, y, val = map(int, input().split())  # 读取信息
        gds[x][y] = val  # (x,y)坐标处生成了一个价值为val的货物
    
    # 读取并更新所有机器人的状态
    for i in range(robot_num):
        # 机器人属性：是否携带货物goods、位置(x,y)以及当前状态status
        robot[i].goods, robot[i].x, robot[i].y, robot[i].status = map(int, input().split())
    
    # 读取并更新所有船只的状态
    for i in range(5):
        # 船只属性：当前状态status和目标泊位的ID pos
        boat[i].status, boat[i].pos = map(int, input().split())
    
    okk = input()  # 输入结束时的OK
    
    return id  # 返回id作为函数的结果 代表当前帧数


# 主程序入口
if __name__ == "__main__":
    Init()  # 调用初始化函数
    for zhen in range(1, 15001): # 主循环，模拟15000帧的运行
        id = Input() # 处理每帧的输入
        print("ship",0,1)
        for i in range(robot_num): # 控制每个机器人随机移动
            print("move", i, robot[i].move())
            print("get", i)
            print("pull",i)
            sys.stdout.flush()
        print("OK")
        sys.stdout.flush()
