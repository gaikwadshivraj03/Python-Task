f = open(r"F:\Final\Template\New folder\Task\access_log", "r")
list1=f.read().split()
t=0
tt=0
f=0
ff=0
fff=0

for i in list1:
    if(i=='200'):
        t+=1
    elif(i=='302'):
        tt+=1        
    elif(i=='304'):
        f+=1
    elif(i=='400'):
        ff+=1
    elif(i=='404'):
        fff+=1
    
print("Status code 200-> count",t)
print("Status code 302-> count",tt)
print("Status code 304-> count",f)
print("Status code 400-> count",ff)
print("Status code 404-> count",fff)



import csv 


fields = ['Status code-'] 
	

rows = [ ["Count of 200 is - " , t], 
		["Count of 302 is - ", tt], 
		["Count of 304 is - ", f], 
		["Count of 400 is - ",ff ], 
		["Count of 404 is -", fff ]]
	    

with open('Status Count', 'w') as f: 
	
	
	write = csv.writer(f) 
	
	write.writerow(fields) 
	write.writerows(rows) 
