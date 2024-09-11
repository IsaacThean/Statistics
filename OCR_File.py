import easyocr
import pandas



def ocr(img):
   
    reader = easyocr.Reader(['en'], gpu = True)
    result = reader.readtext(img)
    return result

def ocrNums(data):
    nums = []
    for (bbox, text, prob) in data:
        if text.isdigit():
            nums.append(int(text))
    return nums

def ocrText(data):
    points = []
    text = []
    nums = []
    class datapoint:
        def __init__(self, name, value):
            self.name = name
            self.value = value
    for (bbox, x, prob) in data: 
        if x.isdigit():
            nums.append(int(x))
        elif any(char.isalpha() for char in x):
            text.append(x)
    text.pop(0)
    text.pop(0)
    return text, nums
#print(ocrText(ocr(image)))

def displayData(text, nums):
    df = pandas.DataFrame({
        "X": text,
        "Y": nums
    })
    return df



#print(displayData(text, nums))
    


