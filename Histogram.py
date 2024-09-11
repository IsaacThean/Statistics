import matplotlib.pyplot as plt
import math
import pandas as pd
classWidth = 0

def data_range(data):
    min_value = min(data)
    max_value = max(data)
    range_value = max_value - min_value
    return range_value

def sortData(data):
    sortedArray = sorted(data)
    return sortedArray

def intervals(data):
    global classWidth
    num = int(input("How many classes do you want: "))
    ran = data_range(data)
    classWidth = math.ceil(ran / num)
    
    intervalSet = [[] for _ in range(num)]
    
    min_value = min(data)
    
    for value in data:
        index = min(num - 1, (value - min_value) // classWidth)
        intervalSet[index].append(value)

    return intervalSet

def frequency(intervals):
    freq = [len(interval) for interval in intervals]
    return freq

def categories(intervalSet):
    labels = []
    start = min(data)
    for i in range(len(intervalSet)):
        end = start + classWidth
        label = f"{int(start)} <= t < {int(end)}"
        labels.append(label)
        start = end
    return labels

def cumFreq(freq):
    cumf = []
    sum = 0
    for num in freq:
        sum += num
        cumf.append(sum)
    return cumf

def endPoints(intervalSet):
    endpoints = []
    start = min(data)
    for _ in intervalSet:
        end = start + classWidth
        endpoints.append(end)
        start = end
    return endpoints

def midPoints(intervalSet):
    midpoints = []
    start = min(data)
    for _ in intervalSet:
        end = start + classWidth
        midpoint = (start + end) / 2
        midpoints.append(midpoint)
        start = end
    return midpoints

def histogram(labels, freq):
    plt.bar(labels, freq)
    plt.xlabel('Intervals')
    plt.ylabel('Frequency')
    plt.tight_layout()

def ogive(endpoints, freq):
    plt.plot(endpoints, freq, marker="o")
    plt.xlabel('Values')
    plt.ylabel('Cumulative Frequency')
    plt.grid(True)

def plot(mid, endpoints, cumfreq):
    plt.bar(mid, cumfreq, width=classWidth, color="lightblue", edgecolor="blue")
    plt.plot(endpoints, cumfreq, marker="o", color="black")
    plt.ylabel('Cumulative Frequency')
    plt.xlabel('Values')
    plt.show()

def freqTable(labels, frequency, cumfreq):
    table = {
        "Ranges:": labels,
        "Frequencies": frequency,
        "Cumulative Frequencies": cumfreq
    } 
    df = pd.DataFrame(table)
    html_table = df.to_excel(index=False)
    print(html_table)

# Input and processing
dataInput = input("Input data: ")
data = list(map(int, dataInput.split()))
dataset = sortData(data)
inter = intervals(dataset)

freq = frequency(inter)
labels = categories(inter)
endpoints = endPoints(inter)
cumfreq = cumFreq(freq)
mid = midPoints(inter)

# Output the results
print(f"Interval set: {inter}") 
print(f"Midpoints: {mid}") 
print(f"Frequencies: {freq}") 
print(f"Endpoints: {endpoints}") 
print(f"CumFrequencies: {cumfreq}") 
print(f"labels: {labels}") 
# Plot the histogram and ogive
#histogram(labels, freq)
#ogive(endpoints, cumfreq)
plot(mid, endpoints, cumfreq)
freqTable(labels, freq, cumfreq)
