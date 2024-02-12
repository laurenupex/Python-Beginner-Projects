# weighted exam score average

# entering number of exams using user input
number_of_exams = int(input("Enter number of exams: "))
print(number_of_exams)

# entering number of credits covered
total_credits = int(input("Enter how many credits these exams cover: "))

# begin with average of 0 and add up percentages from each exam
average = 0

for exam in range(number_of_exams):
    score = int(input("Enter exam score: "))
    exam_credits = int(input("Enter how many credits this exam covered: "))
    average = average + score*exam_credits/total_credits
print("Your average is ", average)
