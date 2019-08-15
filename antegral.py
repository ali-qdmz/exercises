def printme(x):
   z = float(x)
   return float(z)

steps = input('insert steps')
upper_limit = input('insert upper limit')
down_limit = input('insert down limit')
steps = int(steps)
inner_steps = ((float(upper_limit)-float(down_limit))/float(steps))
upper_limit = float(upper_limit)
down_limit = float(down_limit)
total_area = 0
for i in range(steps):
    area = 0
    area = float(printme(down_limit))*float(inner_steps)
    down_limit = float(down_limit) + float(inner_steps)
    total_area = float(area) + float(total_area)
    
print(total_area)
