def main(s):
    """
    A string of five numbers is given. Find the sum of its numbers.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    m1=int(s[-1])
    m2=int(s[-2])
    m3=int(s[-3])
    m4=int(s[-4])
    m5=int(s[-5])
    m=m1+m2+m3+m4+m5
    return m
print(main("12345"))