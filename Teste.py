def swap(a,b,c):
    a[0]=b
    c = b
    return None

if __name__ == '__main__':
    a = [100]

    a[0] = 3
    c = 3
    b = 4

    swap(a,b,c)

    print(a[0])
    print(b)

