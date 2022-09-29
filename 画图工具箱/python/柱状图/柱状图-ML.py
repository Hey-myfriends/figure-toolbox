import numpy as np
import matplotlib.pyplot as plt
import scipy.io as scio

sens_D = np.array([83, 66.25, 81.94, 86, 74.6, 90, 92.3, 74.7, 84.1, 84.1, 86]) / 100
sens_P = np.array([72, 83, 94.1, 91.49, 72.7, 85.5]) / 100
spec_D = np.array([87, 95.38, 98.74, 91.7, 48.4, 60, 100, 79.0, 0, 83.4, 81]) / 100
spec_P = np.array([77.2, 67, 97.1, 88.51, 78.9, 86.3]) / 100
label_sens_D = ['*' if num==0.0 else ' ' for num in sens_D]
label_spec_D = ['*' if num==0.0 else ' ' for num in spec_D]
label_sens_P = ['*' if num==0.0 else ' ' for num in sens_P]
label_spec_P = ['*' if num==0.0 else ' ' for num in spec_P]
# print(spec)
# print(label_spec)
xlabel = ['Cole 2011', 'Mazilu 2012(1)', 'Tripoliti 2013', 'Kim 2015', 'Handojoseno 2015', 'Mazilu 2016(2)',
          'Ahlrichs 2016', 'Martin 2017', 'Olmo 2020', 'Reches 2020', 'Diep 2021',
          'Handojoseno 2012', 'Palmerini 2017', 'Demrozi 2019', 'Kleanthous 2020', 'Zhang 2020', 'Borzì 2021']
# xlabel_P = ['Handojoseno 2012', 'Palmerini 2017', 'Demrozi 2019', 'Kleanthous 2020', 'Zhang 2020', 'Borzì 2021']

width = 0.35
color11, color12 = (79/255,89/255,109/255), (243/255,118/255,74/255)
color21, color22 = (66/255,181/255,64/255), (200 / 255, 0 / 255, 0 / 255)
label11, label12 = 'Sensitivity\n(FoG Detection)', 'Specificity\n(FoG Detection)'
label21, label22 = 'Sensitivity\n(FoG Prediction)', 'Specificity\n(FoG Prediction)'
x_D = np.arange(0, sens_D.shape[0])
x_P = np.arange(sens_D.shape[0], sens_D.shape[0]+sens_P.shape[0])
x = np.arange(sens_D.shape[0]+sens_P.shape[0])
fig, ax = plt.subplots(1,1, figsize=(12,27/4))
rect1 = plt.bar(x_D-width/2, sens_D, width, color=color11, edgecolor='w', label=label11)
rect2 = plt.bar(x_D+width/2, spec_D, width, color=color12, edgecolor='w', label=label12)
rect3 = plt.bar(x_P-width/2, sens_P, width, color=color21, edgecolor='w', label=label21)
rect4 = plt.bar(x_P+width/2, spec_P, width, color=color22, edgecolor='w', label=label22)
ax.set_xticks(x)
ax.set_xticklabels(xlabel, rotation=40, fontsize=15)
ylim = np.array([round(num,1) for num in np.arange(0., 1.1, 0.1)])
ax.set_ylim([ylim.min(), ylim.max()])
ax.set_xlim([-0.5, x.max()+0.5])
ax.set_yticks(ylim)
ax.set_yticklabels(['{:}.0%'.format(round(num*100)) for num in np.arange(0., 1.1, 0.1)], fontsize=13)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.grid(axis='y', c='k', alpha=0.3)
plt.bar_label(rect1, labels=label_sens_D, label_type='center', fontsize=25, padding=12)
plt.bar_label(rect2, labels=label_spec_D, label_type='center', fontsize=25, padding=12)
plt.bar_label(rect3, labels=label_sens_P, label_type='center', fontsize=25, padding=12)
plt.bar_label(rect4, labels=label_spec_P, label_type='center', fontsize=25, padding=12)
plt.figlegend(labels=('Sensitivity\n(FoG Detection)','Specificity\n(FoG Detection)', 'Sensitivity\n(FoG Prediction)', 'Specificity\n(FoG Prediction)'),
              loc='center right', ncol=1, bbox_to_anchor=(1.2, 0.5), markerscale=2,
              fontsize=15,labelspacing=3, shadow=False, frameon=False, framealpha=0.5)
