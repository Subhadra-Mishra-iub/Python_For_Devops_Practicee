import os

folders = input("Please provide list of folders names with spaces in between: ").split(',')

for folder in folders:
    
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print(f"Folder {folder} does not exist")
        
    print(" === Listing files for the folder - " + folder)
    
    for file in files:
        print(file)    
        

#command to run the file in the terminal is: (Example)
#(base) subhadramishra@Subhadras-MacBook-Air Python_For_Devops_Practicee % python "/Users/subhadramishra/Desktop/Overall Practice - 2025/Python_For_Devops_Practicee/Day 10/test.py"
# Please provide list of folders names with spaces in between: /Users/subhadramishra/Desktop/Overall Practice - 2025/Python_For_Devops_Practicee/Day-9
#  === Listing files for the folder - /Users/subhadramishra/Desktop/Overall Practice - 2025/Python_For_Devops_Practicee/Day-9
# my note.txt
# 04-while-loop-devops-usecases.md
# 03-for-loop-devops-usecases.md
# 01-loops.md
# 02-loop-controls.md
# (base) subhadramishra@Subhadras-MacBook-Air Python_For_Devops_Practicee % 

# Note: while giving the file, give the full path of the file.