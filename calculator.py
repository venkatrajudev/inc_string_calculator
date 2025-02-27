def add(numbers:int)->int:
    # return 0 if numbers get empty string
    if numbers == "":
        return 0
    if numbers.startswith("//"): #checking delimiter 
        unpack = numbers.split("\n",1) # splitting delimter adn numbers
        delimiter = unpack[0][2] # delimter
        numbers = unpack[1] # numbers
        num_list = numbers.split(delimiter)
    else:
        numbers = numbers.replace("\n",",") # new line as delimter
        num_list= numbers.split(",") #delimiter as ,
    numbers = [int(n) for n in num_list]
    negatives = [n for n in numbers if n < 0] #checking negatives
    if negatives:
        raise ValueError(f"negative numbers not allowed {', '.join(map(str, negatives))}") # showing negative numbers
    allowed_nums = [n for n in numbers if n <= 1000] # checking positive numbers

    return sum(allowed_nums) # adding all string numbers