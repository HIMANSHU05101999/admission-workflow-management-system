# System Design

## Introduction

This document describes the high-level software architecture and design of the **Admission Workflow Management System**.

The design is derived from the project's business requirements and business analysis. It serves as the technical blueprint for implementing the system by defining its major components, their responsibilities, and how they interact throughout the admission workflow.

Version 1 of the project will be implemented as a **Command Line Interface (CLI)** application using **Python**. The system is designed with a modular architecture so that future versions can incorporate a database, REST APIs, web interfaces, authentication, and online payment verification with minimal architectural changes.

---

# 01. System Overview

The Admission Workflow Management System is designed to digitize and organize the on-campus admission process by introducing a structured, token-based workflow.

The system generates a unique token for each student and uses it as the primary reference throughout the admission journey. Instead of manually coordinating students between departments, the system tracks each student's current workflow stage, manages queues, records workflow progress, and ensures fair processing based on the First Come, First Served (FCFS) principle.

Version 1 focuses on demonstrating the complete admission workflow through a CLI application while keeping the architecture flexible for future enhancements.

---

# 02. System Architecture

The system follows a modular architecture where each component is responsible for a specific part of the admission workflow. This separation of responsibilities improves maintainability, scalability, and future extensibility.

## High-Level Architecture


                     User (Staff)
                          │
                          ▼
                   CLI Application
                          │
        ┌─────────────────┼─────────────────┐
        ▼                 ▼                 ▼
 Admission         Workflow Manager    Queue Manager
 Management
        │                 │                 │
        └─────────────────┼─────────────────┘
                          │
                          ▼
                   Student Records
                          │
                          ▼
                  Storage Manager
                          │
                          ▼
                     JSON Storage


### Component Responsibilities

#### Admission Management

Responsible for initiating and completing the admission process.

**Responsibilities:**

* Register arriving students.
* Generate unique admission tokens.
* Initialize the admission workflow.
* Complete the admission process.

---

#### Workflow Manager

Responsible for controlling the student's progression through the admission workflow.

**Responsibilities:**

* Track the current workflow stage.
* Determine the next workflow stage.
* Update workflow progress.
* Record workflow history.

---

#### Queue Manager

Responsible for ensuring fair and organized student processing.

**Responsibilities:**

* Maintain FCFS queues.
* Manage waiting queues for exception cases.
* Recall waiting tokens.
* Support manual queue overrides by authorized staff.

---

#### Student Records

Responsible for maintaining admission-related information for each student.

**Responsibilities:**

* Store student information.
* Store admission token details.
* Track workflow status.
* Maintain payment verification status.
* Record admission completion.

# 03. Core Entities

The following entities were identified during the business analysis. They represent the primary objects involved in the admission workflow and form the foundation of the system design.

| Entity               | Description                                                                                                |
| -------------------- | ---------------------------------------------------------------------------------------------------------- |
| Student              | Represents a student participating in the admission process.                                               |
| Token                | Represents the unique admission token assigned to each student for workflow tracking and queue management. |
| Workflow Stage       | Represents the current stage of a student's admission journey.                                             |
| Admission Workflow   | Represents the complete sequence of workflow stages from student arrival to admission completion.          |
| Queue                | Represents the First Come, First Served (FCFS) queue for a workflow stage.                                 |
| Waiting Queue        | Represents the queue for students whose processing is temporarily paused due to exceptional circumstances. |
| Staff Member         | Represents authorized university staff interacting with the system during the admission process.           |
| Payment Verification | Represents the manual verification of a student's payment before admission completion.                     |

## Design Principle

The system follows a modular design in which each entity has a clearly defined responsibility. During implementation, these entities will be evaluated to determine whether they should be represented as Python classes, enumerations, or supporting data structures.

The objective is to model the admission process accurately while keeping the design simple, maintainable, and extensible for future versions of the system.

# 04. Class Relationships

This section describes how the core classes interact with one another. Each relationship is designed to maintain a clear separation of responsibilities while keeping the system modular and easy to extend.

---

## AdmissionSystem

The `AdmissionSystem` class acts as the central coordinator of the application. It initializes the system, coordinates interactions between components, and controls the overall execution of the admission workflow.

### Relationships

* Coordinates the `WorkflowManager`.
* Coordinates the `QueueManager`.
* Coordinates the `StorageManager`.

---

## WorkflowManager

The `WorkflowManager` controls the progression of students through the admission workflow.

### Relationships

* Updates a student's current workflow stage.
* Uses the `QueueManager` to move students into the appropriate queue for the next stage.
* Notifies the `StorageManager` (through the `AdmissionSystem`) whenever workflow data needs to be persisted.

