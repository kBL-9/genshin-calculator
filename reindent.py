from os import listdir, walk

path = __file__.replace("\\reindent.py", "")

def reindent(file_path: str):
    text = ""
    with open(file_path, "r") as f:
       text = f.read()
    
    with open(file_path, "w") as f:
        f.write(text.replace("\t", "    "))

# iterate through all file
for root, subdirs, files in walk(path):
    for file_name in files:
        if file_name.endswith(".py"):
            file_path = f"{root}\{file_name}"
            reindent(file_path)