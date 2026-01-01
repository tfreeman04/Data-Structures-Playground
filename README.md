Data Structures Playground (Python)
📌 Overview

Data Structures Playground is a Python project that implements core data structures and algorithms from scratch and provides an interactive way to explore how they work internally.

The goal of this project is to demonstrate a strong understanding of fundamental computer science concepts, clean Python code, and practical software engineering practices such as testing and documentation.

🚀 Features

Implementations of core data structures without relying on built-in shortcuts

Common algorithms with clear time and space complexity explanations

Interactive command-line interface

Terminal-based visualizations

Comprehensive unit tests

🗂 Implemented Data Structures

Stack

Queue

Singly Linked List

Binary Search Tree

⚙️ Implemented Algorithms
Sorting

Bubble Sort — O(n²)

Merge Sort — O(n log n)

Quick Sort — O(n log n) (average)

Searching

Linear Search — O(n)

Binary Search — O(log n)

🧠 Design Decisions

All data structures are implemented from scratch to highlight internal behavior.

Code is organized into logical modules (structures, algorithms, visualizer).

Custom exceptions are used instead of silent failures.

Type hints and docstrings are included for clarity and maintainability.

📊 Time & Space Complexity Summary
Structure / Algorithm Time Complexity Space Complexity
Stack (push/pop) O(1) O(n)
Queue (enqueue/dequeue) O(1) O(n)
Linked List (search) O(n) O(n)
BST (insert/search) O(log n)* O(n)
Merge Sort O(n log n) O(n)

* Average case for balanced trees.

🖥 Sample Visualization
Stack (Top → Bottom)
-------------------
| 30 |
| 20 |
| 10 |
-------------------

Linked List
10 -> 20 -> 30 -> None

🛠 Tech Stack

Python 3.10+

Pytest

Rich (terminal visualization)

📂 Project Structure
data_structures_playground/
├── structures/
├── algorithms/
├── visualizer/
├── tests/
├── main.py
└── README.md

▶️ How to Run Locally
# Clone the repository
git clone https://github.com/yourusername/data-structures-playground.git
cd data-structures-playground

# Create virtual environment
python -m venv venv
source venv/bin/activate # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py

🧪 Running Tests
pytest

🧩 What I Learned

How common data structures work internally

Trade-offs between different implementations

Writing clean, testable Python code

Visualizing abstract concepts in a user-friendly way

🔮 Future Improvements

Add more data structures (Hash Map, Heap, Graph)

Add performance benchmarking

Web-based visualization interface

Persistence for user-defined structures

📬 Contact

Your Name
GitHub: https://github.com/tfreeman04

LinkedIn: https://linkedin.com/in/thomasfreeman-jones
