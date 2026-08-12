from enum import Enum

class WorkflowStage(Enum):
    REGISTRATION="Registration"
    EXAM="Exam"
    VERIFICATION="Verification"
    FILE_CREATION="File Creation"
    PAYMENT="Payment"
    COMPLETED="Completed"

print(WorkflowStage.EXAM == "Exam")