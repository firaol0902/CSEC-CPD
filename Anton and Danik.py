n = int(input())
 
winner = input()
 
danik = winner.count("D")
anton = winner.count("A")
 
if danik == anton:
 
    print("Friendship")
 
elif danik < anton:
 
    print("Anton")
else:
 
    print("Danik")
