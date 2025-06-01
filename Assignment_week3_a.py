
student = {
          "Abdulmuizz" : {
              "Level" : 100,
              "Dept" :  "Computer science"
              },
          "Abdulkareem" : {
              "Level" : 200,
              "Dept" : "Medical lab science"
              },
          "Kamaldeen" : {
              "Level" : 300,
              "Dept" : "PHS"
              },
          "Isiaq" : {
              "Level" : 400,
              "Dept" : "Biochemistry"
              }
          }
for Name,info in student.items():
      print("""\nName : {Name}
  Level : {info["Level"]}
  Department : {info["Dept"]}
           """)



