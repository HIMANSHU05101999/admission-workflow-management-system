# System Design

## Introduction

This document describes the high-level software architecture and design of the **Admission Workflow Management System**.

The design is derived from the project's business requirements and business analysis. It serves as the technical blueprint for implementing the system by defining its major components, their responsibilities, and how they interact throughout the admission workflow.

Version 1 of the project will be implemented as a **Command Line Interface (CLI)** application using **Python**. The system is designed with a modular architecture so that future versions can incorporate a database, REST APIs, web interfaces, authentication, and online payment verification with minimal architectural changes.

---

# System Overview

The Admission Workflow Management System is designed to digitize and organize the on-campus admission process by introducing a structured, token-based workflow.

The system generates a unique token for each student and uses it as the primary reference throughout the admission journey. Instead of manually coordinating students between departments, the system tracks each student's current workflow stage, manages queues, records workflow progress, and ensures fair processing based on the First Come, First Served (FCFS) principle.

Version 1 focuses on demonstrating the complete admission workflow through a CLI application while keeping the architecture flexible for future enhancements.

---

# System Architecture

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

# Core Entities

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

# Class Relationships

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
