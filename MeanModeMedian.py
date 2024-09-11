from OCR_File import ocr, ocrText, displayData

def mean(data):
    sum = 0
    for x in data:
        sum += x 
    mean = sum/len(data)
    return mean

def mode(data):
    modes = {}; 
    seen = []; 
    for x in data:
        if x in seen:
            modes[x] += 1
        else:
            seen.append(x)
            modes[x] = 1
    highest = max(modes.values())
    mode = [k for k, v in modes.items() if v == highest]
    return highest, mode
    
        
def median(data):
    data.sort()
    n = len(data)
    if n % 2 == 1:
        median = data[n // 2]
    else:
   
        median = (data[n // 2 - 1] + data[n // 2]) / 2
        return median

def quartile(data, quartile_type):
    medianIndex = len(data) // 2

    if quartile_type == 'upper':
        upperHalf = data[medianIndex + 1:] if len(data) % 2 == 1 else data[medianIndex:]
        upperQuartile = median(upperHalf)
        return upperQuartile
    elif quartile_type == 'lower':
        lowerHalf = data[:medianIndex]
        lowerQuartile = median(lowerHalf)
        return lowerQuartile
    else:
        raise ValueError("quartile_type must be 'upper' or 'lower'")




image = "B:\ICloud\iCloudDrive\Coding\Python\Statistics\Training Imgs/EconData.png"
text, nums = ocrText(ocr(image))

mean = mean(nums)
mode = mode(nums)
medi = median(nums)

#print(f"mean is {mean}")
#print(f"mode is {mode}")
#print(f"median is {med}")

#print(displayData(text, nums))

print(nums)
print(min(nums))
print(max(nums))
print(mean)
print(mode)
print(medi)
print(quartile(nums, 'lower'))
print(quartile(nums, 'upper'))
