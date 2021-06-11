import os
import math
import shutil
import numpy as np
import matplotlib.pyplot as plt
import csv
from scipy import stats

# hypothesis
h0 = "Data from file matches Benford distribution"
h1 = "Data from file is not matching Benford distribution"

# significance level
alpha = 0.05

# critical value at p = 0.05
critical_value = 15.51

# get path to folder with data files
path_to_data = os.getcwd() + '\\Benford\\'

expected = [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]

def plot(filename, log_directory, expected, observed, chi_square, p_value):
    labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    x = np.arange( len(labels) )
    width = 0.35

    fig, ax = plt.subplots(figsize=(16,8))
    rects1 = ax.bar(x - width / 2, expected, width, label='Expected', color='black')
    rects2 = ax.bar(x + width / 2, observed, width, label='Observed', color='red')

    # text
    ax.set_ylabel('Repetitions count')
    ax.set_title(filename)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_xlabel("chi-square: " + str(chi_square) + " / p-value: " + str(p_value))
    ax.legend()

    ax.bar_label(rects1, padding=5)
    ax.bar_label(rects2, padding=5)


    fig.tight_layout()

    plt_image = filename.split(".")[0] + ".png"

    plt.savefig( os.path.join(log_directory, plt_image) )

    plt.close(fig)

def log(filename, expected, observed, zero_values, chi_square, p_value):
    # getting path for log folder
    current_directory = os.getcwd()
    log_directory = os.path.join(current_directory, filename.split(".")[0])

    # clear previous log folder
    if os.path.exists(log_directory):
        shutil.rmtree(log_directory, ignore_errors=True)

    # create folder for log file and plot
    os.makedirs(log_directory)

    # create log_file in that folder
    log = open( os.path.join(log_directory, "LOG " + filename), "w" )

    # write all information
    log.write("[ ZERO VALUES ] = ")
    log.write(str(zero_values))
    log.write('\n')
    log.write("[ EXPECTED ] = [")
    log.write(', '.join(str(x) for x in expected))
    log.write(']\n')
    log.write("[ OBSERVED ] = [")
    log.write(', '.join(str(x) for x in observed))
    log.write(']\n')
    log.write("[ P-VALUE ] = ")
    log.write(str(p_value))
    log.write('\n')
    log.write("[ SIGNIFICANCE LEVEL ] = ")
    log.write(str(alpha))
    log.write('\n')
    log.write("[ CHI-SQUARE ] = ")
    log.write(str(chi_square))
    log.write('\n')
    log.write("[ CRITICAL VALUE ] = ")
    log.write(str(critical_value))
    log.write('\n')
    log.write("[ CHI-SQUARE < CRITICAL VALUE ] = ")
    log.write( str(chi_square < critical_value) )
    log.write('\n')

    if(chi_square < critical_value):
        conclusion = h0
    else:
        conclusion = h1

    log.write("[ CONCLUSION ] = ")
    log.write(conclusion)

    # save plot image
    plot(filename, log_directory, expected, observed, chi_square, p_value)

    return chi_square < critical_value

def summary(proper, fraud):
    print("[LOG] Possible number of frauds: " + str( len(fraud) ))
    for filename in fraud:
        print(filename)

    print("[LOG] Possible number of proper data:" + str( len(proper) ))
    for filename in proper:
        print(filename)

raw_data = dict()
fraud = []
proper = []

def process_data(raw_data):
    # sort data by it's p-value
    result_data = dict()
    for filename, chi_square in raw_data.items():

        if chi_square >= critical_value:
            result_data[filename] = 1
        else:
            result_data[filename] = round(chi_square / critical_value, 2)

    #
    sorted_by_p_value = sorted(result_data.items(), key=lambda kv: kv[1])

    i = 1

    csv_data = []

    for tuple in sorted_by_p_value:
        csv_row = [ tuple[0], round(tuple[1], 2), i]
        csv_data.append(csv_row)
        i += 1

    csv_data = sorted(csv_data, key=lambda x: x[0])

    return csv_data

def write_to_csv(final_data):
    with open ('452758.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=";")
        labels = ['filename', 'coefficient', 'ordinal number']
        writer.writerow(labels)
        writer.writerows(final_data)



# iterate over every file in folder
for filename in os.listdir(path_to_data):
    # get only .txt files
    if filename.endswith('.txt'):
        # open every file in folder count lines with 0
        zero_values = 0
        # labels   [1, 2, 3, 4, 5, 6, 7, 8, 9]
        observed = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        print("[LOG] Opening data sample: " + filename)
        with open(path_to_data + filename, 'r') as data_file:
            # read every line of file
            for line in data_file:
                leading_number = int(line[0])
                # ignore 0 values
                if leading_number != 0:
                    observed[ leading_number - 1 ] += 1

            # after analysing file pass it to chi-squared test
            chi_squared_test = stats.chisquare(observed, expected)
            chi_square = chi_squared_test[0]
            p_value = chi_squared_test[1]

            if log(filename, expected, observed, zero_values, chi_square, p_value):
                proper.append(filename)
            else:
                fraud.append(filename)

            # chi-square will be re-used for scaling results in .csv
            raw_data[filename] = chi_square

        print("----------------------------------------------------------------------------------")

print("[LOG] File analysis complete")
summary(proper, fraud)
final_data = process_data(raw_data)
write_to_csv(final_data)
