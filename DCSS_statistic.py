import os

#get path, including hard-ware,(E:/DCSS for example)
dcss_path = input("enter DCSS path:")
all_files = os.listdir(dcss_path+"/morgue/")

#get only files with character data
txt_only = []
for str in all_files:
	size = len(str)
	if str[size-3:size+1] == "txt":
		txt_only.append(str)
		