# plt.figlegend()
plt.subplots_adjust(left=0, right=1, top=1, bottom=0, wspace=None, hspace=None)
# plt.show()
plt.savefig('ML.tiff', format='tiff', dpi=300, bbox_inches='tight', pad_inches=0)


# metrics_label = ['Accuracy', 'Precision', 'Specificity', 'Sensitivity', 'F1-score', 'Geometric mean']
# idx0 = [0, 1, 2, 3, 4, 5, 6, 7] #
# labels = ['3', '6', '9', '10', '15', '16', '17', '19']

# results = scio.loadmat('.\\results\\results_all_pmEEG.mat')
# res_pmEEG = results['res']
# res_pmEEG_mean, res_pmEEG_std = res_pmEEG.mean(axis=1), res_pmEEG.std(axis=1)
# res_pmEEG_mean = np.r_[res_pmEEG_mean, res_pmEEG_mean.mean(axis=0, keepdims=True)]
# res_pmEEG_std = np.r_[res_pmEEG_std, res_pmEEG_mean.std(axis=0, keepdims=True)]
#
# results = scio.loadmat('.\\results\\results_all_EEG.mat')
# res_EEG = results['res']
# res_EEG_mean, res_EEG_std = res_EEG.mean(axis=1), res_EEG.std(axis=1)
# res_EEG_mean = np.r_[res_EEG_mean, res_EEG_mean.mean(axis=0, keepdims=True)]
# res_EEG_std = np.r_[res_EEG_std, res_EEG_mean.std(axis=0, keepdims=True)]
#
# results = scio.loadmat('.\\results\\results_all_ACC.mat')
# res_ACC = results['res']
# res_ACC_mean, res_ACC_std = res_ACC.mean(axis=1), res_ACC.std(axis=1)
# res_ACC_mean = np.r_[res_ACC_mean, res_ACC_mean.mean(axis=0, keepdims=True)]
# res_ACC_std = np.r_[res_ACC_std, res_ACC_mean.std(axis=0, keepdims=True)]
#
# results = scio.loadmat('.\\results\\results_all_EEGACC.mat')
# res_EEGACC = results['res']
# res_EEGACC_mean, res_EEGACC_std = res_EEGACC.mean(axis=1), res_EEGACC.std(axis=1)
# res_EEGACC_mean = np.r_[res_EEGACC_mean, res_EEGACC_mean.mean(axis=0, keepdims=True)]
# res_EEGACC_std = np.r_[res_EEGACC_std, res_EEGACC_mean.std(axis=0, keepdims=True)]
#
# results = scio.loadmat('.\\results\\results_all_pmEEGACC.mat')
# res_pmEEGACC = results['res']
# res_pmEEGACC_mean, res_pmEEGACC_std = res_pmEEGACC.mean(axis=1), res_pmEEGACC.std(axis=1)
# res_pmEEGACC_mean = np.r_[res_pmEEGACC_mean, res_pmEEGACC_mean.mean(axis=0, keepdims=True)]
# res_pmEEGACC_std = np.r_[res_pmEEGACC_std, res_pmEEGACC_mean.std(axis=0, keepdims=True)]

