n=int(raw_input("Enter No :: "))
for i in range(2,n):
    if n % i == 0 :
        break
if i==(n-1):
	print "prime"
else:
	print "not prime"