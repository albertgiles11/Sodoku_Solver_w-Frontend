# Sudoku Solver w/Frontend

Simple Project which I used to Learn the basic of Flask and Frontend

## Features
* **Automatic Solving**: Solves any valid 9x9 Sudoku puzzle in milliseconds.
* **Validation**: Checks if the initial board configuration is valid.
* **Clean Web-Interference**: Provides a clear, easy-to-read board representation.
* **Efficiency**: Uses a recursive backtracking approach to find the solution.

## How it Works
The solver utilizes a **backtracking algorithm**, which:
1. Searches for an empty cell.
2. Attempts to place digits 1-9 in that cell.
3. Checks if the digit is valid according to Sudoku rules (Row, Column, and 3x3 Grid).
4. If valid, it moves to the next cell.
5. If no digit works, it "backtracks" to the previous cell and tries a different number.

## Getting Started

### Prerequisites
* Python, Flask, HTML, CSS, JavaScript
* Git

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/albertgiles11/Sodoku_Solver_w-Frontend
   ```
   
2. Install ```flask``` (if not already installed):

   ```
   pip install flask
   ```

3. Run the application :
 
   ```
   run sudoku.py
   ```
   
