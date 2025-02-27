def add(numbers:int)->int:
    if numbers == "":
        return 0
    else:
        numbers = numbers.replace("\n",",")
        num_list= numbers.split(",")
        res = sum(int(n) for n in num_list)
        return res