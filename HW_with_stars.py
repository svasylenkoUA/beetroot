import os
import tempfile

try:
    r = os.mkdir("cache", 0o777)
except:
    print("Dir exists")

os.chdir("cache")
print(os.getcwd())

for i in range(0,5):
    f = tempfile.NamedTemporaryFile(delete=False, suffix=".bak")
    with open(f.name, mode="a",encoding="utf-8") as file:
        file.write(" \n")

#    print(f.name)
print(os.listdir(path="."))


