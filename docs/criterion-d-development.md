# Criterion D: Development

## 1. Development Choices & Environment
* **What evidence belongs here?**
  * Summary of development environment, libraries/frameworks used (e.g., Python 3, `sqlite3`, GUI/web library, `csv`), and repository structure.
  * Justification of architectural or design adjustments made during implementation compared to the initial plan in Criterion C.
* **What do I still need to decide?**
  * Which third-party libraries (if any) am I using for UI or PDF/CSV generation, and why are they appropriate?

## 2. Programming Techniques & Algorithmic Implementation
* **What evidence belongs here?**
  * Annotated code snippets demonstrating computational thinking and technical complexity:
    * Object-Oriented principles (inheritance in `Tutor`/`Tutee`, encapsulation, modular methods).
    * Relational database operations (parameterized SQL queries, joins across `TUTOR_SUBJECTS` and `AVAILABILITY_SLOTS`, transaction safety).
    * Core matching, sorting/ranking, and error-handling/validation logic.
  * Explanation of challenges encountered during coding and how they were resolved (supported by Git commit history).
* **What do I still need to decide?**
  * Which 3–5 specific functions or classes best showcase algorithmic depth rather than basic CRUD operations?

## 3. Testing Evidence
* **What evidence belongs here?**
  * Completed test execution log matching the Criterion C test plan, showing actual outputs vs. expected outputs and pass/fail status.
  * Screenshots or terminal logs proving input validation, conflict blocking, database persistence across restarts, and accurate CSV report exports.
* **What do I still need to decide?**
  * How will I document failed initial tests and the subsequent bug fixes to demonstrate iterative testing?

## 4. Video Evidence
* **What evidence belongs here?**
  * Link/reference to a concise screencast demonstration (typically 2–5 minutes) showing the functioning application end-to-end.
  * Checklist of features demonstrated in the video: adding profiles, running the matching algorithm, triggering a schedule conflict warning, logging a session, and exporting a volunteer hour report.
* **What do I still need to decide?**
  * What script or walkthrough order will prove every Success Criterion clearly within the time limit?
