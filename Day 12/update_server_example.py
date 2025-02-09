#Step-1 is read the file
#Create a list store in a variable list
#oepn in write mode
#updating MAX_connection

#Here key is that to be replace and value is by what it will be replaced

def update_server_config(file_path, key, value):
    
    #step1
    with open(file_path, "r") as file:
        lines = file.readlines()
        
    #step2
    with open(file_path, "w") as file:
        for line in lines:
            if key in line:
                file.write(key + "=" +value + "\n")
            else:
                file.write(line)
                
update_server_config("server.config", "MAX_CONNECTIONS", "1000")