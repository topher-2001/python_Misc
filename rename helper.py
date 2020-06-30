import os

lstdir = os.listdir("./")

search = "Web"
prepend = "web_"

for i in range(len(lstdir)):
    if os.path.isdir("./" + lstdir[i]):
        lsttemdir = os.listdir("./" + lstdir[i])
        for j in range(len(lsttemdir)):
            path = "./" + lstdir[i] + "/"
            if lstdir[i] == search and os.path.isdir(path + lsttemdir[j]):
                os.rename(path + lsttemdir[j], path + prepend + lsttemdir[j])
                print("Renamed: " + path + lsttemdir[j] + " to " + path + prepend + lsttemdir[j])  
