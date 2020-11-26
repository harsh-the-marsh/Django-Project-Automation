import os
import sys


def create():
    projectname = str(sys.argv[1])
    appname = str(sys.argv[2])
    print("Project Name:- ",projectname)
    print("App Name:- ",appname)
    os.system('cmd /c "cd /d E:\Work\Projects\Django Projects & django-admin startproject "' + projectname + '"')
    os.system('cmd /c "cd /d E:\Work\Projects\Django Projects\\"' + projectname + '" & virtualenv venv"')
    os.system('cmd /c "cd /d E:\Work\Projects\Django Projects\\"' + projectname + '" & mkdir static"')
    os.system('cmd /c "cd /d E:\Work\Projects\Django Projects\\"' + projectname + '" & mkdir templates"')
    os.system('cmd /c "cd /d E:\Work\Projects\Django Projects\\"' + projectname + '" & python manage.py startapp "' + appname + '"')

    file_name = 'E:\Work\Projects\Django Projects\\' + projectname + '\\' + projectname + '\\settings.py'

    line_num1= 16
    line_num2 = 39
    text1 = "STATIC_DIR = os.path.join(BASE_DIR,'static')\nTEMPLATES_DIR = os.path.join(BASE_DIR,'templates')\n"
    text2 = "\t'"+appname+"'\n]\n"
    lines = open(file_name, 'r').readlines()
    lines[line_num1] = text1
    lines[line_num2] = text2
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()


    line_number = 58
    string_to_add = "TEMPLATES_DIR"
    string_to_find = "'DIRS': ["
    filename = 'E:\Work\Projects\Django Projects\\' + projectname + '\\' + projectname + '\\settings.py'
    with open(filename,"r") as f:
        s = f.readlines()
    s[line_number] = s[line_number].replace(string_to_find,string_to_find+string_to_add)
    with open(filename,"w") as f:
        for line in s:
            f.write(line)
    f.close()

    line_num= 120
    text = "\nSTATICFILES_DIRS = [STATIC_DIR]\n"
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    last = open(file_name, 'w')
    last.writelines(lines)
    last.close()


    os.system('cmd /c "cd /d E:\Work\Projects\Django Projects & code "' + projectname + '"')

    
if __name__ == "__main__":
    create()