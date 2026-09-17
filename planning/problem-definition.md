# Planning & Problem Definition: Peer Tutoring Coordination System

## 1. User or Client
* **Primary Client:** High School Peer Tutoring Coordinator / Faculty Advisor (NHS Advisor, tutoring manager).
* **Target Audience & Users:**
  * **Administrator (Coordinator):** Needs an efficient way to manage student intakes, run matching logic, resolve scheduling conflicts, and generate reports for volunteer hours.
  * **Peer Tutors (Student Volunteers):** Need reliable tracking of their volunteer hours, clear session assignments, and subject matching.
  * **Tutees (Students Seeking Academic Support):** Need accurate pairings with tutors who are qualified in specific subject areas and available during the same time.

---

## 2. Problem Statement
At many high schools, peer tutoring programs are managed through paper forms or static spreadsheets. This manual approach introduces several major operational bottlenecks:

* **Time-Intensive Matching:** Manually comparing a tutee's subject needs and free time against dozens of potential tutors' availability grids takes long amounts of time.
* **High Schedule Conflict Rates:** Spreadsheet-based tracking frequently leads to human error, such as double-booking tutors, assigning tutors during conflicting times, or pairing students with mismatched subjects.
* **Inaccurate Volunteer Hour Logging:** Paper sign-in logs are frequently lost, miscalculated, or submitted late, creating extra work when verifying hours.
* **Lack of Dynamic Management:** When a student's schedule changes or a tutor drops out, re-evaluating and re-matching affected students requires re-checking all entries manually.

---

## 3. Proposed Computational Solution
The proposed solution is a dedicated **Peer Tutoring Coordination Management Application** (desktop or web database system) that automates matching, manages user profiles, and tracks session logs.

### Key Capabilities:
1. **Intake & Profile Management:** Allows the coordinator to create, update, and maintain profiles for Tutors and Tutees, including subject proficiencies, grade levels, and structured weekly availability matrices.
2. **Automated Matching Engine:** Implements logic that cross-references tutee subject requests and availability against tutor capacity to produce a list of optimal pairings, eliminating manual comparison.
3. **Session & Volunteer Hour Tracking:** Log individual tutoring sessions, automatically count cumulative volunteer hours per tutor, and maintain audit histories.
4. **Conflict Detection & Overrides:** Automatically flags overlapping timings or missing availability while allowing the coordinator to manually review and override matches when necessary.
5. **Data Export & Reporting:** Enables the coordinator to filter data by subject or student and export verified volunteer hour summaries as structured files.

---

## 4. Success Criteria
The success of the proposed system will be measured against the following explicit, testable criteria:

1. **Automated Matching Efficiency:** The system generates a ranked list of top-compatible tutors for any given tutee request within 5 seconds based on subject qualifications and overlapping free periods.
2. **Schedule Conflict Prevention:** The system blocks 100% of invalid match assignments where tutor and tutee availability matrices share zero overlapping time blocks or where the tutor is marked unqualified for the requested subject.
3. **Volunteer Hour Accuracy:** The application accurately calculates cumulative volunteer hours for 100% of logged sessions per tutor with no discrepancy when tested against manually verified session logs.
4. **Data Persistence & Integrity:** All student profiles, schedules, active pairings, and session logs persist across application restarts using a relational database without data loss or corruption.
5. **Report Generation:** The administrative interface successfully exports a correctly formatted summary report containing total verified tutor hours, session counts, and student IDs filtered by date range.
6. **Usability & Process Speed:** A trained administrator can complete student profile creation, run a match search, and assign a tutor in under 3 minutes total workflow time.

---

## 5. Investigation & Research
### Primary Research Question
> *"What exact visual or structured format is currently used and what logic is used to sort tutors and tutees"*
