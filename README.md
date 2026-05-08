````md
# Maze Generator & Solver (DFS Stack-Based Mouse)

## 📌 Project Overview
This project is a dynamic maze generator and maze solver implemented in Python using the Pygame library. The maze is generated using a stack-based Depth First Search (DFS) backtracking algorithm and then solved using another DFS traversal algorithm with backtracking.

The project visually demonstrates:
- Maze generation
- Stack-based DFS traversal
- Recursive backtracking behavior
- Maze solving
- Dead-end detection
- Cycle creation (bonus feature)

---

# 🧠 Maze Generation Algorithm

## DFS Stack-Based “Mouse” Logic
The maze is generated using a Depth First Search (DFS) backtracking algorithm.

A virtual “mouse” starts from a random cell on the left edge of the maze and performs the following steps:

1. Check neighboring cells (up, down, left, right)
2. Select a random unvisited neighbor
3. Remove the wall between the current cell and the selected neighbor
4. Move to the selected cell
5. Push the current position onto a stack
6. Continue until trapped in a dead end
7. Backtrack using the stack until all cells are visited

This process guarantees that:
- Every cell is reachable
- No isolated cells exist
- The maze forms a connected structure

Initially, the maze is generated as a **perfect maze**, meaning there is only one unique path between any two cells.

---

# 🧱 Maze Representation

The maze uses two 2D arrays to represent walls:

```python
northWall[row][col]
eastWall[row][col]
````

### Wall Meaning

* `1` → Wall exists
* `0` → Wall removed

### northWall

Represents the upper wall of each cell.

### eastWall

Represents the right wall of each cell.

This representation follows the data structure requirements specified in the assignment.

---

# 🔴 Maze Solver Algorithm

After maze generation is complete, the maze is solved using another DFS backtracking algorithm.

The solver:

* Starts from the maze entrance on the left edge
* Searches for the exit on the right edge
* Randomly explores available paths
* Uses a stack for traversal and backtracking
* Marks dead ends visually

### Visualization

* 🟢 Green Dot → Maze generation mouse
* 🔴 Red Dot → Maze solving mouse
* 🔵 Blue Cells → Dead ends discovered during solving

When the solver reaches a dead end:

1. The cell is marked blue
2. The algorithm backtracks using the stack
3. Another path is explored

---

# ⭐ Bonus Feature: Cycle Creation

To make the maze more complex, an additional feature was implemented based on the assignment addendum.

### Random Cycle Generation

With a probability of **1 in 20**, the generator removes an extra wall between already visited cells.

This creates:

* Cycles (loops)
* Multiple possible paths
* Non-perfect maze structures

This demonstrates how additional loops can affect traversal methods such as the “shoulder-to-the-wall” rule.

---

# 🖥️ Technologies Used

* Python
* Pygame

---

# ▶️ How to Run the Project

## 1. Install Pygame

```bash
pip install pygame
```

## 2. Run the Program

```bash
python main.py
```

---

# 📂 Project Structure

```text
maze-project/
│
├── main.py
├── maze.py
└── README.md
```

---

# 🎥 Features Demonstrated

✔ Dynamic maze generation
✔ DFS stack-based traversal
✔ Recursive backtracking
✔ Real-time visualization
✔ Maze solving using DFS
✔ Dead-end detection and marking
✔ Randomized traversal behavior
✔ Bonus cycle generation

---

# 📚 Concepts Demonstrated

* Depth First Search (DFS)
* Stack-based backtracking
* Graph traversal
* Maze generation algorithms
* Recursive exploration
* Dynamic visualization using Pygame

---

# 👨‍💻 Author

Developed as part of a maze generation and traversal assignment using Python and DFS-based algorithms.

Name: Selam Tewodros 
section 1
UGR/2331/16
Github ID : selamTedi

```
```
