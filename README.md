# Student Attendance and Performance Tracker

A Python-based system to track student attendance and academic performance and analyze the relationship between attendance and results.

## Problem Statement

In many colleges, attendance records and academic performance are maintained separately, making it difficult to identify patterns between attendance and student outcomes. This system aims to combine both datasets and provide simple insights that help identify at-risk students early.

## Features

- Role-based access for Admin, Teacher, and Student
- Subject-wise attendance tracking
- Marks entry and performance calculation
- Attendance percentage computation
- Identification of students with low attendance
- Basic analytics linking attendance and performance

## Tech Stack

- Language: Python
- Database: SQLite
- Interface: Console-based
- Version Control: Git

## Project Structure

├── main.py              # Entry point of the application
├── database.py          # Database connection and queries
├── models.py            # Data models (Student, Teacher, etc.)
├── attendance.py        # Attendance-related logic
├── performance.py       # Marks and performance calculations
├── analytics.py         # Attendance vs performance analysis

## How to Run

1. Clone the repository:
   git clone https://github.com/arya-kale007/Student-Performance-Tracker.git

2. Navigate to the project directory:
   cd Student-Performance-Tracker

3. Run the application:
   python main.py

Attendance Summary:
Student: John Doe
Subject: Mathematics
Attendance: 72%

Performance Summary:
Average Marks: 68
Status: Warning – Attendance below threshold

## What I Learned

- Designing a system using object-oriented principles
- Structuring a Python project with multiple modules
- Working with relational databases using SQLite
- Handling real-world edge cases in data tracking
- Writing clean, maintainable code

## Future Improvements

- Add a web-based interface
- Export reports as CSV or PDF
- Improve analytics with more statistical insights
- Add authentication security enhancements
