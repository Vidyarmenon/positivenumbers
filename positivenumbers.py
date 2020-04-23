list = [] 
  
n = int(input("Enter number of elements : ")) 
  
for i in range(0, n): 
    ele = int(input()) 
  
    list.append(ele)

index=0
while(index<n):
    if(list[index]>0):
        print(list[index]," ")
    index=index+1
    
