def diagonalDifference(arr):
    d1=[arr[i][i] for i in range(len(arr[0]))]
    d2=[arr[i][len(arr[0])-1-i] for i in range(len(arr[0]))]
    print(abs(sum(d1)-sum(d2)))
    return
    
arr=[[11,2,4],[4,5,6],[10,8,-12]]
diagonalDifference(arr)
