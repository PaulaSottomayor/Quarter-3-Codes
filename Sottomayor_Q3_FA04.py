names = ["Me", "Lia", "Jake"]

steps = [

  [4500, 5200, 4800, 5000, 5300],

  [4000, 4100, 3900, 4200, 4600],

  [6000, 5800, 5900, 6100, 6200]

]

print("Total steps for each person: ")
totals = []
for i in range(len(steps)):
    total = sum(steps[i])
    totals.append(total)
    print(names[i],":", total)

highest_total = max(totals)
lowest_total = min(totals)
highest_index = totals.index(highest_total)
difference = highest_total - lowest_total

print("Person with the highest total: ", names[highest_index], "with", highest_total, "steps.")
print("Difference between the highest and lowest total: ", difference)