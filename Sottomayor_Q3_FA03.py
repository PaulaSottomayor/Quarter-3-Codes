steps = [
    [4500, 5200, 4800, 5500, 5300],  #Me
    [4000, 4100, 3900, 4200, 4600],  #Lia
    [6000, 5800, 5900, 6100, 6200]  #Jake
]

friend = ["Friend 1", "Friend 2", "Friend 3"]
for i in range(len(steps)):
    total= sum(steps[i])
    average = total / len(steps[i])
    minimum = min(steps[i])
    maximum = max((steps[i]))

    print(
        friend[i],
        "- Total:", total,
        "| Average:", average,
        "| Min:", minimum,
        "| Max:", maximum
    )