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

        print("Query is: {0}".format(query))

        if (re.match(r'Q(uit)?', query) is not None):
            exit()
        elif (re.match(r'I(nfo)?', query) is not None):
            info()
        elif (re.match(r'A(verage)?', query) is not None):
            n = re.search(r'\d+', query)
            number = n.group()
            if (number > 6):
                print("\tERROR: Grades Available - 0 to 6")
                continue
            average(number)
        elif (re.match(r'S(tudent)?', query) is not None):
            l = query.split(" ")
            lastname = l[1]
            bus = re.search(r'B(us)?', query)
            if (bus is None):
                student(lastname)
            else:
                student_bus(lastname)
        elif (re.match(r'T(eacher)?', query) is not None):
            l = query.split(" ")
            lastname = l[1]
            teacher(lastname)
        elif (re.match(r'B(us)?', query) is not None):
            n = re.search(r'\d+', query)
            number = n.group()
            busroute(number)
        elif (re.match(r'G(rade)?', query) is not None):
            n = re.search(r'\d+', query)
            number = n.group()
            high = re.search(r'H(igh)?', query)
            low = re.search(r'L(ow)?', query)
            if (high is None and low is None):
               grade(number)
            elif (high is not None):
                grade_high(number)
            else:
                grade_low(number)
        else:
            print("I'm sorry, that query was not recognized.")

def info():
    counts = [0] * 7

    s = open("students.txt", "r")

    for line in s:
        l = list(line.split(","))
        counts[int(l[GRADE])] += 1

    i = 0
    while i < len(counts):
        print("\t{0}: {1}".format(i, counts[i]))
        i += 1


def average(number):
    total = 0
    count = 0

    s = open("students.txt", "r")
    for line in s:
        l = list(line.split(","))
        if l[GRADE] == number:
            total += float(l[GPA])
            count += 1

    print("\t{0}: {1}".format(number, (total/count)))


def student(lastname):
    s = open("students.txt", "r")
    for line in s:
        l = list(line.split(","))
        if l[LNAME] == lastname:
            print("\t{0}, {1}: {2}, {3}, {4}, {5}".format(lastname, l[FNAME], l[GRADE], l[ROOM], l[TLNAME], l[TFNAME]))


def student_bus(lastname):
    s = open("students.txt", "r")
    for line in s:
        l = list(line.split(","))
        if l[LNAME] == lastname:
            print("\t{0}, {1}: {2}".format(lastname, l[FNAME], l[BUS]))
 

def teacher(lastname):
    s = open("students.txt", "r")
    for line in s:
        l = list(line.split(","))
        if l[TLNAME] == lastname:   
            print("\t{0}, {1}".format(l[LNAME], l[FNAME]))


def grade(number):
    s = open("students.txt", "r")
    for line in s:
        l = list(line.split(","))
        if l[GRADE] == number:
            print("\t{0}, {1}".format(l[LNAME], l[FNAME]))


def busroute(number):
    s = open("students.txt", "r")
    for line in s:
        l = list(line.split(","))
        if l[BUS] == number:
            print("\t{0}, {1}: {2}, {3}".format(l[LNAME], l[FNAME], l[GRADE], l[ROOM]))        


def grade_high(number):
    gpa = 0
    save = ""

    s = open("students.txt", "r")
    for line in s:
        l = list(line.split(","))
        if l[GRADE] == number:
            if float(l[GPA]) > gpa:
                gpa = float(l[GPA])
                save = line

    save = list(save.split(","))
    print("\t{0}, {1}: {2}, {3}, {4}, {5}".format(save[LNAME], save[FNAME], save[GPA], save[TLNAME], save[TFNAME].rstrip(), save[BUS]))


def grade_low(number):
    gpa = 100
    save = ""

    s = open("students.txt", "r")
    for line in s:
        l = list(line.split(","))
        if l[GRADE] == number:
            if float(l[GPA]) < gpa:
                gpa = float(l[GPA])
                save = line

    save = list(save.split(","))
    print("\t{0}, {1}: {2}, {3}, {4}, {5}".format(save[LNAME], save[FNAME], save[GPA], save[TLNAME], save[TFNAME].rstrip(), save[BUS]))


if __name__ == '__main__':
    main()