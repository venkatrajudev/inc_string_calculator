def add(numbers:int)->int:
    if numbers == "":
        return 0
    if numbers.startswith("//"):
        unpack = numbers.split("\n",1)
        delimiter = unpack[0][2]
        numbers = unpack[1]
        num_list = numbers.split(delimiter)
    else:
        numbers = numbers.replace("\n",",")
        num_list= numbers.split(",")
    result = sum(int(n) for n in num_list)
    return result