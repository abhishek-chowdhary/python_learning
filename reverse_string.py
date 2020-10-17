def approach1(data):
    return data[::-1]

def approach2(data):
    reverse_data = []
    data_length=len(data)
    while ( data_length > 0 ):
        reverse_data.append(data[data_length-1])
        data_length=data_length-1
    return reverse_data    

# Recursive approach 
def approach3(data,start,end):
    if start >= end:
        return
    data[start], data[end] = data[end], data[start]
    approach3(data,start+1,end-1)



#Input Data 
data = [1,2,3,4,5,6,7,8,9]

#Calling function to return reverse string and store in inside result variable
result = approach1(data)
print( result)

#Recursive result
approach3(data,0,len(data)-1)
print(data)
