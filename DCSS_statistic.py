import os
import time as TIME

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
		
		if str[start:end].isdigit():
			value = int(str[start:end])
			values.append(value)		
	return values
def get_raw_data_str(data_to_get, before_symb, after_symb_pos):
	values = []
	for str in data:
		#get value between : and ,
		position = str.find(data_to_get)
		size = len(data_to_get)
		
		start = position+size+after_symb_pos #pos after :
		end = str.find(before_symb,start, len(str)) # pos before symbol
		
		value = str[start:end]
		values.append(value)		
	return values	
	

	
def combine_list_elems(your_list):
	summ = 0
	for elem in your_list:
		summ= summ + elem
	return summ

#game could be very short, so it wasn't wrote in morgue	
def clear_shit_outta_time_list(time):
	new_time = []
	for elem in time:
		if len(elem) > 0 and elem[0].isdigit():
			new_time.append(elem)
	
	return new_time


def is_null(number):
	if int(number) == 0:
		return True
	else:
		return False
		
def compute_whole_game_time(time):
	hours = 0
	minutes = 0
	seconds = 0
	for elem in time:
		#get data
		hour = int(elem[0:2])
		minute = int(elem[3:5])
		second = int(elem[6:9])
		
		#compute all
		hours = hours + hour
		minutes = minutes + minute
		seconds = seconds + second
	
	final_seconds = final_minutes = final_hours = 0
	
	seconds_str = repr(seconds/60)
	minutes_str = repr(minutes/60)
	hours_str   = repr(hours/60)
	
	#compute seconds
	_seconds = int(seconds_str[3:5])+ int(minutes_str[3:5])
	if _seconds > 60:
		_seconds = _seconds/60
		
		point_pos = repr(_seconds).find(".")
		_minutes = int(repr(_seconds)[0:point_pos])
		minutes = minutes + _minutes
		minutes_str = repr(minutes/60) # update var
		
		_seconds = int(repr(_seconds)[point_pos+1:point_pos+3])

	#compute minutes
	_hours = 0
	_minutes = float(minutes_str)
	if _minutes > 60:
		_minutes = _minutes/60
	else:
		point_pos = repr(_minutes).find(".")
		_hours = int(repr(_minutes)[0:point_pos])
		_minutes = int(repr(_minutes)[point_pos+1:point_pos+3])
	
	#compute hours
	if hours > 0:
		_hours = _hours + hours
		
	final_hours   = _hours
	final_minutes = _minutes
	final_seconds = _seconds
	
	return (final_hours,final_minutes,final_seconds)
	
time_before = TIME.time()

turns = get_data_str("Turns",",",1)
gold = get_data_str("collected"," ",1) # collected x gold
time = get_raw_data_str("lasted","(",1) # game lasted x time
time = clear_shit_outta_time_list(time)
game_time = compute_whole_game_time(time)



time_after = TIME.time()
computing_time = time_after - time_before


print("you played:(h,m,s) ",game_time,"\n")
print("statistic computed in ",computing_time," seconds")


end = input("show info about(gold)(Yg,Ng)")
if end == "Yg":
	whole_gold = combine_list_elems(gold)
	max_gold = max(gold)
	min_gold = min(gold)
	print("whole gold you earn",whole_gold)
	print("max gold you earn:",max_gold)
	print("min gold you earn:",min_gold)
	final = input()# to prevent terminal closing
