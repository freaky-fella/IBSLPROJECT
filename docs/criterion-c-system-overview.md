# Criterion C: System Overview

## 1. System Model & Architecture
* **What evidence belongs here?**
  * High-level system architecture diagram showing data flow between the User Interface, Application/OOP Logic Layer, and Relational Database.
  * Entity-Relationship Diagram (ERD) illustrating tables (`USERS`, `TUTORS`, `TUTEES`, `AVAILABILITY_SLOTS`, `SUBJECTS`, `TUTOR_SUBJECTS`, `MATCHES`, `SESSIONS`), primary/foreign keys, and cardinality.
* **What do I still need to decide?**
  * Should availability be modeled strictly by school period numbers (`1–4`) and days (`Mon–Fri`), or by start/end timestamps?

## 2. Components & Relationships
* **What evidence belongs here?**
  * UML Class Diagram showing class hierarchies (e.g., `Tutor` and `Tutee` inheriting from `User`), attributes, data types, methods, and object relationships.
  * Justification for key data structure choices (e.g., junction table for Many-to-Many subject proficiencies, lists/dictionaries or priority queues for candidate ranking).
* **What do I still need to decide?**
  * Which helper/controller classes (e.g., `MatchEngine`, `DatabaseManager`, `ReportGenerator`) need to be added to my UML class diagram alongside the entity models?

## 3. Algorithms & Logic Flow
* **What evidence belongs here?**
  * Flowcharts and/or structured pseudocode for core computational processes:
    1. **Tutor-Tutee Matching Algorithm:** Filtering by subject, intersecting availability slots, checking `max_weekly_hours`, and ranking candidates.
    2. **Conflict Detection & Validation:** Preventing double-bookings or invalid assignments.
    3. **Volunteer Hour Aggregation:** Calculating verified session durations per tutor.
* **What do I still need to decide?**
  * What exact tie-breaking rule will the ranking algorithm use when two tutors have identical schedule availability (e.g., lowest current active tutee count vs. highest proficiency level)?

## 4. Testing Strategy
* **What evidence belongs here?**
  * Structured test plan table covering **normal**, **boundary/edge**, and **abnormal/invalid** inputs.
  * Explicit test cases mapped directly to every Success Criterion (`SC-1` to `SC-6`) from Criterion A, specifying test inputs, expected outputs, and verification methods.
* **What do I still need to decide?**
  * What synthetic dataset (e.g., 20 tutors, 30 tutees, edge-case schedule conflicts) will I create to benchmark matching speed and accuracy?
