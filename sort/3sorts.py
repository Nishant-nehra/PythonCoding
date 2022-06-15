def bubbleSort(arr,n):
    for i in range(n):
        swaps=0
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swaps+=1
        if swaps==0:
            break
def selectionSort(arr,n):
    for i in range(n):
        lowIndex=i
        for j in range(i+1,n):
            if arr[j]<arr[lowIndex]:
                lowIndex=j
        arr[i],arr[lowIndex]=arr[lowIndex],arr[i]

def insertionSort(arr,n):
    for i in range(1,n):
        j=i-1
        temp=arr[i]
        while j>-1 and arr[j]>temp:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=temp


n=int(input())
arr=list(map(int,input().split()))
# bubbleSort(arr,n)
# selectionSort(arr,n)
insertionSort(arr,n)
print(*arr,sep=' ')
