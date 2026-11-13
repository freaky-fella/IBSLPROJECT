# Criterion A: Problem Specification

## 1. Problem Scenario
* **What evidence belongs here?**
  * Identification of the specific client/end-user (e.g., High School Peer Tutoring Coordinator / NHS Advisor) and target user groups (Tutors, Tutees).
  * Concrete description of the current manual workflow (spreadsheets, paper logs) and its operational bottlenecks (scheduling conflicts, time spent matching, lost volunteer hours).
  * Evidence of client consultation (e.g., interview notes, email transcript, or survey summary confirming the problem exists).
* **What do I still need to decide?**
  * Which exact real-world coordinator will act as my official client for consultation and feedback?
  * What specific documentation or screenshots of the current spreadsheet/sign-in process can I include as baseline evidence?

## 2. Solution Requirements
* **What evidence belongs here?**
  * **Functional Requirements:** Specific actions the system must perform (e.g., intake of tutor/tutee profiles, automated schedule overlap matching, session logging, CSV/PDF report exports).
  * **Non-Functional Requirements:** Usability, data persistence, input validation, and performance expectations.
  * Explicit boundaries defining what is *in scope* vs. *out of scope* for a single-student build.
* **What do I still need to decide?**
  * Will tutors and tutees interact with the system directly, or will only the coordinator operate the interface?
  * What exact data fields are mandatory on official school volunteer hour reports?

## 3. Success Criteria
* **What evidence belongs here?**
  * 4–6 specific, measurable, and testable criteria (`SC-1` to `SC-6`) directly tied to the client's problem.
  * Quantitative benchmarks (e.g., match generation under 5 seconds, 100% blocking of overlapping period conflicts, 0% discrepancy in volunteer hour totals).
* **What do I still need to decide?**
  * Are all my success criteria objective enough that I can design pass/fail test cases for them in Criterion C and evaluate them with evidence in Criterion E?

## 4. Computational Context
* **What evidence belongs here?**
  * Justification for why a computational solution (relational database + OOP architecture + matching algorithm) is superior to the existing manual/spreadsheet approach.
  * Chosen technology stack (e.g., Python, SQLite/PostgreSQL, UI framework) and rationale aligned with the problem constraints.
* **What do I still need to decide?**
  * Will this run as a local desktop application or a lightweight web application?
  * How will the database be hosted or stored locally so the client can easily run it?
