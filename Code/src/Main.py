import csv

from Data import Data
from FindSolution import FindSolution

import pandas as pd



def Main():
    '''
    Config:
    '''

    POPULATION_SIZE = 9
    NUMBER_OF_ELITE_SCHEDULES = 1
    TOURNAMENT_SELECTION_SIZE = 3
    MUTATION_RATE = 0.1

    data = Data('./data/Room.csv', './data/MeetingTime.csv',
                './data/Instructor.csv', './data/Department.csv',
                './data/Course.csv')

    find_solution = FindSolution(data, POPULATION_SIZE, NUMBER_OF_ELITE_SCHEDULES, TOURNAMENT_SELECTION_SIZE, MUTATION_RATE)
    timetable = find_solution.getTimeTable()

    timetable.sort(key=lambda x: x.getMeetingTime().getId())

    department = []
    course = []
    instructor = []
    room = []
    day = []
    time = []

    for i in range(len(timetable)):
        department.append(timetable[i].getDept().getName())
        course.append(timetable[i].getCourse().getName())
        instructor.append(timetable[i].getInstructor().getName())
        room.append(timetable[i].getRoom().getName())
        day.append(timetable[i].getMeetingTime().getDay())
        time.append(timetable[i].getMeetingTime().getTime())

    timetable_data = { 'Shift': time,
                        'Day': day,
                        'Room': room,
                        'Course': course,
                        'Instructor': instructor,
                        'Department': department
                    }

    timetable_df = pd.DataFrame(data=timetable_data)
    timetable_df.to_csv('./export/Timetable.csv', sep=',', encoding='utf-8')

    return 0

if __name__ == '__main__':
    Main()