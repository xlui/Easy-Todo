import os
from flask_script import Manager, Shell

from app import create_app, db
from app.models import TodoList, TodoItem

app = create_app(os.environ.get('FLASK_CONFIG') or 'default')
manager = Manager(app)

if __name__ == '__main__':
    def make_shell_context():
        return dict(app=app, db=db, TodoList=TodoList, TodoItem=TodoItem)


    manager.add_command('shell', Shell(make_context=make_shell_context))

    manager.run()
