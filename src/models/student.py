from .enums import WorkflowStage,QueueType,StudentStatus,PaymentStatus
from .workflow_event import WorkflowEvent

class Student:
    def __init__(self, application_id):
        self.__application_id=application_id
        self.__queue_token=None
        self.__current_stage=WorkflowStage.REGISTRATION
        self.__status=StudentStatus.ACTIVE
        self.__queue_type=QueueType.MAIN
        self.__payment_status=PaymentStatus.PENDING
        self.__history=[]

    @property
    def queue_token(self):
        return self.__queue_token

    @queue_token.setter
    def queue_token(self,val):
        self.__queue_token=val
    
    @property
    def history(self):
        return self.__history.copy()

    def assign_token(self, token):
        self.__queue_token=token

    def add_event(self,event):
        if isinstance(event,WorkflowEvent):
            self.__history.append(event)
        else:
            raise TypeError ("Event does not belong to workflow event")
    
    def __str__(self):
        return f"| Application ID: {self.__application_id} |\n| Token: {self.__queue_token} |\n| Current Stage: {self.__current_stage.value} |\n| Status: {self.__status.value} |\n| Queue Type: {self.__queue_type.value} |\n| Payment Status: {self.__payment_status.value} |\n| History: {self.__history} |"

    def __repr__(self):
        return f"| Application ID: {self.__application_id} |\n| Token: {self.__queue_token} |\n| Current Stage: {self.__current_stage.value} |\n| Status: {self.__status.value} |\n| Queue Type: {self.__queue_type.value} |\n| Payment Status: {self.__payment_status.value} |\n| History: {self.__history} |"
        
if __name__=="__main__":
    we=WorkflowEvent(WorkflowStage.REGISTRATION,"ABC","ABC")
    s1=Student("AAP1")
    s1.add_event(we)
    print(s1.history)
    s1.history.clear()
    print(s1.history)
    s2=Student("AAP2")

    #print(s1)
    #print(s2)
