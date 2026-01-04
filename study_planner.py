tasks=[]
while True:
  print("\nStudy planner")
  print("1. Add tasks")
  print("2. Show tasks")
  print("3. Exit")
  choise=input(" Choose an option (1-3):")
  if choise =="1":
    subject=input("Subject:")
    deadline=input("Deadline:")
    priority=input("Priority (low/medium/high):")
    task={
      "subjeck":subject,
      "deadlin":deadline,
      "priority":priority
    }
    task.append(task)
    print("Task added")
  elif choise =="2":
    if not tasks:
      print("No tasks yet")
    else:
      print("\nYour tasks:")
      for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['subject']} | {task['deadline']} | {task['priority']}")
  elif choise=="3":
    print("Good luck with your studies")
    break
  else:
    print("Invalid choise")
            
            
            
            
    
