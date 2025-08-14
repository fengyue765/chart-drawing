import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 全局设置（字体、分辨率等）
plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决中文显示问题
plt.rcParams['axes.unicode_minus'] = False   # 解决负号显示问题
plt.rcParams['figure.dpi'] = 100             # 图形分辨率
sns.set_theme(style="whitegrid")             # seaborn 主题

def plot_line():
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    
    plt.figure(figsize=(8, 4))
    plt.plot(x, y1, label="sin(x)", color="red", linestyle="--")
    plt.plot(x, y2, label="cos(x)", color="blue", linewidth=2)
    plt.title("折线图示例")
    plt.xlabel("X轴")
    plt.ylabel("Y轴")
    plt.legend()
    plt.show()

def plot_scatter():
    np.random.seed(42)
    x = np.random.randn(100)
    y = x + np.random.randn(100) * 0.5
    sizes = np.random.randint(10, 100, 100)  # 点的大小
    
    plt.figure(figsize=(8, 4))
    plt.scatter(x, y, s=sizes, c="green", alpha=0.6, edgecolors="black")
    plt.title("散点图（带大小和透明度）")
    plt.xlabel("X值")
    plt.ylabel("Y值")
    plt.show()

def plot_bar():
    labels = ['A', 'B', 'C', 'D']
    values = [15, 30, 45, 10]
    
    plt.figure(figsize=(6, 4))
    bars = plt.bar(labels, values, color=['#FF9999', '#66B2FF', '#99FF99', '#FFCC99'])
    plt.title("柱状图示例")
    plt.xlabel("类别")
    plt.ylabel("数值")
    
    # 添加数值标签
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height, f'{height}', ha='center', va='bottom')
    plt.show()

def plot_histogram():
    data = np.random.randn(1000)
    
    plt.figure(figsize=(8, 4))
    plt.hist(data, bins=30, color="purple", alpha=0.7, edgecolor="black")
    plt.title("直方图（数据分布）")
    plt.xlabel("值区间")
    plt.ylabel("频数")
    plt.show()

def plot_box():
    data = [np.random.normal(0, std, 100) for std in range(1, 4)]
    
    plt.figure(figsize=(8, 4))
    plt.boxplot(data, patch_artist=True, labels=['A组', 'B组', 'C组'])
    plt.title("箱线图（数据分布统计）")
    plt.ylabel("数值范围")
    plt.show()

def plot_pie():
    labels = ['A', 'B', 'C', 'D']
    sizes = [15, 30, 45, 10]
    explode = (0, 0.1, 0, 0)  # 突出第二部分
    
    plt.figure(figsize=(6, 6))
    plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90, colors=['#FF9999', '#66B2FF', '#99FF99', '#FFCC99'])
    plt.title("饼图示例", pad=20)
    plt.axis('equal')  # 保持圆形
    plt.show()

def plot_heatmap():
    data = np.random.rand(5, 5)
    
    plt.figure(figsize=(6, 6))
    sns.heatmap(data, annot=True, cmap="YlGnBu", linewidths=0.5)
    plt.title("热力图（相关性示例）")
    plt.show()

def plot_subplots():
    x = np.linspace(0, 10, 100)
    
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))
    fig.suptitle("多子图示例", fontsize=16)
    
    # 子图1
    axes[0, 0].plot(x, np.sin(x), color="red")
    axes[0, 0].set_title("sin(x)")
    
    # 子图2
    axes[0, 1].scatter(x, np.cos(x), color="blue", alpha=0.5)
    axes[0, 1].set_title("cos(x)")
    
    # 子图3
    axes[1, 0].bar(['A', 'B', 'C'], [3, 7, 2], color="green")
    
    # 子图4
    axes[1, 1].hist(np.random.randn(1000), bins=30, color="purple")
    
    plt.tight_layout()  # 自动调整间距
    plt.show()

if __name__ == "__main__":
    plot_line()
    plot_scatter()
    plot_bar()
    plot_histogram()
    plot_box()
    plot_pie()
    plot_heatmap()
    plot_subplots()

