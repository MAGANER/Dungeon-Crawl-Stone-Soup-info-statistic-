import os

#get path, including hard-ware,(E:/DCSS for example)
dcss_path = input("enter DCSS path:")
file_dir = dcss_path+"/morgue/"
all_files = os.listdir(file_dir)

#get only files with character data
txt_only = []
for str in all_files:
	size = len(str)
	if str[size-3:size+1] == "txt":
		txt_only.append(str)
		
#read all data 
data = []
for file in txt_only:
	current_file = open(file_dir+file)
	data_str = current_file.read()
	data.append(data_str)
	current_file.close()

#returns list with values of passed data
def get_data_str(data_to_get):
	values = []
	for str in data:
	    #get value between : and ,
		position = str.find(data_to_get)
		size = len(data_to_get)
		
		start = position+size+1 #pos after :
		end = str.find(",",start, len(str)) # pos before ,
			
		value = str[start:end]
		values.append(value)
		
	return values

def clear_list(your_list, start,end):
	new_list = []
	for str in your_list:
		str = str[start:end+1]
		new_list.append(str)
	your_list.clear()
	return new_list
		
turns = get_data_str("Turns")
gold = get_data_str("collected") # collected x gold
gold = clear_list(gold,0,1)

