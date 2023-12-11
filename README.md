<h1 align="center"> Fire Rescue Route Optimization: Prim's Algorithm for Drones</h1>
<h1 align="center"> Albert - 13522081 </h1>


## Table of Contents
* [Overview](#overview)
* [Description](#Description)
* [Features](#features)
* [How to use](#How-to-use)
* [Requirements](#Requirements)
* [Room for Improvement](#Room-for-Improvement)
* [Additinal Notes](#Additional-Notes)
<!-- <!-- * [License](#license) -- -->

## Overview
This repository contains the implementation of Prim's Algorithm tailored for optimizing fire rescue routes using drones. The project simulates an efficient pathfinding solution in a single-level hospital layout during fire emergencies, enhancing the speed and accuracy of rescue operations.


## Description
The program utilizes a graph-based representation of a hospital blueprint where rooms are nodes, and hallways are edges. Prim's Algorithm, augmented with a probability metric for human presence, computes the minimum spanning tree (MST) for potential rescue paths. This approach prioritizes not only the shortest distance but also the likelihood of finding individuals, showcasing a model that balances quick response with the effectiveness of the rescue mission.

## Features
* Graph-based simulation of a hospital layout for fire rescue.
* Prim's Algorithm with integrated probability metrics for optimizing rescue routes.
* Visual representation of the optimized path using Plotly for intuitive understanding.
* Flexible data structure to accommodate various building layouts.


## How-to-Use
1. **Clone/Download the Repository**: 
Ensure you have Git installed on your system to clone the repository or simply download the ZIP file.
```bash
git clone https://github.com/AlbertChoe/Prim-Algorithm_discreteMath.git
```
2. **Running the Program**:
Navigate to the program directory and run the following command in your terminal.
```bash
python main.py
```

3. **Using the Program**:
Upon running main.py, the program will process the predefined hospital layout and display the optimized rescue route in a new browser window.

## Requirements
- Python 3.7 or above
- Plotly for visualization
- NetworkX for graph-based modeling
- Numpy for numerical operations

To install the required Python libraries, run the following command :
```bash
pip install plotly networkx heapq numpy
```


## Room-for-Improvement
* Integration with real-time data for dynamic route optimization.
* Improved human detection capabilities simulation.
* User interface for emergency responders to interact with the system.


## Additional-Notes
This project is part of a research study aimed at improving emergency response efficiency through technological innovation. It is designed as a proof of concept and serves as a foundation for further development and integration into actual fire rescue systems. Contributions and feedback are welcome to enhance the functionality and applicability of the program.

    