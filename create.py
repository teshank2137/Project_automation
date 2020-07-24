import sys
import os
from github import Github

#!-------------------------------------------------------------
# ? go to bottom to add custom paths to your application
#!-------------------------------------------------------------

with open('path.txt', 'r') as pat:
    for line in pat:
        path = line

for _ in range(2):
    sys.argv.append('')

if sys.argv[1] == '':
    print('Enter folder name\ncreate *foldername* *code editor* *private/public*')
    sys.exit(1)

with open('token.txt', 'r') as tok:
    for line in tok:
        token = line


# ?local stuff

dire = path[0].lower()+':'
os.system(dire)
os.chdir(path)
name = str(sys.argv[1])
os.mkdir(name)
new_path = path + '\\' + name
os.chdir(new_path)
os.system(f'echo {name} >> READme.md')
os.system('echo enter_classified_files >> .gitignore')


# ?github stuff

g = Github(token)
user = g.get_user()
login = user.login
if sys.argv[3].lower() == 'public':
    repo = user.create_repo(name)
else:
    repo = user.create_repo(name, private=True)

os.system('git init')
os.system('git add .')
os.system('git commit -m "initial commit"')
os.system(f'git remote add origin https://github.com/{login}/{name}.git')
os.system('git push -u origin master')

#!-------------------------------------------------------------
# ?add paths to your applicaton here
# * replace{} with appropriate placeholder
# * add new apllication as elif sys.argv[2] == '{your shortcut key}'
# *                        {add 4 spaces}os.system('{command for your application}')
#!-------------------------------------------------------------

# *jupyter notebook
if sys.argv[2] == 'jn':
    os.system('jupyter notebook')

elif sys.argv[2] == 'n':
    os.system('pause')

# TODO visual studio
elif sys.argv[2] == 'vs':
    os.system('{vstudio path}')

elif sys.argv[2] == '{shortcut}':
    os.system('{command}')

elif sys.argv[2] == '{shortcut}':
    os.system('{command}')


# *visual studio code :: DEFAULT
else:
    os.system('code .')
