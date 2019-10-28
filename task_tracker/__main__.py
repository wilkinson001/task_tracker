import argparse
from .task import Task, get_tasks, save_task

def main():
        args = setup_parsers()
        if args.new:
                new_task = Task(*args.new)
                save_task(new_task)
        if args.list:
                get_tasks()


def setup_parsers():
        parser = argparse.ArgumentParser(description='Process some integers.')  
        parser.add_argument('--new', type=str, nargs='+', help='Creates new task')
        return parser.parse_args()

if __name__ == '__main__':
        main()