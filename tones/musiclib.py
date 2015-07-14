import string
#A4 = 440.0 Hz tuning
tempo = 96
#number_of_notes = 12

sample = [("c0",16.35),("cs0",17.32),("db0",17.32),("d0",18.35),\
	("ds0",19.45),("eb0",19.45),("e0",20.60),("f0",21.83),\
	("fs0",23.12),("gb0",23.12),("g0",24.50),("gs0",25.96),\
	("ab0",25.96),("a0",27.50),("as0",29.14),("bb0",29.14),\
	("b0",30.87)]

# Formula used:
# fn = f0 * a**n
# f0  is the default hertz you want to start from
# a = 2**(1.0/12.0)
# n = number of half steps 
# fn is the frequency we want 

######################
a = 2**(1.0/12.0)
f0 = 16.35
n = 1
#####################
#fn = f0 * a ** n

neutralnotes = []
sharpnotes = []
alphabets=string.ascii_lowercase
scale = alphabets[2:7]+"a"+"b"
scalewithsemi='c*d*ef*g*a*b'
twoscale=scalewithsemi*2




def get_base_note(note): #this will get base note.
	return note[0]       #ex: 'cs0' will be 'c'
def get_octav(note):     #this will get octav.
	return note[-1]      #ex: 'cs0' will be '0'
def get_others(note):    #this will get sharps or flats
	if len(note)==2:     #ex: 'cs0' will be 's'
		return 'n'		 #neutral will return 'n'
	else:
		return note[1:-1] 
def get_sharps(note):             #this counts sharps
	others= get_others(note)
	counter = 0
	for x in xrange(len(others)):
		if others[x] == 's':
			counter +=1
	return counter

def get_flats(note):              #this counts flats
	others= get_others(note)
	counter = 0
	for x in xrange(len(others)):
		if others[x] == 'b':
			counter +=1
	return counter
def get_neutrals(note):			 #this counts neutrals
	others= get_others(note)
	counter = 0
	for x in xrange(len(others)):
		if others[x] == 'n':
			counter +=1
	return counter
def total_sharp_flat_neutral(note): #this totals flats and sharps
	sharpnums= get_sharps(note)
	flatnums= get_flats(note)
	neutralnums= get_neutrals(note)
	if neutralnums >0:
		return 0
	else:
		return sharpnums - flatnums

def get_location(note):
	base_note= get_base_note(note)
	octav= get_octav(note)
	sharpnums= get_sharps(note)
	flatnums=get_flats(note)
	for x in xrange(len(scalewithsemi)):
		if scalewithsemi[x]== base_note:
			return ((x+int(octav)*12)+total_sharp_flat_neutral(note))


def frequency(note,tuning):
	print note
	if note == 'rest':
		return 0
	if note == '----------':
		return 0
	f0 = tuning #A4 = tuning hertz
	a4_location= get_location('a4')
	note_location= get_location(note)
	steps = note_location - a4_location
	return tuning*a**steps


def timesDict():
	octav =7 
	#q = [("sq",0.125),("q",0.25),("dq",.375),("ei",0.125 ), ("h",0.5),("dh",.75),("w",1.0),("z",0.0)]
	q = [('w',4),('h',2),('q',1),('e',0.5),('s',0.25),\
	('dq',1.5),('de',1.75),('ds',3.0/8.0),\
	('z',0)]
	d = dict()
	for x in q:
		d[x[0]] = x[1]
	return d
