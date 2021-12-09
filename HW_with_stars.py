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
    with open(f.name, 'w') as file:
        file.write(" ")

#    print(f.name)
    print(os.listdir(path="."))


