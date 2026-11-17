# Criterion A: Problem Specification (First Draft)

## 1. Problem Scenario

### Client and Target Users
* **Primary Client:** High School Peer Tutoring Coordinator (Faculty Advisor / National Honor Society Coordinator).
* **Secondary End-Users:**
  * **Peer Tutors:** Student volunteers offering academic support in verified subjects during free periods.
  * **Tutees:** Students requesting academic assistance in specific courses during matching free periods.

### Current Workflow and Operational Bottlenecks
Currently, the peer tutoring program relies on static spreadsheets (Google Sheets / Excel) and physical paper sign-in logs to manage intake, scheduling, and volunteer hour tracking. At the beginning of each term—and whenever student timetables shift—the coordinator manually cross-references tutee intake responses against tutor rosters. 

Consultation with the coordinator highlighted four recurring operational failures in this manual workflow *(see Appendix A for client interview notes)*:
1. **Time-Intensive Matching:** Manually comparing a tutee's requested subject and weekly free periods against dozens of tutor schedules requires several hours of administrative work each week.
2. **Schedule and Qualification Conflicts:** Visual scanning of spreadsheet grids frequently results in human errors, including double-booking a tutor during the same period, pairing students with zero overlapping free periods, or assigning tutors to subjects they are not qualified to teach.
3. **Unreliable Volunteer Hour Verification:** Paper attendance sheets are periodically misplaced or miscalculated, creating discrepancies when verifying service hours for honor society credit or graduation requirements.
4. **Rigid Reassignment Process:** When a tutor drops out or a student's class schedule changes mid-semester, identifying affected pairings and finding valid replacements requires re-checking records manually.

---

## 2. Solution Requirements

### Functional Requirements
* **FR-1 (User & Profile Management):** The system must allow the coordinator to create, view, update, and deactivate profiles for `Users`, `Tutors` (including maximum weekly hours and active status), and `Tutees` (including grade level).
* **FR-2 (Subject & Proficiency Mapping):** The system must store a catalog of academic `Subjects` and associate tutors with specific subjects and proficiency levels via a normalized relationship.
* **FR-3 (Availability Matrix Storage):** The system must record structured weekly availability (`day_of_week` and `period_number`) for both tutors and tutees.
* **FR-4 (Automated Matching Engine):** Given a tutee's subject request, the system must automatically filter qualified, active tutors, compute schedule overlaps, check weekly hour limits, and output a ranked list of compatible matches.
* **FR-5 (Conflict Prevention & Manual Override):** The system must prevent saving invalid matches where no shared availability exists or where a tutor exceeds capacity, while permitting the coordinator to review and confirm final assignments.
* **FR-6 (Session Logging & Reporting):** The system must log individual tutoring sessions (`date`, `duration_minutes`, `status`, `notes`), automatically aggregate cumulative verified volunteer hours per tutor, and export filtered summary reports as CSV files.

### Non-Functional Requirements
* **NFR-1 (Data Persistence & Integrity):** All records must be stored in a relational database (`SQLite`) enforcing primary and foreign key constraints so data persists reliably across sessions without duplication.
* **NFR-2 (Responsiveness):** Generating candidate matches for a tutee request must execute in under 5 seconds for a dataset of up to 100 active students.
* **NFR-3 (Input Validation):** All user inputs (emails, grade levels, period numbers, session durations) must be validated before database insertion to prevent runtime crashes or corrupt records.

### Scope Boundaries
* **In Scope:** Single-administrator desktop/local web interface operated by the Peer Tutoring Coordinator; relational database storage; automated matching and conflict checking; session hour tracking; CSV report generation.
* **Out of Scope:** Direct integration with the school district's proprietary Student Information System (SIS) or automated mass-emailing via external SMTP servers (identified as potential future enhancements in Criterion E).

---

## 3. Success Criteria

The completed solution will be evaluated against the following measurable, testable criteria:

* **SC-1 (Matching Speed & Automation):** The matching algorithm generates a ranked list of compatible tutors for any valid tutee request in under 5 seconds based on subject qualification and overlapping availability slots.
* **SC-2 (100% Schedule & Qualification Conflict Blocking):** The system prevents 100% of invalid match assignments where the tutor and tutee share zero overlapping free periods, the tutor is unqualified for the requested subject, or the tutor has reached `max_weekly_hours`.
* **SC-3 (Volunteer Hour Calculation Accuracy):** The system computes cumulative verified volunteer hours for every tutor with 0% mathematical discrepancy when cross-checked against manually calculated session records.
* **SC-4 (Relational Data Persistence):** All created profiles, availability slots, active matches, and session logs persist across application restarts in a normalized SQLite database without orphan records or data loss.
* **SC-5 (Administrative CSV Report Export):** The coordinator can generate and export a well-formed CSV report containing tutor IDs, names, session counts, and total verified hours filtered by a specified date range.
* **SC-6 (End-to-End Workflow Efficiency):** During usability testing, the coordinator can register a new student profile, run a match query, confirm a pairing, and log a completed session in under 3 minutes.

---

## 4. Computational Context

### Why a Computational Solution is Appropriate
Static spreadsheets treat schedule grids and subject lists as flat text, forcing a human operator to perform repetitive linear searches across disconnected tables. By transitioning to an **Object-Oriented Python application backed by a relational SQLite database**, the problem is modeled computationally:
* **Relational Normalization:** Separating `USERS`, `TUTORS`, `TUTEES`, `SUBJECTS`, `TUTOR_SUBJECTS`, `AVAILABILITY_SLOTS`, `MATCHES`, and `SESSIONS` eliminates redundant data entry and enforces referential integrity through primary and foreign keys.
* **Algorithmic Set Intersection & Ranking:** Representing student schedules as structured `(day_of_week, period_number)` objects allows the program to programmatically compute schedule intersections and sort eligible tutors by availability overlap and current workload in milliseconds.
* **Modular OOP Architecture:** Encapsulating entities into Python classes (`User`, `Tutor`, `Tutee`, `AvailabilitySlot`, `Match`, `SessionRecord`) isolates data validation and business logic from the user interface, making the codebase maintainable and testable.
