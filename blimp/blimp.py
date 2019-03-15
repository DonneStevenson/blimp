def multi_cv(k, n):
    """
    Print text about number of CVs
    Args:
        k (int): number of folds in single cross validation
        n (int): number of time to do the cross validation
    Returns:
        None
    """
    print("Will do a {} fold validation {} times".format(k, n))