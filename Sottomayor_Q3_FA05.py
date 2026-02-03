names = ["Me", "Lia", "Jake"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
steps = [
  [4500, 5200, 4800, 5000, 5300],
  [4000, 4100, 3900, 4200, 4600],
  [6000, 5800, 5900, 6100, 6200]
]

total_steps_daily = []

for day in range(len(days)):
    total = 0
    for participant in range(len(steps)):
        total += steps[participant][day]
    total_steps_daily.append(total)

for i in range(len(days)):
    print(f"Total steps on {days[i]}: {total_steps_daily[i]}")

most_active_day = total_steps_daily.index(max(total_steps_daily))
max_steps = max(total_steps_daily)
print("Most active day: ",days[most_active_day], "with", max_steps, "steps.")