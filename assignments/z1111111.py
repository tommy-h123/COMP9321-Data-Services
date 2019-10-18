import pandas as pd


#Questions asked in the assignment brief
def question_1():
    print("--------------- question_1 ---------------")
    #read in both csv files
    sum_df = pd.read_csv("Olympics_dataset1.csv")
    win_df = pd.read_csv("Olympics_dataset2.csv")

    #drop first row
    sum_df.drop(index=0, inplace=True)
    win_df.drop(index=0, inplace=True)

    #rename columns, gave distinct names A-E for columns to be removed
    sum_df.columns = ['Country', 'summer_rubbish', 'summer_participation', 'summer_gold', 'summer_silver', 'summer_bronze', 'summer_total']
    win_df.columns = ['Country', 'winter_participation', 'winter_gold', 'winter_silver', 'winter_bronze', 'winter_total', 'A', 'B', 'C', 'D', 'E']
    
    #remove unwanted columns
    win_df.drop(columns=['A', 'B', 'C', 'D', 'E'], inplace=True)
    
    #merge dataframes on Country and print the first 5 rows
    df = pd.merge(sum_df, win_df, on='Country')
    print(df.head(5).to_string())

    #return df for use in following questions
    return df


def question_2(df):
    print("--------------- question_2 ---------------")
    #use regex to remove everything after the country name ie. the abreviation
    df['Country'] = df['Country'].str.replace(' \(.*', '', regex=True)

    #set the country column as the index, this deletes the old column but can be configured to leave County column as well as having the country names as index with drop=False
    df.set_index('Country', inplace=True)

    #drop columns that are unwanted
    df.drop(columns=['summer_rubbish', 'summer_total', 'winter_total'], inplace=True)

    #print first 5 rows
    print(df.head(5).to_string())

    return df


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
    df = question_1()
    df = question_2(df)
    question_3()
    question_4()
    question_5()
    question_6()
    question_7()
    question_8()
    question_9()
    question_10()
