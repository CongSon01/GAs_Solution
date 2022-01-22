'''
Meeting time
    sort by id
'''
class MeetingTime:
    def __init__(self, id, day: str, time: str):
        self._id = id
        self._day = day
        self._time = time

    def getId(self): return self._id
    def getDay(self): return self._day
    def getTime(self): return self._time

'''
Room:
    number
    name
    seat_capacity
'''
class Room:
    def __init__(self, id, name: str, seat_capacity: int):
        self._id = id
        self._name = name
        self._seet_capacity = seat_capacity

    def getId(self): return self._id
    def getName(self): return self._name
    def getCapacity(self): return self._seet_capacity

'''
Instructor

'''
class Instructor:
    def __init__(self, id, name):
        self._id = id
        self._name = name

    def getId(self): return self._id
    def getName(self): return self._name

'''
Course:

'''
class Course:
    def __init__(self, id, name: str, instructor: list[Instructor], max_number_of_students: int):
        self._number = id
        self._name = name
        self._instructor = instructor
        self._max_students = max_number_of_students

    def getId(self): return self._number
    def getName(self): return self._name
    def getInstructor(self): return self._instructor
    def getMaxStudent(self): return self._max_students
    def __str__(self): return self._name

'''
Deparment:

'''
class Department:
    def __init__(self, name: str, course: list[Course]):
        self._name = name
        self._course = course

    def getName(self): return self._name
    def getCourse(self): return self._course

'''
Class:
After Scheduling we have classes
'''
class Class:
    def __init__(self, id, department: Department, course: Course):
        self._id = id
        self._dept = department
        self._course = course
        self._instructor: Instructor = None
        self._meeting_time: MeetingTime = None
        self._room: Room = None

    '''
    Accessor
    '''
    def getId(self): return self._id
    def getDept(self): return self._dept
    def getCourse(self): return self._course
    def getInstructor(self): return self._instructor
    def getMeetingTime(self): return self._meeting_time
    def getRoom(self): return self._room

    '''
    Mutator
    '''
    def setInstructor(self, instructor): self._instructor = instructor
    def setMeetingTime(self, meeting_time): self._meeting_time = meeting_time
    def setRoom(self, room): self._room = room

    '''
    toString():
    '''
    def __str__(self):
        return  str(self._dept.getName()) + ', ' + str(self._course.getName()) + ', ' + \
                str(self._room.getName()) + ', ' + str(self._instructor.getName()) + ', ' + \
                str(self._meeting_time.getDay()) + ', ' + \
                str(self._meeting_time.getTime())