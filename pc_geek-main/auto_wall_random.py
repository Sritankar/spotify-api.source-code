# importing required modules
import os
import random
import ctypes
# specifying path of the wallpapers folder
path = r"C:\Users\vamsi\Downloads\Wallpapers"
# getting list of files from the folder
wallpapers = os.listdir(path)
# removing unnecessary files from the folder
final_wallpapers=[]
for wall in wallpapers:
	if ".ini" not in wall:
		final_wallpapers.append(wall)
# selecting a random wallpaper
random_wallpaper = final_wallpapers[random.randint(0,len(final_wallpapers)-1)]
# getting absolute path of the selected wallpaper
random_wallpaper = os.path.join(path,random_wallpaper)
# changing the desktop wallpaper using SystemParametersInfoA function
random_wallpaper = bytes(random_wallpaper,'utf-8')
ctypes.windll.user32.SystemParametersInfoA(20,0,random_wallpaper,3)