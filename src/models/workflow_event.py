from datetime import datetime
from .enums import WorkflowStage

class WorkflowEvent:
    def __init__(self, stage, action, processed_by, reason=None):
        if isinstance(stage,WorkflowStage):
            self.__stage=stage
        else:
            raise TypeError ("Stage does not belong to WorkflowSatge")

        self.__action=action
        self.__timestamp=datetime.now()
        self.__processed_by=processed_by
        self.__reason=reason

    @property
    def timestamp(self):
        return self.__timestamp


    def __str__(self):
        return f"| Stage: {self.__stage.value} |\n| Action: {self.__action} |\n| Date/Time: {self.__timestamp} |\n| Processed By: {self.__processed_by} |\n| Reason: {self.__reason} |"

    def __repr__(self):
        return f"| Stage: {self.__stage.value} |\n| Action: {self.__action} |\n| Date/Time: {self.__timestamp} |\n| Processed By: {self.__processed_by} |\n| Reason: {self.__reason} |"

if __name__=="__main__":
    work=WorkflowEvent(WorkflowStage.REGISTRATION,"ABC","ABC")
    print(work)