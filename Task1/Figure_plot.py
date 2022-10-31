import numpy as np
import math
import matplotlib.pyplot as plt
import os
from scipy.io import savemat
from scipy.io import loadmat
import seaborn as sns

color_list = sns.color_palette('deep')

# Figures config
config = {
    "font.family":'serif', # sans-serif/serif/cursive/fantasy/monospace
    "font.size": 8, # medium/large/small
    'font.style':'normal', # normal/italic/oblique
    'font.weight':'normal', # bold
    "mathtext.fontset":'cm',# 'cm' (Computer Modern)
    "font.serif": ['Times New Roman'], #
    "axes.unicode_minus": False,# 用来正常显示负号
}
plt.rcParams.update(config)


# # Load teacher accuracy curve
os.chdir('E:/PhD/DIP/ProjectA/Task1/Results')
T_dict = loadmat('accuracy_T.mat')
accuracy_T = T_dict['accuracy_T']
NUM_EPOCHS = T_dict['NUM_EPOCHS']
# plot
plt.figure(dpi=300,figsize=(2.5,2))
plt.plot(range(1,NUM_EPOCHS[0][0]+1),accuracy_T[0],linewidth=1,color = color_list[0])
# plt.title('Test Accuracy (Teacher)',fontsize=8)
plt.xlabel('Epochs',fontsize=8)
plt.ylabel('Accuracy',fontsize=8)
plt.xticks([2,4,6,8,10,12],fontsize=8)
plt.yticks(fontsize=8)
plt.tight_layout(pad=0.2)
plt.savefig('E:/PhD/DIP/ProjectA/Task1/accuracy_T.png',dpi=300)

# Load student from scratch accuracy curve
S_dict = loadmat('accuracy_S.mat')
accuracy_S = S_dict['accuracy_S']
NUM_EPOCHS = S_dict['NUM_EPOCHS']
# Plot
plt.figure(dpi=300,figsize=(2.5,2))
plt.plot(range(1,NUM_EPOCHS[0][0]+1),accuracy_S[0],linewidth=1,color = color_list[0])
plt.xlabel('Epochs',fontsize=8)
plt.ylabel('Accuracy',fontsize=8)
plt.xticks([2,4,6,8,10,12],fontsize=8)
plt.yticks(fontsize=8)
plt.tight_layout(pad=0.2)
plt.savefig('E:/PhD/DIP/ProjectA/Task1/accuracy_S.png',dpi=300)

# Load student + KD accuracy curve
S_KD_dict = loadmat('accuracy_S_KD.mat')
accuracy_S_KD = S_KD_dict['accuracy_S_KD']
NUM_EPOCHS = S_dict['NUM_EPOCHS']
# Plot
plt.figure(dpi=300,figsize=(2.5,2))
plt.plot(range(1,NUM_EPOCHS[0][0]+1),accuracy_S_KD[0],linewidth=1,color = color_list[0])
plt.xlabel('Epochs',fontsize=8)
plt.ylabel('Accuracy',fontsize=8)
plt.xticks([2,4,6,8,10,12],fontsize=8)
plt.yticks(fontsize=8)
plt.tight_layout(pad=0.2)
plt.savefig('E:/PhD/DIP/ProjectA/Task1/accuracy_S_KD.png',dpi=300)

# Load student + Extractive KD accuracy curve
S_EX_dict = loadmat('accuracy_S_EX.mat')
accuracy_S_EX = S_EX_dict['accuracy_S_EX']
NUM_EPOCHS = S_EX_dict['NUM_EPOCHS']
# Plot
plt.figure(dpi=300,figsize=(2.5,2))
plt.plot(range(1,NUM_EPOCHS[0][0]+1),accuracy_S_EX[0],linewidth=1,color = color_list[0])
plt.xlabel('Epochs',fontsize=8)
plt.ylabel('Accuracy',fontsize=8)
plt.xticks([2,4,6,8,10,12],fontsize=8)
plt.yticks(fontsize=8)
plt.tight_layout(pad=0.2)
plt.savefig('E:/PhD/DIP/ProjectA/Task1/accuracy_S_EX.png',dpi=300)

