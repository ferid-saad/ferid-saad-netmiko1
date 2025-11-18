Mon Projet Netmiko
 I. Initialiser un dépôt Git local
 cd /c/Users/fersd/OneDrive/Desktop/ferid-saad-netmiko
 II. Ajouter et commiter des fichiers
 git init
 sudo nano README.md
 git add .
  git commit -m"Ajout du script Python principal"
   git log
commit 214a0fbc538cbb2d0fc741fc6c42df4815e4779b (HEAD -> master)
Author: SAAD FERID <fersd2018@gmail.com>
Date:   Tue Nov 18 08:55:47 2025 +0100

III. Créer et fusionner des branches

git branch feature/netmiko
 git checkout feature/netmiko
 git commit -m "Ajout de la fonction acces_netmiko"
 git checkout master
  git merge feature/netmiko

IV. Travailler avec un dépôt distant sur GitHub

git remote add origin https://github.com/ferid-saad/ferid-saad-netmiko1.git
git push -u origin main
git fetch origin
git checkout -b feature/salut origin/feature/salut

