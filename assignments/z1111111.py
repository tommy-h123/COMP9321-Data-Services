import pandas as pd

#Helper functions used to answer the questions neatly
def read_csv(csv_file):
    """
    :param csv_file: the path of csv file
    :return: A dataframe out of the csv file
    """
    return pd.read_csv(csv_file)

def write_in_csv(dataframe, file):
    """
    :param dataframe: The dataframe which must be written into a csv file
    :param file: where the csv must be stored
    """
    dataframe.to_csv(file, sep=',', encoding='utf-8')

def print_dataframe(dataframe, print_column=True, print_rows=True):
    # print column names
    if print_column:
        print(",".join([column for column in dataframe]))

    # print rows one by one
    if print_rows:
        for index, row in dataframe.iterrows():
            print(",".join([str(row[column]) for column in dataframe]))

#Questions asked in the assignment brief
def question_1():
    print("--------------- question_1 ---------------")
    sum_df = read_csv("Olympics_dataset1.csv")
    sum_df.drop(index=0, inplace=True)
    sum_df.columns = ['Country', 'summer_rubbish', 'summer_participation', 'summer_gold',
                        'summer_silver', 'summer_bronze', 'summer_total']

    win_df = read_csv("Olympics_dataset2.csv")
    win_df.drop(index=0, inplace=True)
    win_df.columns = ['Country', 'winter_participation', 'winter_gold', 'winter_silver',
                        'winter_bronze', 'winter_total', 'A', 'B', 'C', 'D', 'E']
    win_df.drop(columns=['A', 'B', 'C', 'D', 'E'], inplace=True)
    df = pd.merge(sum_df, win_df, on='Country')
    print(df.head(5))


def question_2():
    print("--------------- question_2 ---------------")
    pass


def question_3():
    print("--------------- question_3 ---------------")
    pass


def question_4():
    print("--------------- question_4 ---------------")
    pass


def question_5():
    print("--------------- question_5 ---------------")
    pass


def question_6():
    print("--------------- question_6 ---------------")
    pass


def question_7():
    print("--------------- question_7 ---------------")
    pass


def question_8():
    print("--------------- question_8 ---------------")
    pass


def question_9():
    print("--------------- question_8 ---------------")
    pass


def question_10():
    print("--------------- question_8 ---------------")
    pass


if __name__ == "__main__":
    question_1()
    question_2()
    question_3()
    question_4()
    question_5()
    question_6()
    question_7()
    question_8()
    question_9()
    question_10()
