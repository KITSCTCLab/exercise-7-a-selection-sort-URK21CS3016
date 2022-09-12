from typing import List

def selectionSort(array, size) -> List[int]:
  # Write your code here
  for i in range(0,n-2):
    min=i
    for j in range(1,n-2):
      if List[min]>List[j]:
        min=j
    swap[List[i],List[min]]

# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(selectionSort(data, len(data)))
