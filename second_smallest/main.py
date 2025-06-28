if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    if n < 2:
        print(None)
    else:
        first = second = float('inf')  # Changed from float('-inf')
        
        for num in arr:
            if num < first:              # Changed from >
                second = first
                first = num
            elif num < second and num != first:  # Changed from >
                second = num
        
        if second == float('inf'):       # Changed from float('-inf')
            print(None)
        else:
            print(second)