n = int(input())
arr=list(map(int,input().split()))
count=0
arr2=[]
for i in range(n):
    #here i have appended a tuple with value and index%2
    arr2.append((arr[i],i%2))
arr2.sort()
for i in range(n):
    #here i am checking if after sort index goes from odd to even place or vice versa or not
    #if index parity(odd-even) is changed then count++
    if arr2[i][1]!=i%2:
        count+=1
#1 adjacent swap would fix 2 index parity so total swap req ->count/2
print(count//2)