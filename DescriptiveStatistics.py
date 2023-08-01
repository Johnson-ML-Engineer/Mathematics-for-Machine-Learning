def mean(data):
    return sum(data) / len(data)

def median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    else:
        return sorted_data[n // 2]

def mode(data):
    freq_dict = {}
    for num in data:
        freq_dict[num] = freq_dict.get(num, 0) + 1
    max_freq = max(freq_dict.values())
    return [num for num, freq in freq_dict.items() if freq == max_freq]

def range_data(data):
    return max(data) - min(data)

def variance(data):
    mean_value = mean(data)
    return sum((x - mean_value) ** 2 for x in data) / (len(data))

def standard_deviation(data):
    return variance(data) ** 0.5

# Test the functions
data_list = [5, 7, 2, 8, 4, 6, 3, 9, 1, 10, 3]
print("Mean:", mean(data_list))
print("Median:", median(data_list))
print("Mode:", mode(data_list))
print("Range:", range_data(data_list))
print("Variance:", variance(data_list))
print("Standard Deviation:", standard_deviation(data_list))
