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
    
    while 1:
        query = raw_input("Enter your query: ")

        if (re.match(r'Q(uit)?', query) is not None):
            exit()
        elif (re.match(r'I(nfo)?', query) is not None):
            info()
        elif (re.match(r'A(verage)?:', query) is not None):
            n = re.search(r'\d+', query)
            number = n.group()
            average(number)
        elif (re.match(r'S(tudent)?:', query) is not None):
            l = query.split(" ")
            lastname = l[1]
            bus = re.search(r'B(us)?', query)
            if (bus is None):
                student(lastname)
            else:
                student_bus(lastname)
        elif (re.match(r'T(eacher)?:', query) is not None):
            l = query.split(" ")
            lastname = l[1]
            teacher(lastname)
        elif (re.match(r'B(us)?:', query) is not None):
            n = re.search(r'\d+', query)
            number = n.group()
            busroute(number)
        elif (re.match(r'G(rade)?:', query) is not None):
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
            print("I'm sorry, that query was not recognized. Please try again.")

        print("")

def info():
    # End result variable
    counts = [0] * 7

    # Open File
    try: 
        s = open("students.txt", "r")
    except:
        print("students.txt not found, exiting now")
        exit()

    # Parse file for student grade
    for line in s:
        l = list(line.split(","))
        counts[int(l[GRADE])] += 1

    # Print results
    i = 0
    while i < len(counts):
        print("{0}: {1}".format(i, counts[i]))
        i += 1


def average(number):
    # Only grades 0-6 possibble
    if (int(number) > 6):
        print("")
        return

    # Calculation variables
    total = 0
    count = 0

    # Open file
    try: 
        s = open("students.txt", "r")
    except:
        print("students.txt not found, exiting now")
        exit()
    
    # Parse file for GPAs in the provided grade
    for line in s:
        l = list(line.split(","))
        if l[GRADE] == number:
            total += float(l[GPA])
            count += 1

    # If no students found, print empty line
    if (count == 0):
        print("")
        return

    # Else, print results
    print("{0},{1}".format(number, (total/count)))


def student(lastname):
    found = False
    
    # Open file
    try: 
        s = open("students.txt", "r")
    except:
        print("students.txt not found, exiting now")
        exit()

    # Parse file for students with provided lastname, print results
    for line in s:
        l = list(line.split(","))
        if l[LNAME] == lastname:
            found = True
            print("{0},{1},{2},{3},{4},{5}".format(lastname, l[FNAME], l[GRADE], l[ROOM], l[TLNAME], l[TFNAME].rstrip()))

    # If no students found, print empty line
    if found is False:
        print("")

def student_bus(lastname):
    found = False

    # Open file
    try: 
        s = open("students.txt", "r")
    except:
        print("students.txt not found, exiting now")
        exit()

    # Parse file for students with provided lastname, print bus route  
    for line in s:
        l = list(line.split(","))
        if l[LNAME] == lastname:
            found = True
            print("{0},{1},{2}".format(lastname, l[FNAME], l[BUS]))
 
    # If not students found, print empty line
    if found is False:
        print("")

def teacher(lastname):
    found = False

    # Open file
    try: 
        s = open("students.txt", "r")
    except:
        print("students.txt not found, exiting now")
        exit()
        
    # Parse file for students with provided teacher, print results
    for line in s:
        l = list(line.split(","))
        if l[TLNAME] == lastname:   
            found = True
            print("{0},{1}".format(l[LNAME], l[FNAME]))

    # If no students found, print empty line
    if found is False:
        print("")

def grade(number):
    # Only grades 0-6 possibble
    if (int(number) > 6):
        print("")
        return

    found = False

    # Open file
    try: 
        s = open("students.txt", "r")
    except:
        print("students.txt not found, exiting now")
        exit()

    # Parse file for students in provided grade, print results 
    for line in s:
        l = list(line.split(","))
        if l[GRADE] == number:
            found = True
            print("{0},{1}".format(l[LNAME], l[FNAME]))

    # If no students found, print empty line
    if found is False:
        print("")

def busroute(number):
    found = False

    # Open file
    try: 
        s = open("students.txt", "r")
    except:
        print("students.txt not found, exiting now")
        exit()

    # Parse file for students in provided bus route, print results 
    for line in s:
        l = list(line.split(","))
        if l[BUS] == number:
            found = True
            print("{0},{1},{2},{3}".format(l[LNAME], l[FNAME], l[GRADE], l[ROOM]))        

    # If no students found, print empty line
    if found is False:
        print("")

def grade_high(number):
    # Only grades 0-6 possible
    if (int(number) > 6):
        print("")
        return

    # Comparison and end result variables
    gpa = 0
    save = ""

    # Open file
    try: 
        s = open("students.txt", "r")
    except:
        print("students.txt not found, exiting now")
        exit()

    # Parse file for highest GPA in provided grade level   
    for line in s:
        l = list(line.split(","))
        if l[GRADE] == number:
            if float(l[GPA]) > gpa:
                gpa = float(l[GPA])
                save = line

    # Print results
    save = list(save.split(","))
    print("{0},{1},{2},{3},{4},{5}".format(save[LNAME], save[FNAME], save[GPA], save[TLNAME], save[TFNAME].rstrip(), save[BUS]))


def grade_low(number):
    # Only grades 0-6 possible
    if (int(number) > 6):
        print("")
        return

    # Comparison and end result variables
    gpa = 100
    save = ""

    # Open file
    try: 
        s = open("students.txt", "r")
    except:
        print("students.txt not found, exiting now")
        exit()
        
    # Parse file for lowest GPA in provided grade level
    for line in s:
        l = list(line.split(","))
        if l[GRADE] == number:
            if float(l[GPA]) < gpa:
                gpa = float(l[GPA])
                save = line

    # Print results
    save = list(save.split(","))
    print("{0},{1},{2},{3},{4},{5}".format(save[LNAME], save[FNAME], save[GPA], save[TLNAME], save[TFNAME].rstrip(), save[BUS]))


if __name__ == '__main__':
    main()