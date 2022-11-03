# ECE1512_2022F_ProjectRepo_HaoxiangNing_YitianLiu
## About this Repository
This project contains two main tasks. In the Project folder, you will find two folders for two tasks. In each folder, you will find the .ipynb file for detailed outputs and codes. Besides that, these folders also contain the Figure and the Result. In the Figure folder you will see the curve of our output. In the Result folder, you will find the data output in .mat version.
## Repository Structure
The structure of Project A is as follow, focusing on the knowledge distillation (KD) method and the transfer learning (TL) method.
```
│  README.md
│  
└─Project A
    ├─IEEE Template
    │      .test
    │      conference_101719.tex
    │      IEEEtran.cls
    │      
    ├─Task1
    │  │  Figure_plot.py
    │  │  Task1.ipynb
    │  │  
    │  ├─Figures
    │  │      accuracy_compare.png
    │  │      accuracy_S.png
    │  │      accuracy_S_EX.png
    │  │      accuracy_S_EX_vs_Temps.png
    │  │      accuracy_S_KD.png
    │  │      accuracy_S_KD_T.png
    │  │      accuracy_S_KD_vs_Temp_alpha.png
    │  │      accuracy_T.png
    │  │      
    │  └─Results
    │          accuracy_S.mat
    │          accuracy_S_EX.mat
    │          accuracy_S_EX_vs_Temps.mat
    │          accuracy_S_KD.mat
    │          accuracy_S_KD_vs_Temp.mat
    │          accuracy_S_KD_vs_Temp_alpha.mat
    │          accuracy_T.mat
    │          
    └─Task2
        │  Task2.ipynb
        │  
        ├─Figures
        │      f1_score.png
        │      f1_score_s_KD.jpg
        │      f1_score_s_scratch.jpg
        │      f1_score_t_0.2dr.jpg
        │      f1_score_t_0.5dr.jpg
        │      f1_score_t_0dr.jpg
        │      student_model_scratch.png
        │      teacher_model.png
        │      
        └─Result
                f1_S_KD.mat
                f1_S_scratch.mat
                f1_T.mat
                f1_T_0.2dr.mat
                f1_T_0.5dr.mat
                f1_T_0dr.mat
