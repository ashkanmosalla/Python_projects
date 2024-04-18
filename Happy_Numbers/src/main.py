def is_happy(n):
    seen_num = set()
    while (n != 1) and (n not in seen_num):
        seen_num.add(n)
        n = sum([int(i) ** 2 for i in str(n)])

        return n == 1
    

    if __name__ == '__main__':
        assert is_happy(7) is True
        assert is_happy(45) is False
