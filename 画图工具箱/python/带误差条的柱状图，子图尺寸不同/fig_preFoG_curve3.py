import pandas as pd
import numpy as np
import os, pdb
import matplotlib.pyplot as plt
from matplotlib import font_manager

if __name__ == '__main__':
    my_font = font_manager.FontProperties(fname='C:/Windows/fonts/simkai.ttf', size=12)
    entries = os.listdir('.\weights\\')

    # para = [3, 4, 5, 6, 7, 8] # pre_FoG duration
    # para = [2, 6, 10, 13, 17, 20] # window observations
    para = ["ACC", "GYRO", "ACC-GYRO"]
    metr = np.zeros((7, len(para), 10)) # 识别率 预测率 误报率 提前3秒预测率 提前1秒预测率 平均预测时间裕量 平均识别时间裕量
    labels = [r'$M_{dr}$', r'$M_{pr}$', r'$M_{fpr}$', '提前3秒预测率', '提前1秒预测率', '平均预测时间裕量', '平均识别时间裕量']
    labels2 = ['DetectionRate-te', '0_te', 'FalseAlarmedRate-te',
               '-3_te', '-1_te', 'mean-Predict-Time(Predicted)', 'mean-Predict-Time(Predicted and Detected)']
    
    metr_mean = np.array([[98.48,	98.48,	95.45],
                          [89.39,	93.94,	89.39],
                          [33.33,	30.30,  22.73],
                          [75.76,	59.09,	56.06],
                          [80.30,	78.79,	77.27],
                          [10.76,	5.11,	5.84],
                          [9.73,	4.88,	5.47]])

    metr_std  = np.array([[2.14,	2.14,	3.71],
                          [9.34,	2.14,	2.14],
                          [14.05,	15.00,  11.13],
                          [17.54,	12.86,	4.29],
                          [15.00,	10.71,	3.71],
                          [2.45,	0.97,	0.42],
                          [2.67,	1.14,	0.68]])
    # fig, ax = plt.subplots(1, 4, figsize=(16, 7))
    fig = plt.figure(figsize=(16, 7))
    style = ['//', '.', '', '', '\\\\', '']
    color = ['lightgray', 'gold', 'darkviolet', 'g', 'skyblue', 'black']
    # color = ['lightgray', 'g', 'skyblue']
    width, r, x = 0.25, [-2.5, -1.5, -0.5, 0.5, 1.5, 2.5], np.arange(1, 3)
    r = [-1, 0, 1]
    ax = plt.axes([0.04, 0.05, 0.2, 0.9])
    for i in range(len(para)):
        plt.bar(x+r[i]*width, metr_mean[:2, i], width, yerr=metr_std[:2, i], ecolor='gray', capsize=4,
                  label='{} s'.format(para[0]), color=color[i], hatch=style[i], edgecolor='k')
    ax.set(ylim=[79, 102], xlim=[0.2, 2.8])
    plt.ylabel('%', fontsize=15, rotation=0)
    plt.yticks(ticks=[80, 85, 90, 95, 100], fontsize=12)
    plt.xticks(ticks=[1, 2], labels=[r'$\mathrm{M_{dr}}$', r'$\mathrm{M_{pr}}$'], font_properties=my_font, rotation=0, fontsize=20)

    ax = plt.axes([0.28, 0.05, 0.12, 0.9])
    for i in range(len(para)):
        plt.bar(r[i]*width, metr_mean[2, i], width, yerr=metr_std[2, i], ecolor='gray', capsize=4,
                  label='{} s'.format(para[0]), color=color[i], hatch=style[i], edgecolor='k')
    ax.set(ylim=[0, 52], xlim=[-0.8, 0.8])
    plt.ylabel('%', fontsize=15, rotation=0)
    plt.yticks(ticks=[0, 10, 20, 30, 40, 50], fontsize=12)
    plt.xticks(ticks=[0], labels=[r'$\mathrm{M_{fpr}}$'], font_properties=my_font, rotation=0, fontsize=20)

    ax = plt.axes([0.45, 0.05, 0.2, 0.9])
    for i in range(len(para)):
        plt.bar(x+r[i]*width, metr_mean[3:5, i], width, yerr=metr_std[3:5, i], ecolor='gray', capsize=4,
                  label='{} s'.format(para[0]), color=color[i], hatch=style[i], edgecolor='k')
    ax.set(ylim=[30, 102], xlim=[0.2, 2.8])
    plt.ylabel('%', fontsize=15, rotation=0)
    plt.yticks(fontsize=12)
    plt.xticks(ticks=[1, 2], labels=[r'$\mathrm{M_{pr}^3}$', r'$\mathrm{M_{pr}^1}$'], font_properties=my_font, rotation=0, fontsize=20)

    ax = plt.axes([0.7, 0.05, 0.2, 0.9])
    for i in range(len(para)):
        plt.bar(x+r[i]*width, metr_mean[5:, i], width, yerr=metr_std[5:, i], ecolor='gray', capsize=4,
                  label='{} s'.format(para[0]), color=color[i], hatch=style[i], edgecolor='k')
    ax.set(ylim=[3, 13.5], xlim=[0.2, 2.8])
    plt.ylabel('sec', fontsize=15, rotation=0)
    plt.yticks(fontsize=12)
    plt.xticks(ticks=[1, 2], labels=[r'$\mathrm{\hat{T}_{margin}^p}$', r'$\mathrm{\hat{T}_{margin}^d}$'], font_properties=my_font, rotation=0, fontsize=20)

    # plt.subplots_adjust(wspace=0.1)
    plt.figlegend(labels=['{}'.format(i) for i in para], loc='right', ncol=1, title=None,
                  prop=my_font, title_fontproperties=my_font,
                  fontsize=30, columnspacing=4., labelspacing=2., bbox_to_anchor=(0.99, 0.5))
    # plt.savefig('./Fig/compare_Pre-FOG.png', dpi=300, bbox_inches='tight')
    plt.savefig('./Fig/compare_signals.png', dpi=300, bbox_inches='tight')

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