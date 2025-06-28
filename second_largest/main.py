if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    first = second = float('-inf')
    
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    
    result = second if second != float('-inf') else None
    print(result)