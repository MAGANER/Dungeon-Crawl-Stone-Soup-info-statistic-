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

#returns list with values of passed dat
def get_data_str(data_to_get, before_symb, after_symb_pos):
	values = []
	for str in data:
	    #get value between : and ,
		position = str.find(data_to_get)
		size = len(data_to_get)
		
		start = position+size+after_symb_pos #pos after :
		end = str.find(before_symb,start, len(str)) # pos before symbol
		
		if is_number(str[start:end]):
			value = int(str[start:end])
			values.append(value)		
	return values
	
#True -> number, False -> string
def is_number(str):
	numbers = ("0","1","2","3","4","5","6","7","8","9")
	if str[0] in numbers:
		return True
	elif str[0] == " ":
		if str[1] in numbers:
			return True
	else:
		return False
	
def combine_list_elems(your_list):
	summ = 0
	for elem in your_list:
		summ= summ + elem
	return summ
	
turns = get_data_str("Turns",",",1)
gold = get_data_str("collected"," ",1) # collected x gold

whole_turns = combine_list_elems(turns)
max_turns = max(turns)
min_turns = min(turns)

whole_gold = combine_list_elems(gold)
max_gold = max(gold)
min_gold = min(gold)

print("whole turns you made:",whole_turns)
print("max turns you made:",max_turns)
print("min turns you made:",min_turns)

print("whole gold you earn",whole_gold)
print("max gold you earn:",max_gold)
print("min gold you earn:",min_gold)

