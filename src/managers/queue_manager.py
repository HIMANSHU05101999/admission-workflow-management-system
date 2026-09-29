from models.student import Student
from models.enums import StudentStatus, WorkflowStage
from models.workflow_event import WorkflowEvent
class QueueManager:

    STAGE_TRANSITION={WorkflowStage.REGISTRATION : WorkflowStage.EXAM,
                      WorkflowStage.EXAM : WorkflowStage.VERIFICATION,
                      WorkflowStage.VERIFICATION : WorkflowStage.FILE_CREATION,
                      WorkflowStage.FILE_CREATION : WorkflowStage.COMPLETED,
                      WorkflowStage.COMPLETED : WorkflowStage.COMPLETED}

    def __init__(self,re_entry_gap=5):
        self.__students={}
        self.__next_token=self.token_generator()
        self.__main_queue=[]
        self.__wait_queue=[]
        self.__re_entry_gap=re_entry_gap

    @property
    def student(self):
         return self.__students.copy()

    def add_student(self, student, processed_by = "System"):
        token = self.__next_token
        student.assign_token(token)
        self.__students[token] = student
        self.__main_queue.append(token)
        self.__next_token += 1

        work_flow_update=WorkflowEvent(self.__students[token].current_stage, "Student Added", processed_by)
        self.__students[token].add_event(work_flow_update)


    def token_generator(self):
        if self.__students:
            token_no=max(token for token in self.__students) + 1 
            return token_no
        return 1          

    def next_student(self, processed_by="System"):
        if not self.__main_queue:
             return None

        for token in self.__main_queue:
            if self.__students[token].status == StudentStatus.ACTIVE:
                self.__students[token].status = StudentStatus.IN_PROGRESS
                work_flow_update=WorkflowEvent(self.__students[token].current_stage, "Next Student Called", processed_by)
                self.__students[token].add_event(work_flow_update)
                return self.__students[token]

        

    def complete_stage(self, token, processed_by="System"):
        if token not in self.__students:
            return None
        if self.__students[token].status == StudentStatus.ACTIVE or self.__students[token].status == StudentStatus.COMPLETED:
            raise ValueError("Studen in Active or Completed state")
        #print(self.student)
        if self.__students[token].current_stage in QueueManager.STAGE_TRANSITION:
            self.__students[token].current_stage = QueueManager.STAGE_TRANSITION[self.__students[token].current_stage]
            if self.__students[token].current_stage == WorkflowStage.COMPLETED:
                self.__students[token].status = StudentStatus.COMPLETED
            else:    
                self.__students[token].status = StudentStatus.ACTIVE
        work_flow_update=WorkflowEvent(self.__students[token].current_stage, "Advanced to Next Stage", processed_by)
        self.__students[token].add_event(work_flow_update)

        #print(self.student)
    
    def hold_student(self, token, processed_by="System"):
        if token not in self.__students:
            return None

        if token not in self.__wait_queue:
            self.__wait_queue.append(token)

        if token in self.__main_queue:
            self.__main_queue.remove(token)

        self.__students[token].status = StudentStatus.WAITING

        work_flow_update=WorkflowEvent(self.__students[token].current_stage, "Moved to Waiting Queue", processed_by)
        self.__students[token].add_event(work_flow_update)

    def resume_student(self, token, processed_by="System"):
        if (token not in self.__students or token not in self.__wait_queue) :
            return None
    
        self.__main_queue.insert(self.__re_entry_gap,token)
        self.__wait_queue.remove(token)

        self.__students[token].status = StudentStatus.ACTIVE

        work_flow_update=WorkflowEvent(self.__students[token].current_stage, "Moved to Main Queue", processed_by)
        self.__students[token].add_event(work_flow_update)

                    



                
        

        
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
    qm.add_student(s1, "John")
    #qm.add_student(s2)
    #qm.add_student(s3)

    ##print("--- Initial Queue State ---")
    #print(f"Main Queue Tokens: {qm}")

    # 3. Call first student
    called_1 = qm.next_student()
    #print("\n--- Call 1 ---")
    #print(f"Called Token: {called_1.queue_token} (App ID: {called_1._Student__application_id})")
    #print(f"Status: {called_1.status.value}")

    # 4. Call second student
    #called_2 = qm.next_student()
    #print("\n--- Call 2 ---")
    #print(f"Called Token: {called_2.queue_token}")
    #print(f"Status: {called_2.status.value}")

    # 5. Call third student
    #called_3 = qm.next_student()
    #print("\n--- Call 3 ---")
    #print(f"Called Token: {called_3.queue_token}")
    #print(f"Status: {called_3.status.value}")

    # 6. Call when no ACTIVE students remain
    #called_4 = qm.next_student()
    #print("\n--- Call 4 (All active students in progress) ---")
    #print(f"Result: {called_4}")

    test_token = called_1.queue_token
    print(test_token)

    print()
    print("---Debuging---")
    print()
    qm.complete_stage(test_token,"John")


    
