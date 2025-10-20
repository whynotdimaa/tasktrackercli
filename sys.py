import sys
from main import TaskManager
args = sys.argv[1:]
if not args:
    print("Введи команду(add , list , update , delete, done) :")
    sys.exit()
command = args[0]
tm = TaskManager("ab.json")
if command == "add":
    description = " ".join(args[1:])
    tm.addtasks(description)
elif command == "list":
    for t in tm.listall():
        print(t.to_dict())
elif command == "update":
    id = int(args[1])
    new_desc = " ".join(args[2:])
    tm.updatetasks(id, new_desc)
elif command == "delete":
    id = int(args[1])
    tm.deletetasks(id)
elif command == "done":
    id = int(args[1])
    for task in tm.tasks:
        if task.id == id:
            task.mark_completed()
            task.update()
            tm.save()
            print(f"Task {id} done")
            break
    else:
        print(f"Task {id} not found")
else:
    print("UNKNOWN COMMAND")

