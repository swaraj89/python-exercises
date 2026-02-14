registered_students = {'Lina', 'Omar', 'Ramesh', 'Suresh', 'Rama', 'Hari'}
attended_students = {'Ramesh', 'Suresh', 'Rama', 'Hari'}

print(f"Absent students: {registered_students - attended_students}")
print(f"Absent students: {registered_students.difference(attended_students)}")