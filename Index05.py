import string
def main(s):
    """
    Given a variable s string of length five. Determine the number of digits involved in this variable.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    
    m=0
    if '\060'<=s[-1]<='\070':
        m+=1
    if '\060'<=s[-2]<='\070':
        m+=1
    if '\060'<=s[-3]<='\070':
        m+=1
    if '\060'<=s[-4]<='\070':
        m+=1
    if '\060'<=s[-5]<='\070':
        m+=1
    return m
print(main("1a2s3"))

