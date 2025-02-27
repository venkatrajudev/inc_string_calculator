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
    numbers = [int(n) for n in num_list]
    negatives = [n for n in numbers if n < 0]
    if negatives:
        raise ValueError(f"negative numbers not allowed {', '.join(map(str, negatives))}")
    return sum(numbers)