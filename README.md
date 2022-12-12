# ECE1512_2022F_ProjectRepo_HaoxiangNing_YitianLiu
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
```              
The structure of Project B is as follow, focusing on the dataset distillation (DD) method.
```
│              
└─Project B
    │  .test
    │  networks.ipynb
    │  utils.ipynb
    │  
    ├─Task1
    │      .test
    │      CIFAR10_Continual_Learning.ipynb
    │      CIFAR10_Cross_architecture_Generalization.ipynb
    │      CIFAR10_syn.ipynb
    │      CIFAR10_syn_Gaussian.ipynb
    │      MHIST_Continual_Learning.ipynb
    │      MNIST_Cross_architecture_Generalization.ipynb
    │      MNIST_syn.ipynb
    │      MNIST_syn_Gaussian.ipynb
    │      Train whole dataset.ipynb
    │      
    └─Task2
            .test
            Distribution_Matching_CIFAR10.ipynb
            Distribution_Matching_MNIST.ipynb
            Matching Training Trajectories.ipynb
        
