from ..models.student import Student
class QueueManager:
    def __init__(self,re_entry_gap=5):
        self.__student={}
        self.__token_to_assign=self.token_generator()
        self.__main_queue=[]
        self.__wait_queue=[]
        self.__re_entry_gap=re_entry_gap

    def add_student(self, student: "Student"):
        self.__student[self.__token_to_assign]=student
        self.__main_queue.append(self.__token_to_assign)

    def token_generator(self, student: "Student"):
        if self.__student:
            student.queue_token=max(token for token in self.__student) + 1
        else: 
            student.queue_token=1            

if __name__=="__main__":
    queuemanager=QueueManager()
    print(queuemanager)




    
