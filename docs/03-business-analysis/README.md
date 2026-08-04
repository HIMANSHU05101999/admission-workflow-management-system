# Business Analysis

## Introduction

This document analyzes the existing on-campus admission process observed during the university admission experience. Its purpose is to understand the current workflow, identify operational challenges, document business rules, and provide the foundation for designing the Admission Workflow Management System.

The analysis is based on real observations made during the university admission process.

---

# Current Admission Workflow (As-Is Process)

The existing admission process consists of the following stages.

---

# Stage 1 – Student Arrival and Initial Document Submission

## Purpose

To register the student's arrival and collect the required admission documents needed to begin the admission process.

## Primary Actors

* Student
* Admission Officer

## Input

The student reports to the admission desk carrying:

* Admission Application Form
* Class 10 Marksheet
* Class 12 Marksheet
* Graduation Final Semester Marksheet

## Process

The student reports to the admission desk and submits the required admission documents.

The admission staff verifies that the required documents have been submitted and allows the student to proceed to the entrance examination.

At this stage, no physical admission file is created. The application form and attached academic documents continue to move with the student.

## Output

* Student registered for the admission process.
* Required documents accepted.
* Student becomes eligible for the entrance examination.

## Pain Points

* Large numbers of students arrive simultaneously.
* No structured queue management.
* Queue jumping leads to unfair processing.
* Manual coordination causes delays.
* Students are uncertain about the next workflow stage.

---

# Stage 2 – Entrance Examination

## Purpose

To conduct the university's admission entrance examination before document verification.

## Primary Actors

* Student
* Examination Invigilator

## Input

* Admission Application Form
* Class 10 Marksheet
* Class 12 Marksheet
* Graduation Final Semester Marksheet

## Process

Students proceed to the examination hall carrying the application form and supporting academic documents.

Before the examination begins, the invigilator temporarily collects the application form and attached documents.

Students complete the admission examination under the invigilator's supervision.

After the examination, the invigilator returns the application form and supporting documents to the student.

Students then independently locate the document verification room.

## Output

* Admission examination completed.
* Application form and documents returned to the student.
* Student becomes eligible for document verification.

## Pain Points

* Students must determine the location of the next stage themselves.
* No centralized guidance system exists.
* Staff rely on verbal communication.
* Students are often confused about where to go next.

---

# Stage 3 – Document Verification

## Purpose

To verify the student's academic documents before continuing the admission process.

## Primary Actors

* Student
* Verification Officer

## Input

* Admission Application Form
* Class 10 Marksheet
* Class 12 Marksheet
* Graduation Final Semester Marksheet

## Process

Students proceed to the document verification room carrying their application form and supporting documents.

Multiple verification officers perform verification simultaneously.

There is no organized queue or token assignment. Students independently approach whichever verification officer appears available.

The verification officer reviews the documents and completes the required verification on the application form.

After verification, the student proceeds to the physical file creation stage.

## Output

* Academic documents verified.
* Verification completed.
* Student becomes eligible for physical file creation.

## Pain Points

* No structured queue exists.
* Students randomly approach available verification officers.
* Students arriving later may be verified before students who have waited longer.
* No digital tracking of verification status.
* Staff manually coordinate student processing.

---

# Stage 4 – Physical File Creation

## Purpose

To create the student's official physical admission file and prepare the payment form required for fee verification.

## Primary Actors

* Student
* Admission Staff

## Input

* Verified Admission Application Form
* Class 10 Marksheet
* Class 12 Marksheet
* Graduation Final Semester Marksheet
* Required passport-size photographs

## Process

After successful document verification, the student proceeds to the file creation desk.

Admission staff organize the verified application form and supporting academic documents into an official physical admission file.

During this stage, the student submits the required passport-size photographs and signs the necessary admission documents as instructed by the admission staff.

The completed physical admission file becomes the university's official admission record and remains with the university.

A payment form is prepared and handed to the student.

The student is instructed to proceed to the accountant with the payment form.

## Output

* Official physical admission file created.
* Required admission documents signed.
* Passport-size photographs collected.
* Payment form issued to the student.
* Student becomes eligible for payment verification.

## Pain Points

* Physical file preparation is completely manual.
* Students have no visibility into file preparation progress.
* Workflow progress cannot be tracked digitally.
* Students rely on verbal instructions to locate the payment counter.

---

# Stage 5 – Payment Verification and Fee Processing

## Purpose

To manually verify the student's fee payment and complete the admission process while handling exceptional cases when required.

## Primary Actors

* Student
* Accountant

## Input

* Payment Form
* Payment details or transaction reference

## Process

The student submits the payment form to the accountant.

The accountant instructs the student to complete the required payment if it has not already been made.

After payment, the accountant manually verifies the payment details.

If the student has obtained special permission, such as an installment plan, fee concession, or another administrative exception, the accountant requests the student to obtain the required approval signatures on the payment form before continuing.

The student returns to the accountant after obtaining the required approvals.

Once all payment requirements have been satisfied, the accountant manually verifies the payment and completes the admission process.

## Output

* Payment manually verified.
* Admission process completed.

## Pain Points

* Payment verification is completely manual.
* Transaction details are manually checked.
* Exception cases interrupt the normal workflow.
* Students must leave the payment counter to obtain approval signatures and later return.
* Returning students have no structured method of re-entering the queue.
* Queue jumping may occur.
* Staff manually decide the order in which students are processed.

---

# Stakeholders

| Stakeholder             | Responsibility                                                       |
| ----------------------- | -------------------------------------------------------------------- |
| Student                 | Completes the admission workflow by visiting each stage.             |
| Admission Officer       | Registers students and collects the initial admission documents.     |
| Examination Invigilator | Conducts the entrance examination and manages examination documents. |
| Verification Officer    | Verifies academic documents.                                         |
| Admission Staff         | Creates the physical admission file and prepares the payment form.   |
| Accountant              | Verifies payments and completes the admission process.               |

---

# Business Rules Observed

* Students must report with the required admission documents.
* The entrance examination must be completed before document verification.
* Document verification must be completed before physical file creation.
* The physical admission file is created and retained by the university.
* The student receives only the payment form after file creation.
* Payment verification is performed manually by the accountant.
* Certain students may require additional approval signatures before payment verification can be completed.
* Admission is completed only after successful manual payment verification.

---

# Exception Scenarios

* Installment payment approval required.
* Fee concession approval required.
* Payment failure.
* Multiple payment transactions.
* Student temporarily unavailable.
* Queue jumping.
* Manual priority processing by staff.

---

# Proposed Workflow (To-Be Process)

*To be documented.*

---

# Process Improvements

*To be documented.*
