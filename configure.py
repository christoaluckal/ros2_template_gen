import os
import shutil

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


ignore = [".git"]
file_list = []

while True:
    package_name = input("Enter package name: ")
    base_cpp = input("Enter base CPP file name: ")
    exec_name = input("Enter CPP executable name: ")
    node_name = input("Enter node name: ")
    class_name = input("Enter Class Name: ")

    if (package_name == base_cpp) or (package_name == exec_name) or (package_name == node_name) or (base_cpp == exec_name) or (base_cpp == node_name) or (exec_name == node_name):
        raise Exception(f"{bcolors.FAIL} All names must be unique {bcolors.ENDC}")

    break


current_location = os.getcwd()
up = os.path.abspath(os.path.join(current_location, os.pardir))
os.chdir(up)
shutil.copytree(os.path.join("ros2_template_gen"), os.path.join(package_name))
os.chdir(os.path.join(package_name))
shutil.rmtree(".git")

for folder, subfolders, files in os.walk(os.getcwd()):
    for file in files:
        filePath = os.path.abspath(os.path.join(folder, file))
        
        # check if filepath has any of the ignore strings
        if any([i in filePath for i in ignore]):
            continue

        file_list.append(filePath)
        # print(filePath)



for file in file_list:
    if "configure.py" in file:
        continue
    with open(file, "r") as f:
        print(file)
        content = f.read()
        content = content.replace("__TEMPLATEPACKAGENAME__", package_name)
        content = content.replace("__TEMPLATEEXENAME__", exec_name)
        content = content.replace("__TEMPLATENODENAME__", node_name)
        content = content.replace("__TEMPLATECPPNAME__", base_cpp)
        content = content.replace("__TEMPLATECLASSNAME__",class_name)

    with open(file, "w") as f:
        f.write(content)

    if "__TEMPLATECPPNAME__" in file:
        new_file = file.replace("__TEMPLATECPPNAME__", base_cpp)
        shutil.move(file, new_file)

shutil.move("include/__TEMPLATEPACKAGENAME__", f"include/{package_name}")
# shutil.move("resource/__TEMPLATE_PACKAGE", "resource/" + package_name)
os.remove("configure.py")

print("You can run")
print("*"*30)
print(bcolors.WARNING + f"colcon build --packages-select {package_name} " + bcolors.ENDC)
print(bcolors.OKCYAN + f"ros2 launch {package_name} start.launch.py" + bcolors.ENDC)
print(bcolors.OKGREEN + f"ros2 run {package_name} {exec_name}" + bcolors.ENDC)
print("*"*30)