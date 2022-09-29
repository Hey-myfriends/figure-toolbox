import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib import font_manager

if __name__ == '__main__':
    my_font = font_manager.FontProperties(fname='C:/Windows/fonts/simkai.ttf', size=12)
    entries = os.listdir('.\weights\\')

    # para = [3, 4, 5, 6, 7, 8] # pre_FoG duration
    para = [2, 6, 10, 13, 17, 20] # window observations
    metr = np.zeros((7, len(para), 10)) # 识别率 预测率 误报率 提前3秒预测率 提前1秒预测率 平均预测时间裕量 平均识别时间裕量
    labels = ['识别率', '预测率', '误报率', '提前3秒预测率', '提前1秒预测率', '平均预测时间裕量', '平均识别时间裕量']
    labels2 = ['DetectionRate-te', '0_te', 'FalseAlarmedRate-te',
               '-3_te', '-1_te', 'mean-Predict-Time(Predicted)', 'mean-Predict-Time(Predicted and Detected)']
    for i, t in enumerate(para):
        # path = '.\weights\EEGNet-loss(3,5,1)-modify-normalize-focalloss-{}\\'.format(t)
        path = '.\weights\EEGNet-loss(3,5,1)-modify-normalize-focalloss-observation-{}\\'.format(t)
        files = os.listdir(path)
        for file in files:
            if file[-4:] != 'xlsx':
                continue
            metrics = pd.read_excel(io=path+file)
            for j, name in enumerate(labels2):
                metr[j, i] = np.array(metrics[name][:-2])

    # figure
    metr_mean, metr_std = metr.mean(axis=-1), metr.std(axis=-1)
    # fig, ax = plt.subplots(1, 4, figsize=(16, 7))
    fig = plt.figure(figsize=(16, 7))
    style = ['//', '.', '', '', '\\\\', '']
    color = ['lightgray', 'gold', 'darkviolet', 'g', 'skyblue', 'black']
    width, r, x = 0.14, [-2.5, -1.5, -0.5, 0.5, 1.5, 2.5], np.arange(1, 3)
    ax = plt.axes([0.04, 0.05, 0.2, 0.9])
    for i in range(len(para)):
        plt.bar(x+r[i]*width, metr_mean[:2, i], width, yerr=metr_std[:2, i], ecolor='gray', capsize=4,
                  label='{} s'.format(para[0]), color=color[i], hatch=style[i], edgecolor='k')
    ax.set(ylim=[55, 102])
    plt.ylabel('%', fontsize=15, rotation=0)
    plt.yticks(ticks=[60, 70, 80, 90, 100], fontsize=12)
    plt.xticks(ticks=[1, 2], labels=['识别率', '预测率'], font_properties=my_font, rotation=0, fontsize=20)

    ax = plt.axes([0.28, 0.05, 0.12, 0.9])
    for i in range(len(para)):
        plt.bar(r[i]*width, metr_mean[2, i], width, yerr=metr_std[2, i], ecolor='gray', capsize=4,
                  label='{} s'.format(para[0]), color=color[i], hatch=style[i], edgecolor='k')
    ax.set(ylim=[0, 42], xlim=[-0.55, 0.55])
    plt.ylabel('%', fontsize=15, rotation=0)
    plt.yticks(ticks=[0, 5, 10, 15, 25, 35, 40], fontsize=12)
    plt.xticks(ticks=[0], labels=['误报率'], font_properties=my_font, rotation=0, fontsize=20)

    ax = plt.axes([0.45, 0.05, 0.2, 0.9])
    for i in range(len(para)):
        plt.bar(x+r[i]*width, metr_mean[3:5, i], width, yerr=metr_std[3:5, i], ecolor='gray', capsize=4,
                  label='{} s'.format(para[0]), color=color[i], hatch=style[i], edgecolor='k')
    plt.ylabel('%', fontsize=15, rotation=0)
    plt.yticks(fontsize=12)
    plt.xticks(ticks=[1, 2], labels=['提前3秒\n预测率', '提前1秒\n预测率'], font_properties=my_font, rotation=0, fontsize=20)

    ax = plt.axes([0.7, 0.05, 0.2, 0.9])
    for i in range(len(para)):
        plt.bar(x+r[i]*width, metr_mean[5:, i], width, yerr=metr_std[5:, i], ecolor='gray', capsize=4,
                  label='{} s'.format(para[0]), color=color[i], hatch=style[i], edgecolor='k')
    ax.set(ylim=[0, 3.5])
    plt.ylabel('sec', fontsize=15, rotation=0)
    plt.yticks(fontsize=12)
    plt.xticks(ticks=[1, 2], labels=['平均预测\n时间裕量', '平均识别\n时间裕量'], font_properties=my_font, rotation=0, fontsize=20)

    # plt.subplots_adjust(wspace=0.1)
    plt.figlegend(labels=['{}'.format(i) for i in para], loc='right', ncol=1, title='拼接窗口\n数量设定',
                  prop=my_font, title_fontproperties=my_font,
                  fontsize='large', columnspacing=4., labelspacing=2., bbox_to_anchor=(0.97, 0.5))
    # plt.savefig('./compare_Pre-FOG.png', dpi=300, bbox_inches='tight')
    plt.savefig('./compare_observations.png', dpi=300, bbox_inches='tight')

    # for i in range(metr.shape[0]):
    #     metr_now = metr[i]
    #     if i < 2:
    #         # ax[0].bar()
    #         ax[0].errorbar(np.arange(metr.shape[1]), metr_now.mean(axis=-1), yerr=metr_now.std(axis=-1), linestyle=style[i],
    #                        fmt='o', color=linecolor[i], ecolor='gray', elinewidth=2, capsize=4, label=labels[i])
    #     elif i == 2:
    #         pass
    #     elif 2 < i < 5:
    #         pass
    #     else:
    #         ax[1].errorbar(np.arange(metr.shape[1]), metr_now.mean(axis=-1), yerr=metr_now.std(axis=-1), linestyle=style[i],
    #                        fmt='o', color=linecolor[i], ecolor='gray', elinewidth=2, capsize=4, label=labels[i])
    # ax[0].set_xlabel('冻结前期时长(sec)', fontproperties=my_font, fontsize=13)
    # ax[0].set_ylabel('%', fontsize=13)
    # ax[0].set(xticks=list(range(len(para))), xticklabels=para)
    # ax[1].set_xlabel('冻结前期时长(sec)', fontproperties=my_font, fontsize=13)
    # ax[1].set_ylabel('sec', fontsize=13)
    # ax[1].set(xticks=list(range(len(para))), xticklabels=para)
    # ax[0].legend(loc='upper right', prop=my_font)
    # ax[1].legend(loc='upper right', prop=my_font)
    # plt.subplots_adjust(wspace=0.1)
    # plt.savefig('./compare_Pre-FOG.png', dpi=300, bbox_inches='tight')