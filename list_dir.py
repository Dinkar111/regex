import os


os.chdir('new directory')
current_dir = os.getcwd()

# prints all the files from inside the new directory 
for root, dir, files in os.walk(current_dir):
    for f in files:
        print(os.path.join(root, f))


# print('<-------------->')
# for files in os.listdir(current_dir):
#     full_path = os.path.join(current_dir, files)
#     if os.path.isfile(full_path):
#         print(full_path)
#     else:
#         for f in os.listdir(full_path):
#             print(os.path.join(full_path, f))
