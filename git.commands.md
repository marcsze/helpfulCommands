###A list of useful git commands

####Initial repository setup

git init
git add .
git commit -m "First commit"
git remote add origin https://github.com/SchlossLab/MSze_Project1_Control_Microbiome.git
git remote -v
git push origin master

**Change URL for the adding repository**
git remote set-url origin https://github.com/SchlossLab/MSze_Project1_Control_Microbiome.git

**Add all changes to next commit to git repository**
git add . 

**Observe what will be added to git repository**
git status

**Add all changes to repository**
git commit

**Exit text editor that is pulled up**
:wq

**Alternative way**
git commit -m '<message>'

