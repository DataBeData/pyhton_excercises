#Save Filtered Lines
#From feedback.txt, write only the lines that contain 
# the word "positive" into a new file positive_feedback.txt.

with open("feedback.txt") as file,\
open("positive_feedback.txt", "w") as filter_file:
    for line in file:
        if "positive" in line:
            filter_file.write(line)