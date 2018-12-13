import math
import copy

#TODO
#how do I initially choose the class 1 and 2?
#I understand we're regrouping because of the lack of features, but still idk

global_data = []

def get_features_array(datatable_name, feature_nums_to_search):
    f = open(datatable_name, "r")
    f = [x.strip() for x in f if x.strip()]
    data = [tuple(map(float, x.split())) for x in f[0:]]
    global_data = list(data)

    features_arr = [[x[0] for x in data]] #initialize array with classes only
    for feature_num in feature_nums_to_search:
        temp = [x[feature_num] for x in data]
        features_arr.append(temp)

    return features_arr

def nearest_neighbor(features_arr):
    num_correct = 0




    num_feature_rows = len(features_arr[0])
    num_feature_cols = len(features_arr)

    print "num_feature_rows = " + str(num_feature_rows)
    print "num_feature_cols = " + str(num_feature_cols)

    for k in range(num_feature_rows):  # first loop
        min_distance = pow(10, 100)
        min_index = 0
        for j in range(num_feature_rows):  # second loop
            if k != j:  # don't select same row
                squared_tot_distance = 0
                for i in range(num_feature_cols):
                    if i != 0:
                        squared_tot_distance += pow(features_arr[i][k] - features_arr[i][j], 2)
                square_root_distance = math.sqrt(squared_tot_distance)
                if min_distance > square_root_distance:
                    min_distance = square_root_distance
                    min_index = j

        if features_arr[0][k] == features_arr[0][min_index]:
            num_correct += 1
            print "Num Correct: " + str(num_correct)
        else:
            print "Wrong class!!!"

    return float(num_correct)/num_feature_rows * 100


#main:
# search the sample test data set and return feature 1 and 2
# TODO create a class that iterates through 1 to 10 features and then 1 to 100 features
#result_arr = get_features_array("CS170_SMALLtestdata__108.txt", [6, 5, 4])
# result_arr = get_features_array("CS170_SMALLtestdata__109.txt", [7, 9, 2])
result_arr = get_features_array("CS170_SMALLtestdata__110.txt", [6, 4, 9])
# result_arr = get_features_array("CS170_SMALLtestdata__SAMPLE.txt", [1, 3])
#print result_arr
#print global_data
accuracy = nearest_neighbor(result_arr)
print "Accuracy is: " + str(accuracy) + "%"

