import math
import copy
import time

#TODO
#how do I initially choose the class 1 and 2?
#I understand we're regrouping because of the lack of features, but still idk

def get_features_array(data, feature_nums_to_search):

    features_arr = [[x[0] for x in data]] #initialize array with classes only
    for feature_num in feature_nums_to_search:
        temp = [x[feature_num] for x in data]
        features_arr.append(temp)

    return features_arr

def nearest_neighbor(features_arr):
    num_correct = 0

    num_feature_rows = len(features_arr[0])
    num_feature_cols = len(features_arr)

    #print "num_feature_rows = " + str(num_feature_rows)
    #print "num_feature_cols = " + str(num_feature_cols)

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
            #print "Num Correct: " + str(num_correct)
        #else:
            #print "Wrong class!!!"

    return float(num_correct)/num_feature_rows * 100

def forward_selection(datatable_name):

    f = open(datatable_name, "r")
    f = [x.strip() for x in f if x.strip()]
    data = [tuple(map(float, x.split())) for x in f[0:]]

    num_feature_rows = len(data)
    num_feature_cols = len(data[0])

    print "fw --- num_feature_rows = " + str(num_feature_rows)
    print "fw --- num_feature_cols = " + str(num_feature_cols)

    level_BEST_features_node = []  # node that you are checking
    level_BEST_accuracy = 0
    set_of_BEST_features_nodes = []  # current set of best nodes, greedy path
    BEST_accuracy = 0

    for i in range(num_feature_cols):
        if (i != 0):
            initial_node = level_BEST_features_node

            level_BEST_features_node = []  # node that you are checking
            level_BEST_accuracy = 0
            for j in range(num_feature_cols):
                #temp_curr_features_node = list(set_of_BEST_features_nodes)
                temp_curr_features_node = list(initial_node)
                if j != 0 and not j in temp_curr_features_node:
                    temp_curr_features_node.append(j)

                    #print "temp_curr_features_node = " + str(temp_curr_features_node) + " - j val: " + str(j) \
                    #      + " - i val: " + str(i)
                    result_arr = get_features_array(data, temp_curr_features_node)
                    accuracy = nearest_neighbor(result_arr)

                    curly_braces = print_node_array(temp_curr_features_node)
                    #print "Using feature(s) " + curly_braces + " accuracy is " + str(accuracy) + "%"

                    if(accuracy > level_BEST_accuracy): # if the accuracy of the current node is better than BEST in level
                        level_BEST_features_node = temp_curr_features_node  # update best features array
                        level_BEST_accuracy = accuracy  # updated the new accuracy

            curly_braces_loop = print_node_array(level_BEST_features_node)
            # display curr level best
            print "Feature set " + curly_braces_loop + " was best, accuracy is " + str(level_BEST_accuracy) + "%"
            print "On the " + str(i) + "th level of the search tree"
            if (level_BEST_accuracy > BEST_accuracy):
                set_of_BEST_features_nodes = level_BEST_features_node
                print "Updated total features node! Old accuracy = " + str(BEST_accuracy) + " New accuracy = " \
                      + str(level_BEST_accuracy)
                BEST_accuracy = level_BEST_accuracy

    # display total best
    curly_braces_final = print_node_array(set_of_BEST_features_nodes)
    print "Finished search!! The best feature subset is " + curly_braces_final + ", which has an accuracy of " \
          + str(BEST_accuracy) + "%"


def print_node_array(node_array):
    node_array_string = "{"
    node_array_size = len(node_array)

    for i in range(node_array_size):
        node_array_string += str(node_array[i])
        if i != (node_array_size - 1):
            node_array_string += ","

    node_array_string += "}"

    return node_array_string



#main:
start_time = time.time()

print "Beginning search."
#forward_selection("CS170_SMALLtestdata__108.txt")
#forward_selection("CS170_SMALLtestdata__109.txt")
#forward_selection("CS170_SMALLtestdata__110.txt")
forward_selection("CS170_LARGEtestdata__108.txt")
#forward_selection("CS170_LARGEtestdata__109.txt")
#forward_selection("CS170_LARGEtestdata__110.txt")

print "--- %s seconds ---" % (time.time() - start_time)

# TODO create a class that iterates through 1 to 10 features and then 1 to 100 features



