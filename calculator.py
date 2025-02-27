def add(numbers)->int:
    if numbers == "":
        return 0
    else:
        num_list= numbers.split(",")
        return sum(int(n) for n in num_list)