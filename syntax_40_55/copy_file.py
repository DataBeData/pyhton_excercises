#Copy File Content
#Copy the contents of source.txt into a new file called copy.txt.

with open("ex.txt", "r", newline="") as file, \
    open("copy.txt", "w", newline="") as copy_file:
    text = file.read()
    copy_file.write(text)

"""
with open("ex.txt", "r", newline="") as src, \
open("copy.txt", "w", newline="") as dst:
    for line in src:
        dst.write(line)
"""
"""
import shutil
shutil.copyfile("ex.txt", "copy.txt")
"""