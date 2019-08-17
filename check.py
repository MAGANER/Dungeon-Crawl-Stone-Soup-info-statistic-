import os

dcss_path = "E:/DCSS" #my path
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

#game could be very short, so it wasn't wrote in morgue	
def clear_shit_outta_time_list(time):
	new_time = []
	for elem in time:
		if is_number(elem[0]):
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
		#my game never lasted more than 59 minutes
		print("WOW, finish this script!")
		
	final_hours   = _hours
	final_minutes = _minutes
	final_seconds = _seconds
	
	return (final_hours,final_minutes,final_seconds)
	
	
turns = get_data_str("Turns",",",1)
gold = get_data_str("collected"," ",1) # collected x gold
time = get_raw_data_str("lasted","(",1) # game lasted x time
time = clear_shit_outta_time_list(time)
game_time = compute_whole_game_time(time)

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

print("you played:(h,m,s)",game_time)