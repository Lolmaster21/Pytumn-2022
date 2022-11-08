class Student:
    def __init__(self, name, ID, hobby, next=None):
        self.name = name
        self.ID = ID
        self.hobby = hobby
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, name,hobby, ID):
        newStudent = Student(name,hobby, ID)
        if self.head:
            current = self.head
            
            while current.next:
                current = current.next
            current.next = newStudent
        else:
            self.head = newStudent
            
    def printList(self):
        current = self.head
        while current:
            print("Student name:", current.name,", Hobby:", current.hobby, ", ID:", current.ID)
            current = current.next
            
    def getNumber(self):
        print("What name do I look for?")
        student = input()
        lol = 0
        current = self.head
        while current:
            if student == current.name:
                return True
            else:
                lol += 1
                current = current.next
                
    def numStudents(self):
         lamo = 0
         current = self.head
         while current:
            lamo += 1
            current = current.next
         print("There are:", lamo,"students")
         
#     def bounty(self, x):
#         current = self.head
#         while current:
#             if x == 3:
#                 print("The student on bounty is: ")
#                 


       #create vairable, initialize to 0
        #walk through the linked list
        #add one to variable each time
        
        

StudentLine = LinkedList()

StudentLine.insert("timothy", 32147,  "breathing")
StudentLine.insert("new name", 51606, "being original")
StudentLine.insert("Tamatha", 343,"photosynthesis")
StudentLine.insert("Nicky", 5486, "anime")
StudentLine.insert("Lala",7, "Stupid memes")
StudentLine.insert("Alexa",50265, "Coding")


StudentLine.printList()
StudentLine.numStudents()
print(StudentLine.getNumber())
# StudentLine.bounty(3)

