# Map-Coloring-Using-CSP

## Project Overview

### CSP for Map Coloring

The CSP model for this problem consists of:

Variables: Each region on the map, which represents a node, needs to be assigned a color.
Domains: The set of possible colors (e.g., red, green, blue, yellow) for each region.
Constraints: Adjacent regions (nodes connected via edges) must not share the same color.

The project leverages CSP solving techniques to ensure that all constraints are satisfied across the map while using the minimum number of colors possible.

### Components

Map Representation: The map is modeled as a graph where regions are nodes and borders between regions are edges. Each region must be colored such that no adjacent regions (connected by edges) share the same color.
Solver Logic: The core of the project resides in the CSP solver, which handles:
Variable Selection: Deciding which region to color next based on heuristics (e.g., Minimum Remaining Values).
Constraint Propagation: Ensuring that when a region is colored, the constraints are propagated to its neighbors.
Backtracking: A recursive approach to resolving conflicts when a constraint violation occurs.
Utilities: Several utility functions are used to support the CSP solver, such as loading map data, parsing the region adjacency, and visualizing the colored map.

### Maps Used

USA: A sample map showing different states in the United States.
Iran: A regional map of Iran to demonstrate the algorithm's flexibility in handling various geographies.
Tehran Province: A smaller subset of the Iranian map to showcase localized coloring problems.

### Key Files

map.py: The main file that handles loading the map and executing the coloring algorithm.
solver.py: Contains the CSP solver logic, implementing techniques such as backtracking and constraint propagation.
utils.py: Utility functions to assist with loading maps, defining regions, and visualizing results.

### Problem Scope

This project provides a flexible platform for solving the map coloring problem, capable of being extended to other CSP-related problems. The logic of the solver.py can be easily adapted to different domains, and the map handling in map.py can be modified to accommodate different sets of constraints or variable structures.

### Visualization

Sample maps (USA, Iran, and Tehran Province) are included to help visualize the output of the coloring algorithm. These maps demonstrate how the CSP solver efficiently assigns colors to regions under the given constraints.

### Constraints Management

The adjacency matrix or graph is built based on the input map, ensuring that no two connected nodes (regions) share the same color.
The algorithm considers various heuristics for optimizing the coloring process, reducing the complexity of backtracking.
