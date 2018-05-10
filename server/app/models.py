from datetime import datetime

from . import db


class TodoList(db.Model):
    __tablename__ = 'todo_list'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(128))
    isDelete = db.Column(db.Boolean, default=False)
    locked = db.Column(db.Boolean, default=False)
    # items
    items = db.relationship('TodoItem', lazy='dynamic')

    def json(self):
        return {
            'id': self.id,
            'content': self.content,
            'isDelete': self.isDelete,
            'locked': self.locked,
        }

    @staticmethod
    def init(count=5):
        from random import seed
        import forgery_py
        seed()
        for i in range(count):
            todo_list = TodoList(content=forgery_py.lorem_ipsum.sentence(),
                                 locked=forgery_py.basic.boolean())
            db.session.add(todo_list)
        db.session.commit()


class TodoItem(db.Model):
    __tablename__ = 'todo_item'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    date = db.Column(db.Date, default=datetime.date)
    list_id = db.Column(db.Integer, db.ForeignKey('todo_list.id'))

    def json(self):
        return {
            'id': self.id,
            'content': self.content,
            'date': self.date,
        }

    @staticmethod
    def init(item_count=7):
        import forgery_py
        for todo_list in TodoList.query.all():  # type: TodoList
            for i in range(item_count):
                item = TodoItem(content=forgery_py.lorem_ipsum.sentence(),
                                date=forgery_py.date.date(True),
                                list_id=todo_list.id)
                db.session.add(item)
            db.session.commit()