---

## QueueManager

The `QueueManager` is responsible for maintaining the admission queues.

### Relationships

* Manages the Main Queue (FCFS).
* Manages the Waiting Queue for exception cases.
* Stores and updates student queue positions.
* Returns the next eligible student for processing.
* Supports manual queue overrides by authorized staff.

The `QueueManager` does **not** determine the student's next workflow stage. It only manages queue operations.

---

## Student

The `Student` class represents an individual participating in the admission process.

### Relationships

* Stores the student's admission token.
* Stores the current workflow stage.
* Stores the payment verification status.
* Is updated by the `WorkflowManager`.
* Is managed by the `QueueManager`.

---

## StorageManager

The `StorageManager` provides persistent storage for the application.

### Relationships

* Loads student records from storage.
* Saves student records.
* Saves queue data.
* Saves workflow progress.
* Operates independently of the business logic, allowing JSON storage to be replaced by a database in future versions without requiring changes to the system's core components.

---

# Relationship Summary

| Source          | Relationship | Target          |
| --------------- | ------------ | --------------- |
| AdmissionSystem | Coordinates  | WorkflowManager |
| AdmissionSystem | Coordinates  | QueueManager    |
| AdmissionSystem | Coordinates  | StorageManager  |
| WorkflowManager | Updates      | Student         |
| WorkflowManager | Uses         | QueueManager    |
| QueueManager    | Manages      | Student         |
| StorageManager  | Loads/Saves  | Student Records |
| StorageManager  | Loads/Saves  | Queue Data      |
| StorageManager  | Loads/Saves  | Workflow Data   |


# 05. Workflow Sequence

This section describes how the major system components interact throughout the admission process. It provides a high-level view of the execution flow without describing implementation details.

---

# Workflow 1 – Student Registration

## Objective

Register a new student and initialize the admission workflow.

### Sequence

```text
Staff starts the CLI Application
        │
        ▼
Student arrives at the admission desk
        │
        ▼
AdmissionSystem registers the student
        │
        ▼
QueueManager generates a unique admission token
        │
        ▼
Student record is created
        │
        ▼
WorkflowManager sets the initial workflow stage
        │
        ▼
QueueManager places the student in the Main (FCFS) Queue
        │
        ▼
StorageManager saves the updated system data
```

### Outcome

* Student successfully registered.
* Admission token generated.
* Student added to the active admission workflow.

---

# Workflow 2 – Stage Processing

## Objective

Move a student through the admission workflow in the correct sequence.

### Sequence

```text
QueueManager calls the next eligible student
        │
        ▼
Student reports to the current admission stage
        │
        ▼
Staff completes the stage
        │
        ▼
WorkflowManager updates the student's workflow stage
        │
        ▼
QueueManager places the student in the queue for the next stage
        │
        ▼
StorageManager saves the updated workflow state
```

### Outcome

* Student progresses to the next admission stage.
* Workflow status remains synchronized.
* Queue order is preserved.

---

# Workflow 3 – Exception Handling

## Objective

Handle situations where a student cannot proceed through the normal workflow.

### Sequence

```text
Student cannot continue
        │
        ▼
WorkflowManager identifies an exception
        │
        ▼
QueueManager moves the student to the Waiting Queue
        │
        ▼
Main Queue continues processing
        │
        ▼
After a configurable number of students,
the Waiting Queue is checked
        │
        ▼
Eligible student is recalled
        │
        ▼
Student resumes the admission workflow
        │
        ▼
StorageManager saves the updated workflow state
```

### Possible Exception Cases

* Installment payment approval
* Fee concession approval
* Payment verification pending
* Temporary absence of the student
* Administrative hold

### Outcome

* Main workflow remains uninterrupted.
* Exception cases are handled fairly.
* Students can rejoin the workflow without losing their admission progress.

---

# Workflow 4 – Manual Queue Override

## Objective

Allow authorized staff to prioritize a student when necessary.

### Sequence

```text
Authorized staff enters a token number
        │
        ▼
QueueManager locates the student
        │
        ▼
WorkflowManager validates the request
        │
        ▼
Student is processed immediately
        │
        ▼
Workflow continues normally
        │
        ▼
StorageManager records the updated workflow state
```

### Outcome

* Special cases can be handled without disrupting the overall workflow.
* Manual intervention remains controlled and traceable.

---

# Workflow 5 – Admission Completion

## Objective

Complete the admission process and archive the student's admission record.

### Sequence

