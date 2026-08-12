from enum import Enum

class WorkflowStage(Enum):
    REGISTRATION = "Registration"
    EXAM = "Exam"
    VERIFICATION = "Verification"
    FILE_CREATION = "File Creation"
    PAYMENT = "Payment"
    COMPLETED = "Completed"

class QueueType(Enum):
    MAIN = "Main"
    WAITING = "Waiting"

class StudentStatus(Enum):
    ACTIVE = "Active"
    WAITING = "Waiting"
    COMPLETED = "Completed"
    
class PaymentStatus(Enum):
    PENDING = "Pending"
    APPROVAL_REQUIRED = "Approval Required"
    VERIFIED = "Verified"