# Plot Teacher, Student with and without KD and Compare
plt.figure(dpi=300,figsize=(2.5,2))
plt.plot(range(1,NUM_EPOCHS[0][0]+1),accuracy_T[0],linewidth=1,color = color_list[0],label='Teacher')
plt.plot(range(1,NUM_EPOCHS[0][0]+1),accuracy_S[0],linewidth=1,color = color_list[1],label='Student without KD')
plt.plot(range(1,NUM_EPOCHS[0][0]+1),accuracy_S_KD[0],linewidth=1,color = color_list[2],label='Student with KD')
plt.plot(range(1,NUM_EPOCHS[0][0]+1),accuracy_S_EX[0],linewidth=1,color = color_list[3],label='Student with KD+')
plt.legend(fontsize=8,frameon=False)
plt.xlabel('Epochs',fontsize=8)
plt.ylabel('Accuracy',fontsize=8)
plt.xticks([2,4,6,8,10,12],fontsize=8)
plt.yticks([95.0,95.5,96.0,96.5,97.0,97.5,98.0,98.5,99.0,99.5],fontsize=8)
plt.tight_layout(pad=0.2)
plt.savefig('E:/PhD/DIP/ProjectA/Task1/accuracy_compare.png',dpi=300)

# Plot Student + KD vs. T (alpha=0.5)
S_KD_dict = loadmat('accuracy_S_KD_vs_Temp.mat')
accuracy_S_KD = S_KD_dict['accuracy_S_KD']
temperatures = S_KD_dict['temperatures']
# Plot
S_KD = plt.figure(dpi=300,figsize=(2.5,2))
# log2_temperatures = [math.log2(x) for x in temperatures]
plt.plot(temperatures[0],accuracy_S_KD[0],linewidth=1,color = color_list[0])
plt.semilogx(base=2)
plt.xlabel('Temperature ($T$)',fontsize=8)
plt.ylabel('Accuracy',fontsize=8)
plt.xticks([1,2,4,8,16,32,64],fontsize=8)
plt.yticks(fontsize=8)
plt.tight_layout(pad=0.2)
plt.savefig('E:/PhD/DIP/ProjectA/Task1/accuracy_S_KD_T.png',dpi=300)


# The accuracies of KD student model over different parameters (T, alpha)
S_KD_T_alpha_dict = loadmat('accuracy_S_KD_vs_Temp_alpha.mat')
accuracy_S_KD_T_alpha = S_KD_T_alpha_dict['accuracy_S_KD_T_alpha']
temperatures = S_KD_T_alpha_dict['temperatures'][0]
alphas = S_KD_T_alpha_dict['alphas'][0]
# Plot
cbar_ticks = [98.0, 98.2, 98.4, 98.6, 98.8, 99.0]
S_EX_Ts = plt.figure(dpi=300,figsize=(3,1.8))
ax = sns.heatmap(accuracy_S_KD_T_alpha,annot=True,fmt=".2f",xticklabels=temperatures,yticklabels=alphas,cmap="Blues",cbar_kws={"ticks": cbar_ticks})
ax.set_xlabel("Temperature ($T$)",fontsize=8)
ax.set_ylabel("Alpha ("+r'$\alpha$'+")",fontsize=8)
# ax.set_title("Test Accuracy (Student+KD) vs. student T and teacher T",fontsize=8)
ax.invert_yaxis()
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)
plt.tight_layout(pad=0.2)
plt.savefig('E:/PhD/DIP/ProjectA/Task1/accuracy_S_KD_vs_Temp_alpha.png',dpi=300)


# The accuracies of extractive KD  student model over different parameters
S_EX_Ts_dict = loadmat('accuracy_S_EX_vs_Temps.mat')
accuracy_S_EX_Ts_Tt = S_EX_Ts_dict['accuracy_S_EX_Ts_Tt']
temperatures = S_EX_Ts_dict['temperatures'][0]
# Plot
cbar_ticks = [97.6, 98.0, 98.4, 98.8, 99.2]
plt.figure(dpi=300,figsize=(3,1.8))
ax = sns.heatmap(accuracy_S_EX_Ts_Tt,annot=True,fmt=".2f",xticklabels=temperatures,yticklabels=temperatures,cmap="Blues",cbar_kws={"ticks": cbar_ticks})
ax.set_xlabel("Teacher temperature ($T$)",fontsize=8)
ax.set_ylabel("Student temperature ($T^S$)",fontsize=8)
# ax.set_title("Test Accuracy (Student+KD) vs. student T and teacher T",fontsize=8)
ax.invert_yaxis()
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)
plt.tight_layout(pad=0.2)
plt.savefig('E:/PhD/DIP/ProjectA/Task1/accuracy_S_EX_vs_Temps.png',dpi=300)


plt.show()