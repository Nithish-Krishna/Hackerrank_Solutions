if __name__ == '__main__':
    n = int(input())
    integer_list = list(map(int, input().split()))
    new_tuple = tuple(integer_list)
    print(hash(new_tuple))
