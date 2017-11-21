import pandas as pd

from PalindromicNumbers import PalindromicNumbers


def write_to_csv(data_set):
    df = pd.DataFrame(data_set, columns=['Decimal', 'Smallest Base In Which The Number Is A Palindrome'])
    try:
        df.to_csv('results.csv', index=False)
        print('\nData has been written to results.csv')
    except PermissionError as err:
        # file is already open, can't write
        print('\n%s. Please close and try again.' % err)


def main(upper_limit=1000):
    data_set = []
    for decimal in range(1, upper_limit + 1):
        base = PalindromicNumbers(decimal).execute()
        data_set.append([decimal, base])
    write_to_csv(data_set)


if __name__ == '__main__':
    main()

