INTRODUCTION
For this assessment, you will apply the algorithms and data structures you studied in this course to solve a real programming problem.
You will also implement an algorithm to route delivery trucks that will allow you to meet all delivery constraints while traveling under 140 miles.
You will then describe and justify the decisions you made while creating this program.

The skills you showcase in your completed project may be useful in responding to technical interview questions for future employment.
This project may also be added to your portfolio to show to future employers.

SCENARIO
The Western Governors University Parcel Service (WGUPS) needs to determine an efficient route and delivery distribution for their Daily Local Deliveries (DLD)
because packages are not currently being consistently delivered by their promised deadline. The Salt Lake City DLD route has three trucks, two drivers, and an
average of 40 packages to deliver each day. Each package has specific criteria and delivery requirements.

Your task is to determine an algorithm, write code, and present a solution where all 40 packages (listed in the attached “WGUPS Package File”) will be delivered
on time while meeting each package’s requirements and keeping the combined total distance traveled under 140 miles for both trucks. The specific delivery locations
are shown on the attached “Salt Lake City Downtown Map,” and distances to each location are given in the attached “WGUPS Distance Table.” The intent is to use the
program for this specific location and also for many other cities in each state where WGU has a presence. As such, you will need to include detailed comments to
make your code easy to follow and to justify the decisions you made while writing your scripts.

Keep in mind that the supervisor should be able to see, at assigned points, the progress of each truck and its packages by any of the variables listed in the
“WGUPS Package File,” including what has been delivered and at what time the delivery occurred.

ASSUMPTIONS
•   Each truck can carry a maximum of 16 packages, and the ID number of each package is unique.
•   The trucks travel at an average speed of 18 miles per hour and have an infinite amount of gas with no need to stop.
•   There are no collisions.
•   Three trucks and two drivers are available for deliveries. Each driver stays with the same truck as long as that truck is in service.
•   Drivers leave the hub no earlier than 8:00 a.m., with the truck loaded, and can return to the hub for packages if needed.
•   The delivery and loading times are instantaneous, i.e., no time passes while at a delivery or when moving packages to a truck at the hub
    (that time is factored into the calculation of the average speed of the trucks).
•   There is up to one special note associated with a package.
•   The delivery address for package #9, Third District Juvenile Court, is wrong and will be corrected at 10:20 a.m. WGUPS is aware that the
    address is incorrect and will be updated at 10:20 a.m. However, WGUPS does not know the correct address (410 S State St., Salt Lake City, UT 84111) until 10:20 a.m.
•   The distances provided in the WGUPS Distance Table are equal regardless of the direction traveled.
•   The day ends when all 40 packages have been delivered.

REQUIREMENTS
A. Identify a named self-adjusting algorithm (e.g., “Nearest Neighbor algorithm,” “Greedy algorithm”) that you used to create your program to deliver the packages.
    -> I used a Nearest Neighbor algorithm

B. Write an overview of your program, in which you do the following:
    1. Explain the algorithm’s logic using pseudocode.
        -> Create truck objects
        -> Create package hash map     | for x up to initial capacity: create hash buckets
        -> Import package data         | for each row in packageData: create package object, insert package object into hash map
        -> Sort packages into bags     | for each package ID: prioritize special deliveries and early deadlines
        ->                               for each remaining package: sort into quadrants
        ->                               for each quadrant: insert closest quadrants together
        ->                               for each overflow: insert if bag is not full
        -> Load/compile delivery route | move packages into new array, set package departure
        ->                               while undelivered is not empty: calculate closest neighbor, move package back to truck,
        ->                                                               update mileage, address, and delivery time
        ->                               send truck back to hub
        -> User interface              | while not done: ask user for input
        ->                                  if 1: ask for time, print all package info at given time
        ->                                  if 2: ask for time, ask for package id.  while not 0: print package at given time
        ->                                  if 3: print truck information
        ->                                  if 4: exit

    2. Describe the programming environment you used to create the Python application.
        -> Jetbrains
        -> PyCharm 2022.3.2 (Community Edition)
        -> Build #PC-223.8617.48, built on January 24, 2023
        -> Runtime version: 17.0.5+1-b653.25 amd64
        -> VM: OpenJDK 64-Bit Server VM by JetBrains s.r.o.
        -> Windows 10 10.0
        -> GC: G1 Young Generation, G1 Old Generation
        -> Memory: 2028M
        -> Cores: 16

    3. Evaluate the space-time complexity of each major segment of the program, and the entire program, using big-O notation.
        -> Overall Time Complexity  = O(N^2)
        -> Overall Space Complexity = O(N)

    4. Explain the capability of your solution to scale and adapt to a growing number of packages.
        -> My solution would be able to handle an increase in packages fairly well once the additional logic accounting for
        -> the overflow bag is uncommented.  As the number of packages increases I would recommend a proportional increase in
        -> the hash map's initial capacity.  The program does not, however, account for business hours and would run trucks
        -> regardless of how long it may take to deliver every package.

    5. Discuss why the software is efficient and easy to maintain.
        -> The software is very efficient in both data acquisition and lookup with a worst-case complexity of O(N^2) during package sorting
        -> and route compilation.  While not ideal, the routing algorithm does decrease in computation with each iteration.  The addition of
        -> quadrants allows for packages which are relatively close by to be loaded together, further increasing route efficiency.  Maintenance
        -> of the data files would be the key to keeping this program lightweight and portable.

    6. Discuss the strengths and weaknesses of the self-adjusting data structures (e.g., the hash table).
        -> The biggest advantages of this hash map are fast insertions and searches, with a worst-case runtime of O(N/10). However, the map is
        -> rather bulky as it uses a key, value pair and stores quite a lot of information for each package.

