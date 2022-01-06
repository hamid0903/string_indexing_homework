def main(s):
    """
    A string of length five is given. Return the index of the "*" character, return False if not present.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    m=0
    if s[-1]=='\052':
        m+=1
    if s[-2]=='\052':
        m+=1
    if s[-3]=='\052':
        m+=1
    if s[-4]=='\052':
        m+=1    
    if s[-5]=='\052':
        m+=1    
    return m
print(main("go*od"))
