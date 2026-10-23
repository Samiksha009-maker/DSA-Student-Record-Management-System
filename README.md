# Student Record Management System (DSA Mini Project)

A beginner-friendly command-line project built with Python. It demonstrates basic data structures and algorithms through student record operations.

## Features
- Add, display, search, update, and delete student records
- Search by PRN/ID using **linear search**
- Sort marks from highest to lowest using **bubble sort**
- Optional sample records for quick testing
- Validates PRN uniqueness and marks (0–100)

## Requirements
- Python 3.8 or newer
- No external libraries required

## How to run
1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:
   ```bash
   python main.py
   ```
   On some systems, use `python3 main.py`.
4. Choose `7` to load sample data, then try options `2`, `3`, and `6`.

## DSA concepts
- **List:** stores the student records
- **Linear search:** finds a record by PRN/ID; worst-case time complexity **O(n)**
- **Bubble sort:** sorts records by marks; worst-case time complexity **O(n²)**
- **List insertion/deletion:** adds and removes records

## Limitations
Records are kept in memory and are cleared when the program exits. File/database storage can be added as a future improvement.

## Suggested GitHub description
A simple Python DSA mini project for managing student records using lists, linear search, and bubble sort.
