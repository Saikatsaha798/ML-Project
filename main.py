'''
-------------------------- Brief desciption of main.py --------------------------

This contains body of the model with many features which allows user a lot of flexibiliy
to select features to train the model as per needs and availability of data.

Firstly, It gets the CSV of user desired company's csv with the help of file_loc.py, for 
details view its documentation. Then, it fetches data from it and stores in a PANDAS DATAFRAME
and then converts it into a NUMPY ARRAY for more effieciency.

Secondly, It asks user which features can be provided and the machine can be trained using
only those. In it, two options give :
DEFAULT : 'Prev Close', 'Open', 'High', 'Low', 'Last'
CUSTOM : Chosen by USER from DEFAULT FEATRUES

Then, It trains the model with USER SELECTED FEATURES with a LINEAR REGRESSION

Then, It asks USER for providing the DATA for which prediction to be MADE.

Then, A optional feature is there to check the PRECISION of the PREDICTION in case the data 
is released or readily availble which when ERROR is calculated and display with POINTER
PRECISION of 3.

Then, To reduce the users work in restarting the program it asks USER what he wants to do 
next -
1. Same feature set and Company
2. Same Company
3. Fresh Start
4. Exit

Accordingly, program restarting and SAVING user's TIME AND WORK

'''



from sklearn import linear_model
from sklearn.metrics import mean_absolute_percentage_error
import pandas as pd
import numpy as np
import file_loc as f1

def custom_features(df, datasets):
    feature_list = np.array([])
    features = np.array([])

    print("Enter the Datas from below which is available -", end= '\n\n')
    for i in range(5):
        c = input(f"Can you provide data for {df.keys()[i+3]} (y/n) ? ")
        if c=='y':
            feature_list = np.append(feature_list, [i+3], 0)

            if features.size == 0:
                features = datasets[:, np.newaxis, i+3]

            else:
                features = np.append(features, datasets[:, np.newaxis, i+3], 1)

    print()

    if features.size == 0:
        print("As the feature set you have chosen is NULL, hence we switched to DEFAULT FEATURES SET.\n")
        features = datasets[:, 3:8]

    return features,feature_list


def feature_selection(df, datasets):
    feature_list = np.array([])
    print("\nChoose which features are available with you -")

    print("Default : ", end='')
    for i in range(5):
        if i==4:
            print(df.keys()[i+3], end = '\n')
            break
        print(df.keys()[i+3], end = ', ')

    print("[ Note : More features you choose more accurate the prediction is. ]", end='\n\n')

    print("1. Default\n2. Custom\n")

    while True:
            try:
                ch = int(input("Please enter the Choice (only list number) : "))
                if ch  in range(1,3):
                    break
                else:
                    print("Choice NOT provided. ")
            except:
                print("Choice NOT provided. ")

    print()

    if ch == 1:
        stock_features = datasets[:, 3:8]
    
    elif ch == 2:
        stock_features, feature_list = custom_features(df, datasets)
    
    else:
        print("The choice entered was invalid hence the Default was selected.\n")
        stock_features = datasets[:, 3:8]
    
    if feature_list.size == 0:
        feature_list = np.array(range(3,8))

    return stock_features, feature_list

def feature_data(df, feature_list):
    feature_user = np.array([[]])

    print("Enter the Data for PREDICTION : \n")
    
    for i in feature_list:
        while True:
            try:
                data = float(input(f'{df.keys()[i]} : '))
                break
            except:
                print("Data NOT acceptable.")

        feature_user = np.append(feature_user, [[data]], 1)
    print()

    return feature_user

def check_error(label_predicted):
    while True:
            try:
                data = float(input(f'Close [ACTUAL DATA] : '))
                print()
                break
            except:
                print("Data NOT acceptable.")

    label_test = np.array([data])
    print("Error : ",int(mean_absolute_percentage_error(label_test, label_predicted)*1000)/1000, "%\n")
    
ch_1 = 'y'

while ch_1 == 'y':
    df = pd.read_csv(f1.give_location())
    datasets = df.to_numpy()

    ch_2 = 'y'

    while ch_2 == 'y':
        stock_features, feature_list = feature_selection(df, datasets)

        features_train = stock_features

        stock_label = datasets[:,8]
        label_train = stock_label

        model = linear_model.LinearRegression()
        model.fit(features_train, label_train)

        ch_3 = 'y'

        while ch_3 == 'y':
            features_test = feature_data(df, feature_list)

            label_predicted = model.predict(features_test)

            print("Close (Data Predicted) : ", int(label_predicted[0]*1000)/1000 , "\n")

            ch = input("Do want to check error (y/n) ? [DATA REQUIRED] : ")
            print()

            if ch == 'y':
                check_error(label_predicted)
            
            print("Continue with ... \n")
            print("1. Same feature set and Company")
            print("2. Same Company")
            print("3. Fresh Start")
            print("4. Exit\n")

            while True:
                    try:
                        ch_ov = int(input("Choice : "))
                        if ch_ov  in range(1,5):
                            break
                        else:
                            print("Choice NOT provided. ")
                    except:
                        print("Choice NOT provided. ")
            print()
            
            if ch_ov == 1:
                pass
            elif ch_ov == 2:
                ch_3 = 'n'
            elif ch_ov == 3:
                ch_3 = 'n'
                ch_2 = 'n'
            elif ch_ov == 4:
                ch_3 = 'n'
                ch_2 = 'n'
                ch_1 = 'n'
                print("Thank You! for using our PROGRAM.\n")