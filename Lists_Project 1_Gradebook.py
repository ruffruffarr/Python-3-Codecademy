#1 make a list of grades from last semester
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

#2 make three lists that separates subjects, grades, and gradebook 
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

#3 append (add) two new items to gradebook by using .append()
gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])

#5 change the visual arts grade from 93 to 98 (access the last item in the list > then the last item in that sublist
gradebook[-1][-1] = 98
print(gradebook)

# .remove() poetry's grade and .append() pass
gradebook[2].remove(85)
gradebook[2].append("Pass")
print(gradebook)

# create a variable that adds last semester's and this semester's gradebooks and print it in the terminal
full_gradebook = last_semester_gradebook + gradebook 
print(full_gradebook)
