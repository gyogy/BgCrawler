import sys
from project.db.controller import DBController

if __name__ == '__main__':

    choice = sys.argv[1]
    if choice == 'boot':
        dbc = DBController()
