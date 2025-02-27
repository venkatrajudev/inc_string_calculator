def add(numbers:int)->int:
    if numbers == "":
        return 0
    else:
        num_list= numbers.split(",")
        res = sum(int(n) for n in num_list)
        print(res,"------")
        return res