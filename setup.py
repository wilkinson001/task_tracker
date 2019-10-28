from setuptools import setup
setup(
    name = 'tasktracker',
    version = '0.1.0',
    packages = ['task_tracker',],
    entry_points = {
        'console_scripts': [
            'task_tracker = task_tracker.__main__:main'
        ]
    })