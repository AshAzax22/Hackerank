if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    z=max(arr)
    while True:
        if z in arr:
            arr.remove(z)
        else:
            break
    print(max(arr))
