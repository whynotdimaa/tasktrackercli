import datetime
from pathlib import Path
import json

class Task:
    def __init__(self, id, description, status , createdat, updatedat):
        self.id = id
        self.description = description
        self.status = status
        self.createdat = createdat
        self.updatedat = updatedat
    def mark_in_progress(self):
        self.status = 'in-progress'
    def mark_completed(self):
        self.status = 'done'
    def to_dict(self):
        return {
            'id': self.id,
            'description': self.description,
            'status': self.status,
            'createdat': self.createdat,
            'updatedat': self.updatedat,
        }
    def update(self):
        self.updatedat = datetime.datetime.now().isoformat()
    @staticmethod
    def from_dict(data):
        return Task(
            id=data['id'],
            description = data['description'],
            status = data['status'],
            createdat = data['createdat'],
            updatedat = data['updatedat'],
    )
class TaskManager:
    def __init__(self, filepath):
        self.tasks = []
        self.filepath = Path(filepath)
        try:
            with open(self.filepath) as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            print('File not found')
        else:
            print("File found")
    def listall(self):
        return self.tasks
    def addtasks(self , description):
        new_id = len(self.tasks) + 1
        now = datetime.datetime.now().isoformat()

        new_task = Task(new_id, description, "todo", now, now)
        self.tasks.append(new_task)

        with open (self.filepath, 'w') as f:
            json.dump([t.to_dict() for t in self.tasks], f)
        print("Task added")
    def removetasks(self , description):




tm = TaskManager("ab.json")
