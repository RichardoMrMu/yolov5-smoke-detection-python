import os
import shutil
root_path = './save_data'

label_path = root_path + "/labels"
if not os.path.exists(label_path):
    os.mkdir(label_path)
img_path = root_path + "/images"
if not os.path.exists(img_path):
    os.mkdir(img_path)

before_path =  "./save_data"
for i in os.listdir(before_path):
    if i.endswith(".txt"):
        shutil.move(os.path.join(before_path,i),os.path.join(label_path,i))
    elif i.endswith(".jpg") or i.endswith(".png"):
        shutil.move(os.path.join(before_path,i),os.path.join(img_path,i))
    print(i)