C. Write an original program to deliver all the packages, meeting all requirements, using the attached supporting documents
   “Salt Lake City Downtown Map,” “WGUPS Distance Table,” and the “WGUPS Package File.”
        1. Create an identifying comment within the first line of a file named “main.py” that includes your first name, last name, and student ID.
        2. Include comments in your code to explain the process and the flow of the program.

D. Identify a self-adjusting data structure, such as a hash table, that can be used with the algorithm identified in part A to store the package data.
    -> I implemented a ten bucket hash map using key, value pairs
        1. Explain how your data structure accounts for the relationship between the data points you are storing.
            -> Each package has a unique ID which is hashed and inserted into its corresponding bucket.  Package ID's 10, 20, 30, 40 are in bucket 0
            -> 1, 11, 21, 31 in bucket 1 etc.  This allows for fast insertion without collision and efficient searches.

E. Develop a hash table, without using any additional libraries or classes, that has an insertion function that takes the following components as input and inserts the components into the hash table:
    •   package ID number
    •   delivery address
    •   delivery deadline
    •   delivery city
    •   delivery zip code
    •   package weight
    •   delivery status (e.g., delivered, en route)

F. Develop a look-up function that takes the following components as input and returns the corresponding data elements:
    •   package ID number
    •   delivery address
    •   delivery deadline
    •   delivery city
    •   delivery zip code
    •   package weight
    •   delivery status (i.e., “at the hub,” “en route,” or “delivered”), including the delivery time

G. Provide an interface for the user to view the status and info (as listed in part F) of any package at any time, and the total mileage traveled by all trucks.
   (The delivery status should report the package as at the hub, en route, or delivered. Delivery status must include the time.)
    1.  Provide screenshots to show the status of all packages at a time between 8:35 a.m. and 9:25 a.m.
    2.  Provide screenshots to show the status of all packages at a time between 9:35 a.m. and 10:25 a.m.
    3.  Provide screenshots to show the status of all packages at a time between 12:03 p.m. and 1:12 p.m.

H. Provide a screenshot or screenshots showing successful completion of the code, free from runtime errors or warnings, that includes the total mileage traveled by all trucks.

I. Justify the core algorithm you identified in part A and used in the solution by doing the following:
    1.  Describe at least two strengths of the algorithm used in the solution.
        -> Short and easy to understand and maintain
        -> Provides a very efficient route, albeit not necessarily the best
    2.  Verify that the algorithm used in the solution meets all requirements in the scenario.
        -> The provided screenshots show each package is delivered on time and special delivery instructions were adhered to by the sorting algorithm
    3.  Identify two other named algorithms, different from the algorithm implemented in the solution, that would meet the requirements in the scenario.
        -> Dijkstra's Shortest Path
        -> Christofides Algorithm
            a.  Describe how each algorithm identified in part I3 is different from the algorithm used in the solution.
                -> Dijkstra's shortest path algorithm differs in its approach by not settling on simply the nearest neighbor.  The algorithm
                -> keeps track of a vertex's predecessor pointer and distances between adjacent points.
                -> Taken from zyBook ISBN: 978-1-5418-4355-4 | Chapter 6.11 Algorithm: Dijkstra's shortest path
                ->  "Dijkstra's algorithm initializes all vertices' distances to infinity (∞), initializes all vertices' predecessors to 0, and pushes all vertices
                ->   to a queue of unvisited vertices. The algorithm then assigns the start vertex's distance with 0. While the queue is not empty, the algorithm pops
                ->   the vertex with the shortest distance from the queue. For each adjacent vertex, the algorithm computes the distance of the path from the start vertex
                ->   to the current vertex and continuing on to the adjacent vertex. If that path's distance is shorter than the adjacent vertex's current distance,
                ->   a shorter path has been found. The adjacent vertex's current distance is updated to the distance of the newly found shorter path's distance, and
                ->   vertex's predecessor pointer is pointed to the current vertex. Dijkstra's algorithm initializes all vertices' distances to infinity (∞), initializes
                ->   all vertices' predecessors to 0, and pushes all vertices to a queue of unvisited vertices. The algorithm then assigns the start vertex's distance with 0.
                ->   While the queue is not empty, the algorithm pops the vertex with the shortest distance from the queue. For each adjacent vertex, the algorithm computes
                ->   the distance of the path from the start vertex to the current vertex and continuing on to the adjacent vertex. If that path's distance is shorter than the
                ->   adjacent vertex's current distance, a shorter path has been found. The adjacent vertex's current distance is updated to the distance of the newly found
                ->   shorter path's distance, and vertex's predecessor pointer is pointed to the current vertex."
                ->
                -> Christofides algorithm first creates a minimum spanning tree (MST) and finds all vertices with odd degree nodes.  Next is to create a minimum perfect matching
                -> by taking all possible paths between these nodes and calculate the combination with the shortest distance.  We then combine the matching and spanning tree to
                -> create a Eulerian multigraph which can have multiple edges between two nodes.  We then create a Eulerian tour by using Fleury's algorithm, which recursively
                -> computes the path that travels each edge of the graph once and visits every node.  The final step is to remove excess visits by creating a Hamiltonian path by
                -> walking along the Eulerian tour and checking if a city has already been visited.  If the node has been visited it is skipped and we move on to the next node.
                -> Detailed instructions for this algorithm can be found at https://cse442-17f.github.io/Traveling-Salesman-Algorithms/#christofides_header