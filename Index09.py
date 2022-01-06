def main(s):
    """
    a single character string is given. Convert it to int type, return -1 if not possible.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    m=0
    if '\060'<=s[0]<='\070':
        m=s
    else:
        m=-1
    return m
print(main('k'))