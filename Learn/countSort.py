from random import randint
import array

MYLIMIT = 32
def generate_randomnos(N, mylist):
    for i in range(0,N):
        x = randint(0,10)
        mylist.append(x)


def countsort(myarray, k):
	temp = array.array('B', xrange(1)) * (k)    
	for i in myarray: #temp is my index array
		temp[i] += 1         #no.  of occurences and cumulative

	#print 'temp after step 1:', temp


	print "temp len", len(temp)
	for index, each in enumerate(temp):
		if index == 0:
			continue
		temp[index] += temp[index-1]


	#print 'temp after step 2:', temp
		
	#places = [0 for i in range(len(myarray))] 
	places = array.array('B', xrange(1)) * len(myarray) 
	#print "places:", places
	for each in myarray:
		places[temp[each]-1] = each
		temp[each] -= 1

	return places

def generateRand(k, myarray):
	k = k-2 #because one number already added
	while k>0:
		myarray.append(randint(0,99)) #memory limitation, so uaing smaller range for randInt
		k -= 1;


myarray = array.array('B',[randint(0,9)])

generateRand(2 ** MYLIMIT - 1, myarray)

print "Initial array:", myarray
print countsort(myarray, 2 ** MYLIMIT - 1)
