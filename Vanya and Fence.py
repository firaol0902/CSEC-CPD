n, h = map(int, input().split())
 
lis = list(map(int, input().split()))
 
 
counter = 0
 
for i in lis:
 
    if i <= h:
 
        counter += 1
        continue
 
    counter +=2
 
 
print(counter)
