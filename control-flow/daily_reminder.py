task = input("Enter your task: ")
task_priority = input("Priority (high/medium/low): ").lower().strip()
time_bound = input("Is it time-bound?(yes/no): ")
match task_priority:
    case "high":
        if time_bound=="yes":
         print(f"Reminder: {task} is a high priority task that requires attention today")
        else:
           print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")
    case "medium":
      if time_bound=="yes":
         print(f"Reminder: {task} is a medium priority task that requires attention today")
      else:
         print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")
    case "low":
      if time_bound=="yes":
         print(f"Reminder: {task} is a low priority task that requires attention today")
      else:
        print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")