from uuid import uuid4

class Task:
    owner = None
    col_header = "name | description | priority\n"

    def __init__(self, name, description, priority=0):
        self.name = name
        self.description = description
        self.priority = priority
        self.uid = uuid4()

    def __repr__(self):
        self.col_header += f"{self.name} | {self.description} | {self.priority}"
        return col_header


def get_tasks():
    pass

def save_task()
    pass