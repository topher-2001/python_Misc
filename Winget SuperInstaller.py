import os
import webbrowser


#Programs as WinGet Names
will_install = ("Chrome", "Visual Studio Code", "OBS Studio", "7Zip", "Windows Terminal",
		"Minecraft Launcher", "Ubuntu 18.04", "Steam")
cant_install = ("Java", "")

#Winget Agreement
print("IN ORDER FOR THIS TO RUN YOU MUST BEABLE TO USE \"winget\"")
has_winget = input("Do you have \"winget\" [y/n]: ")
print(has_winget)

#Dosent have winget
if has_winget.lower()[0] == 'n':
	print("unable to run")
	print("please install \"winget\"")
	webbrowser.open("https://docs.microsoft.com/en-us/windows/package-manager/winget/", new = 2)
	exit()

#Print installable and non installable programs
print("\nThis program will install: ")
for prog in will_install:
	print(prog)
print("\nYou will still need to install ")
for prog in cant_install:
	print(prog)

#Agreement
agree = input("Are you ok with all these being installed [y/n]")
if agree.lower()[0] == 'n':
	print("Ok program closing")
	exit()

#Installation
for program in will_install:
	os.system("winget install " + program)
