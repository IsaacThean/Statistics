import matplotlib.pyplot as plt
from OCR_File import ocr, ocrText
categories = []

class cate:
    def __init__(self, name, frequency):
        self.name = name 
        self.frequency = frequency 

def find_category(name):
    for i, category in enumerate(categories):
        if category.name == name:
            return i
    return -1  

def categoricalFrequency(data):
    for x in range(len(data)):
        index = find_category(data[x])
        if index == -1:  
            newCat = cate(data[x], 1)
            categories.append(newCat)
        else:  
            categories[index].frequency += 1
        
    # Collect data for pie chart
    labels = [cats.name for cats in categories]
    sizes = [cats.frequency for cats in categories]
  
    for cats in categories:
        percent = 100 * cats.frequency / len(data)
        print(cats.name, cats.frequency, f"{percent}%")
    
    # Plotting the pie chart
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.show()

categoricalFrequency(ocr('B:\ICloud\iCloudDrive\Coding\Python\Statistics\Training Imgs\img1.png'))