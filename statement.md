# Statement
## Problem Statement
> Task Management in an easy, fast, snappy way.

These days, people tend to use very bulky apps and websites to manage tasks and
store their data on cloud servers which might become a privacy issue. Due to this,
smaller tools that can easily and efficiently store data without compromising privacy
and network needs is a much-needed requirement.

**taskIt** solves that problem. It completely works offline, eliminating the need for a bulky Electron-based application that requires a lot of memory and CPU usage
overhead.

On top of that, it is purely CLI based, making it really snappy and quick, not requiring
any OS dependent UI libraries.

The best part about the app is its compatibility with SQLite3 Database files. This
ensures that your data stays with you at any time.

## Scope Of The Project
This project is a pure CLI-based Python project that allows users to perform CRUD (Create Read Update Delete) operations on tasklists and tasks within a tasklist.

Tasks are easily indexed and tasklists are known by their names.

The scope of this project is - 
- Single User Task Management
- Command Line Interface (CLI)
- CRUD for tasks and tasklists
- Saving Data into a `.db` SQLite3 file.

Out of scope things for this project are -
- Multi-collabrative Task Management
- Graphical User Interface (GUI)
- Third Party Integration


## Target Users
- Students who need to organize assignments, deadlines, and study schedules.
- Working professionals managing daily to-do lists and project tasks.
- Freelancers tracking multiple client tasks and deadlines.
- Anyone looking for a simple, distraction-free way to manage personal tasks.

## High-Level Features
- Create, Read, Update, Delete tasklists.
- Create, Read, Update, Check, Uncheck, Delete tasks in a particular tasklist.
- Set Priority Levels.
- Give Tags to any task.
- Simple Command Line Interface for ease of use.
- Persistent storage into SQLite3 Database.