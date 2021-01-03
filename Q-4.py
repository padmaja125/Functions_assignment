get = input("Enter the string with hyphen separated : ")
def sorting(x):
    a=[]
    for y in x.split('-'):
        a.append(y) 
    return a.sort()

print(sorting(get))