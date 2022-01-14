import re

# indeces of data in each line
LNAME = 0
FNAME = 1
GRADE = 2
ROOM = 3
BUS = 4
GPA = 5
TLNAME = 6
TFNAME = 7

def main():
    print("Hello User!")
    
    while 1:
        query = raw_input("Enter your query: ")

        print("Query is: {}", query)

        if (re.match(r'Q(uit)?', query) is not None):
            exit()
        elif (re.match(r'I(nfo)?', query) is not None):
            info()
        elif (re.match(r'A(verage)?', query) is not None):
            n = re.search(r'\d+', query)
            number = n[0]
            average(number)
        # elif (re.match(r'S(tudent)?', query) is not None):
        #     lastname =
        #     bus =  
        #     if (!bus):
        #        student(lastname)
        #     else:
        #        student_bus(lastname, bus)   
        # elif (re.match(r'T(eacher)?', query) is not None):
        #     lastname =
        #     teacher(lastname)
        # elif (re.match(r'B(us)?', query) is not None):
        #     number =
        #     bus(number)
        # elif (re.match(r'G(rade)?', query) is not None):
        #     number =
        #     high =
        #     if high is None:
        #        grade(number)
        #     else:
        #        grade_hl(number, high)
        else:
            print("I'm sorry, that query was not recognized.")

    # print("Hi ", name)
    # num = len(sys.argv)
    # args = sys.argv
    # pyscript = sys.argv[0]  # this would be schoolsearch

def info():
    # For each grade (from 0 to 6) compute the total number of students in that grade.
    # Report the number of students in each grade in the format
    # <Grade>: <Number of Students>
    # sorted in ascending order by grade
    counts = []

    s = open("students.txt", "r")

    for line in s:
        l = list(line.split(","))
        counts[l[GRADE]] += 1

    i = 0
    while i < len(counts):
        print("{0}: {1}".format(i, counts[i]))
        i += 1

    print("info!")

def average(number):
    # Search the contents of the students.txt file for the entries where the student’s grade
    # matches the number provided in the instruction.
    
    # Compute the average GPA score for the entries found. Output the grade level (the number
    # provided in command) and the average GPA score computed.
    total = 0
    count = 0

    s = open("students.txt", "r")
    for line in s:
        l = list(line.split(","))
        if l[GRADE] == number:
            total += l[GPA]
            count += 1

    print("{0}: {1}".format(number, (total/count)))

    print("average!")   

def student(lastname):
    # search the contents of the students.txt file for the entry (or entries) for students with
    # the given last name.

    # For each entry found, print the last name, first name, grade and classroom assignment for
    # each student found and the name of their teacher (last and first name).

    print("student!")

def student_bus(lastname, bus):
    # search the contents of the students.txt file for the entry (or entries) for students with
    # the given last name.

    # For each entry found, print the last name, first name and the bus route the student takes.
    
    print("student bus!")

def teacher(lastname):
    # Search the contents of the students.txt file for the entries where the last name of the
    # teacher matches the name provided in the instruction.

    # For each entry found, print the last and the first name of the student.
        
    print("teacher!")

def grade(number):
    # Search the contents of the students.txt file for the entries where the student’s grade
    # matches the number provided in the instruction.

    # For each entry, output the name (last and first) of the student.

    print("grade!")

def bus(number):
    # Search the contents of the students.txt file for the entries where the bus route number
    # matches the number provided in the instruction.

    # For each such entry, output the name of the student (last and first) and their grade and classroom.

    print("bus!")

def grade_hl(number, high):
    # Search the contents of the students.txt file for the entries where the student’s grade
    # matches the number provided in the instruction.

    # If the H[igh] keyword is used in the command, find the entry in the students.txt file
    # for the given grade with the highest GPA. Report the contents of this entry (name of the
    # student, GPA, teacher, bus route).

    # If the L[ow] keyword is used in the command, find the entry in the students.txt file
    # for the given grade with the lowest GPA. Report the contents of this entry (name of the
    # student, GPA, teacher, bus route).    

    print("grade high/low!")

if __name__ == '__main__':
    main()