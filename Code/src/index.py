from flask import Flask, render_template, request, jsonify
from flask_bootstrap import Bootstrap
import requests
import csv

from Data import Data
from FindSolution import FindSolution

import pandas as pd

from werkzeug.utils import redirect

data_timeTable = "./export/Timetable.csv"

data_Course = "./data/Course.csv"
data_Instructor = "./data/Instructor.csv"
data_MeetingTime = "./data/MeetingTime.csv"
data_Department = "./data/Department.csv"
data_Rooms = "./data/Room.csv"

app = Flask(__name__)
Bootstrap(app)



@app.route('/generation_text', methods=['GET'])
def generation_text():
    return render_template('generation_text.html')

@app.route('/export', methods=['GET', 'POST'])
def export():
    POPULATION_SIZE = 9
    NUMBER_OF_ELITE_SCHEDULES = 1
    TOURNAMENT_SELECTION_SIZE = 3
    MUTATION_RATE = 0.1

    data = Data(data_Rooms, data_MeetingTime,
                data_Instructor, data_Department,
                data_Course)

    find_solution = FindSolution(data, POPULATION_SIZE, NUMBER_OF_ELITE_SCHEDULES, TOURNAMENT_SELECTION_SIZE, MUTATION_RATE)
    if (find_solution == False):
        return "HELLo"
    else:
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
        return redirect("/")

@app.route('/')
def index():
    with open(data_timeTable) as csv_file:
        data = csv.reader(csv_file, delimiter=',')
        first_line = True
        data_timeTables = []
        for row in data:
            if not first_line:
                data_timeTables.append({
                    "Shift":row[1],
                    "Day":row[2],
                    "Room":row[3],
                    "Course":row[4],
                    "Instructor":row[5],
                    "Department":row[6]
                })
            else:
                first_line = False
        return render_template("index.html", timeTables = data_timeTables)

@app.route('/listRoom', methods=['GET'])
def listRoom():
    with open(data_Rooms) as csv_file:
        data_rooms = csv.reader(csv_file, delimiter=',')
        first_line = True
        data_Room = []
        for row in data_rooms:
            if not first_line:
                data_Room.append({
                    "name":row[1],
                    "seat_capacity":row[2]
                })
            else:
                first_line = False
        return render_template("Room/listRoom.html", Rooms = data_Room)

@app.route('/addRoom', methods=["GET", "POST"])
def addRoom():
    if request.method == "GET":
        return render_template("Room/addRoom.html")
    elif request.method == "POST":
        roomdata = dict(request.form)
        new_name = roomdata["name"]
        seat_capacity = int(roomdata["seat_capacity"])
        with open(data_Rooms, "r+", newline='') as csv_file:
            data_rooms = csv.reader(csv_file, delimiter=',')
            id_room = len(list(data_rooms)) - 1
            List_room=[id_room, new_name,seat_capacity]
            data = csv.writer(csv_file)
            data.writerow(List_room)
            csv_file.close()
        return jsonify({'new_name' : new_name})

@app.route('/listCourse', methods=['GET'])
def listCourse():
    with open(data_Course) as csv_file:
        data_courses = csv.reader(csv_file, delimiter=',')
        first_line = True
        data_course = []
        for row in data_courses:
            if not first_line:
                data_course.append({
                    "name":row[1],
                    "instructor_id":row[2],
                    "max_number_of_students":row[3]
                })
            else:
                first_line = False
        return render_template("Course/listCourse.html", courses = data_course)

@app.route('/addCourse', methods=["GET" , "POST"])
def addCourse():
    if request.method == "GET":
        with open(data_Instructor) as csv_file:
            data_ins = csv.reader(csv_file, delimiter=',')
            first_line = True
            data_instructor = []
            for row in data_ins:
                if not first_line:
                    data_instructor.append({
                        "id":row[0],
                        "professor":row[1]
                    })
                else:
                    first_line = False
            return render_template("Course/addCourse.html", instructors = data_instructor)
    elif request.method == "POST":
        course_data = dict(request.form)
        name = course_data["name"]
        instructor_id = int(course_data["instructor_id"])
        max_number_of_students = int(course_data["max_number_of_students"])
        with open(data_Course, "r+", newline='') as csv_file:
            data_course_s = csv.reader(csv_file, delimiter=',')
            id_course = len(list(data_course_s)) - 1
            List_course = [id_course, name,instructor_id , max_number_of_students]
            data = csv.writer(csv_file)
            data.writerow(List_course)
            csv_file.close()
        return redirect("/listCourse")
        
if __name__ == '__main__':
	app.run(debug=True)