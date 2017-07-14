# Enter your code here. Read input from STDIN. Print output to STDOUTN = int(raw_input())
N = int(raw_input())

for i in range(N):                 
	string = raw_input()            

	odd = []
	even= []
	for index,item in enumerate(string):
	
	    if index %2 == 0: 
	        even.append(item)
	    elif index %2 != 0: 
	        odd.append(item)
	        
	even = ''.join(even)
	odd = ''.join(odd)


	answer = even + ' ' + odd

	print answer
