students=("rishabh - meerut"
"imtiyaz - delhi"
"nilima - cochin"
"rati - shimla"
"ayishah - delhi"
"raghu - shimla"
"naseer - kanpur"
"karthikeyan - delhi"
"salma - jaipur"
"pankaj - delhi"
"brijesh - delhi"
"govind - delhi"
"puneet - shimla"
"siddhi - delhi"
"suman - jaipur"
"rajeev - shimla"
"mohinder - delhi"
"rajendra - jaipur"
"priyanka - shimla"
"neela - delh")
file = open("names_students.html", "w")
for names in students:
    (file.write(names))