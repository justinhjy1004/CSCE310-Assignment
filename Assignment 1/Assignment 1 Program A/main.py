# Authors: Justin Ho and Abby Seibel
# Assignment 1A Weather Station Data

import sys

def parse_text(file):
    f = open(file, "r")
    num_lines = f.readline().strip()
    num_lines = int(num_lines)

    text_array = []
    for i in range(num_lines):
        text_array.append(f.readline())

    return text_array

def parse_weather_dict(array):

    weather_dict = {}

    # For each observation, the data is split into key and values and stored in a dict
    # The Key is time and Value is temperature
    for i in range(len(array)):
        time = array[i][0:16]
        temp = float(array[i][17:].strip())
        weather_dict[time] = temp

    return weather_dict

if __name__ == "__main__":
    # Obtain files and parse text
    file_a = parse_text(sys.argv[1])
    file_b = parse_text(sys.argv[2])

    # create dictionary that maps time to temp
    weather_a = parse_weather_dict(file_a)
    weather_b = parse_weather_dict(file_b)

    # Obtain the set of time in A and in B
    set_time_a = set(weather_a.keys())
    set_time_b = set(weather_b.keys())

    # Obtain time that is in A but not in B (A-B)
    set_time_diff_a = set_time_a.difference(set_time_b)
    # Obtain time that is in B but not in A (A-B)
    set_time_diff_b = set_time_b.difference(set_time_a)

    # Obtained the time stamp that exists in both A and B
    time_shared = set_time_a.intersection(set_time_b)

    # iterate each time stamp that is shared
    for time in time_shared:
        temp_a = weather_a.get(time)
        temp_b = weather_b.get(time)

        # Print out inconsistent data given time stamp
        if(temp_a != temp_b):
            print("Inconsistent Data (%s): A: %.2f B: %.2f" % (time, temp_a, temp_b))

    # Print time difference for data in set A but not in B
    for time in set_time_diff_a:
        print("Missing Data (%s) in data set A but not in B" % (time))

    # Print time difference for data in set B but not in A
    for time in set_time_diff_b:
        print("Missing Data (%s) in data set B but not in A" % (time))

