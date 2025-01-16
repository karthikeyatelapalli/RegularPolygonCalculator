# Regular Polygon Calculator

This Python program calculates the **perimeter** and **area** of a regular polygon based on the number of sides and the length of each side provided by the user. It employs the `RegularPolygon` class, which encapsulates the logic for handling polygon properties and calculations.

---

## **Features**
1. **RegularPolygon Class**:
   - Stores the number of sides and the side length of the polygon.
   - Provides methods to calculate:
     - **Perimeter**: The total length around the polygon.
     - **Area**: The enclosed space within the polygon, using trigonometric calculations.

2. **Interactive User Input**:
   - Prompts the user to enter valid inputs:
     - Number of sides (must be >= 3).
     - Side length (must be >= 0.1).
   - Rejects invalid inputs and prompts the user to re-enter.

3. **Detailed Output**:
   - Displays the number of sides, side length, perimeter, and area in a clear and formatted manner.

---

## **How to Run**

### **Requirements**
- Python 3.x
- No additional libraries are required (uses the built-in `math` module).

### **Steps**
1. Save the program as `polygon_calculator.py`.
2. Open a terminal or command prompt.
3. Navigate to the folder containing the program.
4. Run the program:
   ```bash
   python3 polygon_calculator.py
