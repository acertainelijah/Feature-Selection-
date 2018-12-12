



def getFeaturesArray(datatable_name, feature_nums_to_search):
    f = open(datatable_name, "r")
    f = [x.strip() for x in f if x.strip()]
    data = [tuple(map(float, x.split())) for x in f[0:]]

    features_arr = [[x[0] for x in data]] #initialize array with classes only
    for feature_num in feature_nums_to_search:
        temp = [x[feature_num] for x in data]
        features_arr.append(temp)

    return features_arr

# search the sample test data set and return feature 1 and 2
result_arr = getFeaturesArray("CS170_SMALLtestdata__SAMPLE.txt", [1, 3])
print result_arr