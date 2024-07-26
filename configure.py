import os
import shutil

ignore = [".git"]
file_list = []

while True:
    package_name = input("Enter package name: ")
    base_py = input("Enter base python file name: ")
    exec_name = input("Enter executable name: ")
    node_name = input("Enter node name: ")

    if (package_name == base_py) or (package_name == exec_name) or (package_name == node_name) or (base_py == exec_name) or (base_py == node_name) or (exec_name == node_name):
        print("All names must be unique")
        continue

    break


current_location = os.getcwd()
up = os.path.abspath(os.path.join(current_location, os.pardir))
os.chdir(up)
shutil.copytree(os.path.join("ros2_py_template"), os.path.join(package_name))
os.chdir(os.path.join(package_name))
shutil.rmtree(".git")

for folder, subfolders, files in os.walk(os.getcwd()):
    for file in files:
        filePath = os.path.abspath(os.path.join(folder, file))
        
        # check if filepath has any of the ignore strings
        if any([i in filePath for i in ignore]):
            continue

        file_list.append(filePath)
        print(filePath)



for file in file_list:
    if "configure.py" in file:
        continue
    with open(file, "r") as f:
        content = f.read()
        content = content.replace("__TEMPLATE_PACKAGE", package_name)
        content = content.replace("__TEMPLATE_EXEC_NAME", exec_name)
        content = content.replace("__TEMPLATE_NODE_NAME", node_name)
        content = content.replace("__TEMPLATE_ENTRY", base_py)

    with open(file, "w") as f:
        f.write(content)

    if "__TEMPLATE_ENTRY" in file:
        new_file = file.replace("__TEMPLATE_ENTRY", base_py)
        shutil.move(file, new_file)

shutil.move("__TEMPLATE_PACKAGE", package_name)
shutil.move("resource/__TEMPLATE_PACKAGE", "resource/" + package_name)


    