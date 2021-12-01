lines = []
with open("day1.txt", "r") as file:
   lines = [int(line.strip()) for line in file.readlines()]

count = 0
for i in range(len(lines) - 1):
   if lines[i + 1] > lines[i]:
      count += 1 

print(count)

count2 = 0
for i in range(1, len(lines) - 2):
   if lines[i - 1] + lines[i] + lines[i+1] < lines[i] + lines[i+1] + lines[i+2]:
      count2 += 1 

print(count2)