from models.student import Student
from models.enums import StudentStatus
class QueueManager:
    def __init__(self,re_entry_gap=5):
        self.__students={}
        self.__next_token=self.token_generator()
        self.__main_queue=[]
        self.__wait_queue=[]
        self.__re_entry_gap=re_entry_gap

    @property
    def student(self):
         return self.__students.copy()

    def add_student(self, student):
        token = self.__next_token
        student.assign_token(token)
        self.__students[token] = student
        self.__main_queue.append(token)
        self.__next_token += 1

    def token_generator(self):
        if self.__students:
            token_no=max(token for token in self.__students) + 1 
            return token_no
        return 1          

    def next_student(self):
        if not self.__main_queue:
             return None

        for token in self.__main_queue:
            if self.__students[token].status == StudentStatus.ACTIVE:
                self.__students[token].status = StudentStatus.IN_PROGRESS
                return self.__students[token]

        
    def __str__(self):
        return f"Total Student: {self.__students} Next Token: {self.__next_token} Main Queue: {self.__main_queue} Wait Queue: {self.__wait_queue} Re Entry Position: {self.__re_entry_gap}"

    def __repr__(self):
            return f"Total Student: {self.__students}  Next Token: {self.__next_token} Main Queue: {self.__main_queue} Wait Queue: {self.__wait_queue} Re Entry Position: {self.__re_entry_gap}"
    
if __name__ == "__main__":
    qm = QueueManager()

    # 1. Create three students
    s1 = Student("APP001")
    s2 = Student("APP002")
    s3 = Student("APP003")

    # 2. Add them to the queue
    qm.add_student(s1)
    qm.add_student(s2)
    qm.add_student(s3)

    print("--- Initial Queue State ---")
    print(f"Main Queue Tokens: {qm}")

    # 3. Call first student
    called_1 = qm.next_student()
    print("\n--- Call 1 ---")
    print(f"Called Token: {called_1.queue_token} (App ID: {called_1._Student__application_id})")
    print(f"Status: {called_1.status.value}")

    # 4. Call second student
    called_2 = qm.next_student()
    print("\n--- Call 2 ---")
    print(f"Called Token: {called_2.queue_token}")
    print(f"Status: {called_2.status.value}")

    # 5. Call third student
    called_3 = qm.next_student()
    print("\n--- Call 3 ---")
    print(f"Called Token: {called_3.queue_token}")
    print(f"Status: {called_3.status.value}")

    # 6. Call when no ACTIVE students remain
    called_4 = qm.next_student()
    print("\n--- Call 4 (All active students in progress) ---")
    print(f"Result: {called_4}")



    
