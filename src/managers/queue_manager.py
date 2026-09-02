from ..models.student import Student
class QueueManager:
    def __init__(self,re_entry_gap=5):
        self.__student={}
        self.__next_token=self.token_generator()
        self.__main_queue=[]
        self.__wait_queue=[]
        self.__re_entry_gap=re_entry_gap

    @property
    def student(self):
         return self.__student.copy()

    def add_student(self, student):
        token = self.__next_token
        student.assign_token(token)
        self.__student[token] = student
        self.__main_queue.append(token)
        self.__next_token += 1

    def token_generator(self):
        if self.__student:
            token_no=max(token for token in self.__student) + 1 
            return token_no
        return 1          

    def next_student(self):
        if not self.__main_queue:
             return None
        
        student_token=self.__main_queue[0]

        if student_token in self.__student:
            return self.__student[student_token]

    
    def __str__(self):
        return f"Total Student: {self.__student} Next Token: {self.__next_token} Main Queue: {self.__main_queue} Wait Queue: {self.__wait_queue} Re Entry Position: {self.__re_entry_gap}"

    def __repr__(self):
            return f"Total Student: {self.__student}  Next Token: {self.__next_token} Main Queue: {self.__main_queue} Wait Queue: {self.__wait_queue} Re Entry Position: {self.__re_entry_gap}"
    
if __name__=="__main__":
    s1=Student("A01")
    s2=Student("A02")
    queuemanager=QueueManager()
    #s1.queue_token=queuemanager.token_generator()
    #s2.queue_token=queuemanager.token_generator()
    queuemanager.add_student(s1)
    queuemanager.add_student(s2)
    print(queuemanager)
    #print(queuemanager.token_generator())
    #print(queuemanager.token_generator())


    
