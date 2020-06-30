def countup(n):
    while True:
        yield n
        n += 1

def get_nth_element(n):
    final_element = ''
    countup_gen = countup(0)

    while True:
        num = countup_gen.__next__()
        final_element += str(num * num)
        if len(final_element) > n:
            return final_element[n]


print(get_nth_element(4))

