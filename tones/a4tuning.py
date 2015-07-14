import string
#A4 = 440.0 Hz tuning
tempo = 60
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

f = []
alphabets=string.ascii_lowercase
scale = alphabets[2:7]+"a"+"b"
twoscale=scale*2

def neutral(octavs):
	number_of_notes= octavs*7
	for x in xrange(number_of_notes):
		f.append((twoscale[x%7]+str(x/7),16.35*a**x)) 
	return f
def sharps(octavs):
	number_of_notes= octavs*5
	for x in xrange(number_of_notes):
		f.append()
print neutral(2)