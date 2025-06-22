def persq(n):
    var = int(n**0.5)
    if var*var == n:
        return True
    
    return False
result = persq(37)
print(result)
    