# width = 0.18
# x = np.arange(res_ACC_mean.shape[0])
# subject = ['Sub.{:d}'.format(i+1) for i in x[:-1]]
# subject.append('Ave.')
# subject[5] += '*'
#
# fig, ax = plt.subplots(2,2, figsize=(12,7))
# count = 0
# for idx in [0,3,4,5]: # 选择哪几个指标绘图
#     i, j = int(count/2), count%2
#     # ax[i, j].bar(x - 2*width, res_pmEEG_mean[:,idx], width, yerr=res_pmEEG_std[:, idx], capsize=1.5,
#     #              edgecolor='w', label='pmEEG', ecolor='gray', color=(70/255,100/255,100/255), hatch='///')
#     # ax[i, j].bar(x - width, res_EEG_mean[:, idx], width, yerr=res_EEG_std[:, idx], capsize=1.5,
#     #              edgecolor='w', label='EEG', ecolor='gray', color=(79/255,89/255,109/255))
#     # ax[i, j].bar(x - 0*width, res_ACC_mean[:, idx], width, yerr=res_ACC_std[:, idx], capsize=1.5,
#     #              edgecolor = 'w', label='ACC', ecolor='gray', color=(243/255,118/255,74/255))
#     # ax[i, j].bar(x + width, res_EEGACC_mean[:, idx], width, yerr=res_EEGACC_std[:, idx], capsize=1.5,
#     #              edgecolor = 'w', label='EEG-ACC', ecolor='gray', color=(66/255,181/255,64/255))
#     # ax[i, j].bar(x + 2*width, res_pmEEGACC_mean[:, idx], width, yerr=res_pmEEGACC_std[:, idx],
#     #              capsize=1.5,edgecolor = 'w', label='pmEEG-ACC', ecolor='gray', color=(230/255,0/255,0/255))
#
#     ax[i, j].bar(x - 2 * width, res_EEG_mean[:, idx], width, yerr=res_EEG_std[:, idx], capsize=1.5,
#                  edgecolor='w', label='EEG', ecolor='gray', color=(70 / 255, 100 / 255, 100 / 255), hatch='///')
#     ax[i, j].bar(x - width, res_ACC_mean[:, idx], width, yerr=res_ACC_std[:, idx], capsize=1.5,
#                  edgecolor='w', label='ACC', ecolor='gray', color=(79 / 255, 89 / 255, 109 / 255))
#     ax[i, j].bar(x - 0 * width, res_EEGACC_mean[:, idx], width, yerr=res_EEGACC_std[:, idx], capsize=1.5,
#                  edgecolor='w', label='EEG-ACC', ecolor='gray', color=(243 / 255, 118 / 255, 74 / 255))
#     ax[i, j].bar(x + width, res_pmEEG_mean[:,idx], width, yerr=res_pmEEG_std[:, idx], capsize=1.5,
#                  edgecolor='w', label='pmEEG', ecolor='gray', color=(66 / 255, 181 / 255, 64 / 255))
#     ax[i, j].bar(x + 2 * width, res_pmEEGACC_mean[:, idx], width, yerr=res_pmEEGACC_std[:, idx],
#                  capsize=1.5, edgecolor='w', label='pmEEG-ACC', ecolor='gray', color=(230 / 255, 0 / 255, 0 / 255))
#
#     ax[i, j].set_ylabel(metrics_label[idx] + '(%)', fontsize=10)
#     # ax[i, j].set_xlabel('Subject', loc='right')
#     ax[i, j].set_xticks(x)
#     # ax[i, j].set_xticklabels(labels)
#     ax[i, j].set_xticklabels(subject)
#     ylim = np.array([round(num,1) for num in np.arange(0., 1.1, 0.2)])
#     ax[i, j].set_ylim([ylim.min(), ylim.max()])
#     ax[i, j].set_xlim([-0.5, x.max()+0.5])
#     ax[i, j].set_yticks(ylim)
#     ax[i, j].set_yticklabels(['{:}'.format(round(num*100)) for num in np.arange(0., 1.1, 0.2)])
#     ax[i, j].spines['right'].set_visible(False)
#     ax[i, j].spines['left'].set_visible(False)
#     ax[i, j].spines['top'].set_visible(False)
#     ax[i, j].grid(axis='y', c='k', alpha=0.3)
#     # if count <= 1:
#     #     ax[i, j].legend(loc='upper center', ncol=3, bbox_to_anchor=(0.5, 1.15),
#     #                     fontsize=8, labelspacing=2.5, shadow=False, frameon=True, framealpha=1)
#     count = count + 1
# # plt.axis('off')
# plt.figlegend(labels=('EEG','ACC','EEG-ACC','pmEEG','pmEEG-ACC'),
#               loc='upper center', ncol=5, bbox_to_anchor=(0.5, 1.07), markerscale=2,
#               fontsize=10,labelspacing=None, shadow=False, frameon=True, framealpha=1)
# # plt.legend(loc='upper center', ncol=5, bbox_to_anchor=(0.5, 1.15),fontsize=8, labelspacing=2.5, shadow=False, frameon=True, framealpha=1)
# plt.subplots_adjust(left=0, right=1, top=1, bottom=0, wspace=0.11, hspace=0.22)
# # plt.tight_layout()
# plt.savefig('bar4.tiff', format='tiff', dpi=300, bbox_inches='tight', pad_inches=0)
# plt.show()