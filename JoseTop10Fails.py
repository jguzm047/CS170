import math
from joblib.numpy_pickle_utils import xrange



def main():
    print("Welcome\n")
    file_name = input('Type in text file:')
    new_data = []
    orig_data = []
    with open(file_name, "r") as f:
        datafile = f.readlines()
    print("finish reading")
    option = input("Select Algorithm: ")
    if option == 1:
        forward_selection(datafile)
    elif option == 2:
        print('Backward')
    elif option == 3:
        print('Own Alg')



def LOCV(datafile, current, feature_to_add=None):
    correct_counter = 0
    distance = {}
    if feature_to_add is not None:
        current.append(feature_to_add)
    for i in xrange(len(datafile)):
        neighbor = None
        min_distance = 999999
        for k in xrange(len(datafile)):
            if i != k:
                if distance.has_key((i, k)):
                    dist = distance[(i, k)]
                else:
                    if (i + 1) in current:
                        dist += (datafile[1][i] - datafile[1][i]) ** 2
                        math.sqrt(dist)
                        distance[(i, k)] = dist
                        distance[(k, i)] = dist

                    distance[(i, k)] = dist
                    distance[(k, i)] = dist
                if min_distance > dist:
                    min_distance = dist
                    neighbor = datafile[k]
        if neighbor is not None and neighbor != datafile[i]:
            if neighbor[0] == datafile[i][0]:
                correct_counter += 1
    percent = float(float(correct_counter) / float(len(datafile))) * 100
    return percent

def forward_selection(datafile):
    current_feature_ser = []
    print ('search begin\n')
    best_accuracy_all = (0, [])
    for i in xrange(len(datafile[0][1])):
        feature_to_add = -1
        best_accuracy = 0

        for k in xrange(len(datafile[0][1])):
            if(k + 1) not in current_feature_ser:
                accur = LOCV(datafile, current_feature_ser[:], k + 1)
                feature_ser = current_feature_ser[:]
                feature_ser.append(k + 1)
                print("using features:", feature_ser, "acc:", accur, "%")
                if accur >= best_accuracy:
                    best_accuracy = accur
                    feature_to_add = k + 1
        current_feature_ser.append(feature_to_add)

        if best_accuracy_all[0] >= best_accuracy:
            print ("Warning")
        else:
            best_accuracy_all = (best_accuracy, current_feature_ser[:])
        print (current_feature_ser, best_accuracy, best_accuracy_all[1], best_accuracy_all[0])
        return best_accuracy_all

#def chooseAlgorithmDATA():

if __name__ == "__main__":
    main()
