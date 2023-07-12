def search(array,find):
    count=0
    for i in range(len(array)):
        if array[i]==find:
            count+=1
    return count

array=list(map(int,input("Enter the Array Elements: ").split()))
find=int(input("Enter the element to find: "))
print(search(array,find))
