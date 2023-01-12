# read
'''# read file
file = open("show.txt", "r")
print(file.read())
'''

'''# Read lines
file = open("show.txt", "r")
print(file.readline(5))  # 5 charactor num
print("ggggg")
print(file.readline())
print(file.readlines())   # lines conver LIST
'''

'''#loop Read
file = open("show.txt", "r")
for x in file:
    print(x)
'''

# Write
'''# Deleat and write
file = open("show.txt", "w")
file.write("pooda punda")
file.close()

file = open("show.txt", "r")
print(file.read())'''

'''# appand
file = open("show.txt", "a")
file.write("\njgghjhfyk jhhvjgch")
file.close()

file = open("show.txt", "r")
print(file.read())'''

'''# Delet file
import os
if os.path.exists("shofw.txt"):
    os.remove("shofw.txt")
    # os.rmdir("folder_name")  #folder delet
else:
    print("file not ")