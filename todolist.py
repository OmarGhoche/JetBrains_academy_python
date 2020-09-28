from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker

# Creates a DataBase to interact with
engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base = declarative_base()


# Via ORM, python objects act like rows in a Table, and the Table itself is a Class
class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='Nothing to-do!')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


# Creates the engine and Base
Base.metadata.create_all(engine)

# Starts a Session
Session = sessionmaker(bind=engine)
session = Session()

# I preferred not to use classes, just a simple while loop!
while True:
    print("1) Today's tasks\n2) Week's tasks\n3) All tasks\n4) Missed tasks\n5) Add task\n6) Delete task\n0) Exit")
    choice = input()
    # All commands are made in regards to the if, elif, else Control Flow
    if choice == "1":  # Because input is of <class 'str'>
        today = datetime.today()
        rows = session.query(Table).filter(Table.deadline == today.date()).all()  # rows == today's tasks
        print(f"\nToday {today.day} {today.strftime('%b')}:")
        if rows:  # If there is, at least, one row in the Table...
            for i in range(len(rows)):
                print(f"{i + 1}. {rows[i]}")  # Since arrays are ero-indexed, it is needed to add + 1 to make it start 1
        else:
            print("Nothing to do!")
        print()  # Those represent white spaces to make it more pleasant
    elif choice == "2":
        today = datetime.today()
        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        print()
        for i in range(7):
            current_day = today + timedelta(days=i)
            day_of_week = current_day.weekday()
            # To print the week of the day I used the `weekdays` array and the weekday()
            # If weekday() returns 2 for example, then weekdays[2] == "Wednesday"
            print(f"{weekdays[day_of_week]} {current_day.day} {current_day.strftime('%b')}:")
            rows = session.query(Table).filter(Table.deadline == current_day.date()).all()
            if rows:
                for j in range(len(rows)):
                    print(f"{j + 1}. {rows[j]}")
            else:
                print("Nothing to do!")
            print()
    elif choice == "3":
        rows = session.query(Table).order_by(Table.deadline).all()
        print("\nAll tasks:")
        for i in range(len(rows)):
            print(f"{i + 1}. {rows[i]}. {rows[i].deadline.day} {rows[i].deadline.strftime('%b')}")
        print()
    elif choice == "4":
        # Below: first filters only tasks with deadline before today, then order those by date!
        rows = session.query(Table).filter(Table.deadline < datetime.today().date()).order_by(Table.deadline).all()
        print("\nMissed tasks:")
        if rows:
            for i in range(len(rows)):
                print(f"{i + 1}. {rows[i]}. {rows[i].deadline.day} {rows[i].deadline.strftime('%b')}")
            print()
        else:
            print("Nothing is missed!\n")
    elif choice == "5":
        print("\nEnter task")
        the_task = input()
        print("Enter deadline")
        the_deadline = input()
        new_row = Table(task=the_task,
                        deadline=datetime.strptime(the_deadline, '%Y-%m-%d').date())
        session.add(new_row)
        session.commit()
        print("The task has been added!\n")
    elif choice == "6":
        rows = session.query(Table).order_by(Table.deadline).all()
        if rows:
            print("\nChoose the number of the task you want to delete:")
            for i in range(len(rows)):
                print(f"{i + 1}. {rows[i]}. {rows[i].deadline.day} {rows[i].deadline.strftime('%b')}")
            print()
            task_num = int(input())
            session.delete(rows[task_num - 1])
            session.commit()
            print("The task has been deleted!\n")
        else:
            print("\nNothing to delete!\n")
    else:
        # If `0` or any other key different than `1,2,3,4,5 and 6` are pressed along with `Enter`
        # The program quits!
        print("Bye!")
        break
