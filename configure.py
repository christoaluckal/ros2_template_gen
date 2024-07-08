import os
import shutil

ignore = [".git"]
file_list = []

for folder, subfolders, files in os.walk(os.getcwd()):
    for file in files:
        filePath = os.path.abspath(os.path.join(folder, file))
        
        # check if filepath has any of the ignore strings
        if any([i in filePath for i in ignore]):
            continue

        file_list.append(filePath)
        print(filePath)

package_name = input("Enter package name: ")
base_py = input("Enter base python file name: ")
exec_name = input("Enter executable name: ")
node_name = input("Enter node name: ")

for file in file_list:
    if "configure.py" in file:
        continue
    with open(file, "r") as f:
        content = f.read()
        content = content.replace("__TEMPLATE_PACKAGE", package_name)
        content = content.replace("__TEMPLATE_EXEC_NAME", exec_name)
        content = content.replace("__TEMPLATE_NODE_NAME", node_name)

    with open(file, "w") as f:
        f.write(content)

    if "__TEMPLATE_ENTRY" in file:
        new_file = file.replace("__TEMPLATE_ENTRY", base_py)
        shutil.move(file, new_file)

shutil.move("__TEMPLATE_PACKAGE", package_name)


    