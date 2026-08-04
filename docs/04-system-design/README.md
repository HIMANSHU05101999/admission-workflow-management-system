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
