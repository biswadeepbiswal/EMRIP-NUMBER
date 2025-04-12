# print emrip number in a given range bi using function


def is_emrip(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
        return True
    
    print("emrip numbers from 1 to 100 are:")
    for num in range(1, 101):
        if is_emrip(num):
            reversed_num = int(str(num)[::-1])
            if reversed_num !=num and is_emrip(reversed_num):
                print(num, end='')