if __name__=='__main__':
    n=int(input())
    num=tuple(map(int, input().split()))
    hash_val=hash(num)
    print(hash_val)

    print("-------------------------------")
    n = int(input())
    l = tuple(map(int, input().split()))
    tuple_hash = hash(l)
    print(tuple_hash)