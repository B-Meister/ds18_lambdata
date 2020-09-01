FAV_COLORS = ['maroon', 'black', 'sky-blue']


def report_missing_values(df, threshold=0.1):
    '''
    This function returns a list of columns which have a set percentage of
    missing values.
    Args:
        df (Numpy array or dataframe): Object to be searched for missing values
        threshold (float or int): Percentage of missing values needed to return
    Returns:
        The rows where missing value percentage is higher than the threshold.
    '''
    nan_cols = []
    for column in df:
        if df[column].isna().mean() >= threshold:
            nan_cols.append(df[column].name)
        else:
            pass
    print('Columns containing missing values:')
    print(nan_cols)


def split(df):
    """
    Splits the given dataframe into a 8/2 split for training and testing
    :param df:the dataframe you want to split
    :return:
    """
    training, test = train_test_split(df, test_size=0.2, random_state=42)
    train, val = train_test_split(training, test_size=0.2, random_state=42)

    return train.shape, valshape, test.shape