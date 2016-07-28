#!/usr/bin/env python

from flask_migrate import Manager
from flask_migrate import MigrateCommand
from website import app

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
