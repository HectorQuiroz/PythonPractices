contacts={"number":"4","students":
[
    {"name":"Hector Quiroz","email":"hector.quiroz@crato-it.com"},
    {"name":"Harry Potter","email":"harrypotter@howgarts.com"},
    {"name":"Hermione Granger","email":"hgranger@howgarts.com"},
    {"name":"Ron Weasley","email":"rweasley@howgarts.com"}
]
}

for student in contacts["students"]:
    print(student["email"])
