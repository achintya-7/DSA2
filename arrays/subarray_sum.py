def brute(arr):
    n = len(arr)
    max_sum = -794939273

    for i in range(n):
        for j in range(i, n):
            summ = 0

            for k in range(i, j+1):
                summ += arr[k]

            max_sum = max(max_sum, summ)

    return max_sum

def better(arr):
    n = len(arr)
    max_sum = -43954365

    for i in range(n):
        summ = 0
        for j in range(i, n):   
            summ += arr[j]
        
            max_sum = max(max_sum, summ)

    return max_sum

def best(arr): # KADHANS
    n = len(arr)
    max_sum = -794939273
    summ = 0

    for i in range(n):
        summ += arr[i]

        if (summ > max_sum):
            max_sum = summ

        if (summ < 0):
            summ = 0
    
    return max_sum


if __name__ == "__main__":
    arr = [29, -1, -2, 4, -1, 4, -3]
    print(better(arr))
    print(brute(arr))
    print(best(arr))
            

            