```text
Payment verification completed
        │
        ▼
WorkflowManager marks the admission as completed
        │
        ▼
QueueManager removes the student from the active workflow
        │
        ▼
StorageManager archives the completed admission record
        │
        ▼
Completed admission becomes available for reporting and analytics
```

### Outcome

* Admission process completed successfully.
* Student removed from active processing.
* Admission record preserved for future reference, reporting, and statistical analysis.

---

# Workflow Summary

The Admission Workflow Management System ensures that every student follows a structured and transparent admission journey.

The workflow is designed to:

* Maintain First Come, First Served (FCFS) processing.
* Support controlled exception handling.
* Allow authorized manual intervention when required.
* Preserve completed admission records for reporting and future analysis.
* Keep business logic independent of the underlying storage mechanism, allowing future migration from JSON storage to a relational database without major architectural changes.

# 06. Exception Handling

## Introduction

During the admission process, not every student follows the standard workflow. Some students may require additional approvals, experience payment-related issues, or become temporarily unavailable. The system is designed to handle these situations without interrupting the normal admission process.

Instead of blocking the workflow, affected students are temporarily moved to a Waiting Queue. The Main Queue continues processing other students while the system periodically recalls students from the Waiting Queue.

---

# Exception Handling Strategy

The system follows the principles below:

* The Main Queue should never stop because of an individual student.
* Students facing temporary issues are moved to the Waiting Queue.
* Waiting Queue students are automatically recalled after a configurable number of students have been processed.
* Authorized staff can manually prioritize a student when necessary.
* Every exception is recorded for future reporting and analysis.

---

# Supported Exception Scenarios

## Installment Approval

A student requests permission to pay fees in installments.

**System Action**

* Move the student to the Waiting Queue.
* Allow other students to continue.
* Recall the student after the required approval has been obtained.

---

## Fee Concession Approval

A student has received permission for a scholarship or fee concession.

**System Action**

* Move the student to the Waiting Queue.
* Resume processing after approval is completed.

---

## Payment Verification Pending

The student's payment cannot be verified immediately.

**System Action**

* Temporarily move the student to the Waiting Queue.
* Resume processing once payment verification is completed.

---

## Student Temporarily Unavailable

The student's token is called, but the student is not present.

**System Action**

* Skip the current turn.
* Move the student to the Waiting Queue.
* Recall the student after a configurable number of admissions.

---

## Manual Priority Processing

An authorized staff member decides to process a specific student immediately.

**System Action**

* Locate the student's token.
* Temporarily prioritize the student.
* Continue normal queue processing afterward.

---

# Waiting Queue Strategy

The Waiting Queue ensures fairness while preventing workflow interruptions.

The system periodically checks the Waiting Queue after processing a configurable number of students from the Main Queue.

If an eligible student is available, the student is recalled and allowed to continue from the stage where processing was paused.

---

# Design Goals

The exception handling mechanism is designed to:

* Maintain uninterrupted workflow.
* Preserve fairness.
* Minimize waiting time.
* Support administrative flexibility.
* Record operational insights for future analysis.

# 07. Future Architecture

## Introduction

Version 1 of the Admission Workflow Management System focuses on demonstrating the complete admission workflow using a Python-based Command Line Interface (CLI).

The system has been designed using a modular architecture so that future versions can introduce new technologies without requiring significant changes to the core business logic.

---

# Planned Evolution

## Version 1

### Technology

* Python
* Command Line Interface (CLI)
* JSON-based storage

### Features

* Student registration
* Token generation
* FCFS queue management
* Waiting Queue
* Workflow management
* Manual payment verification
* Admission record archiving

---

## Version 2

### Planned Improvements

* SQLite or PostgreSQL database
* Authentication and authorization
* Improved reporting
* Better data persistence
* Administrative dashboards

---

## Version 3

### Planned Improvements

* REST API
* Web application
* Multi-user support
* Role-based access control
* Real-time workflow tracking

---

## Version 4

### Planned Improvements

* Online payment verification integration (optional)
* Notification system
* Analytics dashboard
* Performance reports
* Admission statistics
* Workflow optimization reports

---

# Scalability

The modular design allows individual components to evolve independently.

For example:

* JSON storage can be replaced by a relational database.
* The CLI interface can be replaced by a web application.
* Manual payment verification can be extended to support payment gateway verification if permitted by the institution.
* Additional workflow stages can be introduced without redesigning the core architecture.

---

# Long-Term Vision

The long-term objective is to develop a production-ready admission workflow platform that provides:

* Fair and transparent queue management.
* Efficient workflow coordination.
* Comprehensive admission analytics.
* Scalable architecture.
* Easy integration with future technologies.
