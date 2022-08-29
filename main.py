import numpy as np
import matplotlib as mpl
import matplotlib.pylab as plt


history = np.zeros(10)
# 全局变量，用于存储每局游戏的的最终积分
plt.rcParams['font.sans-serif'] = ['SimHei']
# plt 库设置使正常显示中文


for i in range(10):
# 10局游戏
    score = 100
    # 初始积分
    score_sum = []
    # 用于存储一局游戏中每次抛投后的新积分
    
    for j in range(200):
    # 最多进行 200 次抛投
        head = np.random.randint(0, 2)
        # 通过随机数模拟硬币正反面，随机数范围为 0 和 1
        # 1 为正面，0 为反面

        if head:
            delta = 10
        else:
            delta = -10

        score += delta
        # 计算新的积分
        score_sum.append(score)
        # 将新的积分通过 append 方法存储在 score_sum 变量里

        if score <= 0:
        # 积分为 0 时结束该局
            break

        if score >= 500:
        # 积分达到 500 后结束该局
            break
    
    print(f"第{i+1}局中每次抛投后的分数:{score_sum}")
    history[i] = score_sum[-1]
    print(f'本局最终成绩:{history[i]}')
    print("\n")
    
    X = range(j+1)
    Y = score_sum

    plt.clf()

    cmp = mpl.colors.ListedColormap(['r','g','b'])
    # 定义了 [0, 1] 区间的浮点数到颜色的映射规则
    norm = mpl.colors.BoundaryNorm([-1, 5, 495, 1000], cmp.N)
    # 定义了变量值到 [0, 1] 区间的映射规则
    plt.scatter(X, Y, c=Y, cmap=cmp, norm=norm, alpha=0.7)
    # 绘制散点图

    plt.xlabel('次数')
    plt.ylabel('积分')
    plt.title(f'第{i+1}局中每次抛投后的累计分数(本局抛投{j+1}次)')
    
    plt.savefig(f'第{i+1}局抛投累计分数.png', dpi=600)
    # 保存图片为 .png 格式


print(f"10局游戏的历史分数:{history}")
num = np.sum(history >= 500)
print(f"10局游戏后积分达到预期目标(500)的次数:{num}")