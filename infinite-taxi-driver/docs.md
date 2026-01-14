# Infinite Taxi Driver
In an alternate world, we encounter a remarkable city characterized by a perfect grid system. The city's roads run exclusively north-south and east-west, forming a grid where each block is a 1-mile by 1-mile square, with parallel roads spaced 1 mile apart. This grid extends infinitely in all directions. Each intersection on this grid can be represented as a coordinate point (x, y) (x, y). As a taxi driver, you start at a specific location with the goal of reaching your destination. However, you are restricted to driving only along the city's roads, meaning you can move solely in the cardinal directions: north, south, east, and west.

```

Legend:
         C: Cab
         D: Destination
         Initial Grid:
                    Infinitely More Expansions
                      . . . . . . . . . . .
                    Y . . . . . . . . . . .
                ... 6 _ _ _ _ _ _ _ _ _ _ _ ...
                ... 5 _ _ _ _ _ _ _ _ _ _ _ ...
                ... 4 _ _ _ _ _ _ _ _ _ _ _ ...
                ... 3 _ _ _ _ _ _ _ _ D _ _ ...
                ... 2 _ _ _ _ _ _ _ _ _ _ _ ...
                ... 1 _ _ _ _ _ _ _ _ _ _ _ ...
                ... 0 _ _ _ C _ _ _ _ _ _ _ ...
                     0 1 2 3 4 5 6 7 8 9 10 X
                      . . . . . . . . . . .
                      . . . . . . . . . . .
                    Infinitely More Expansions
```
We now introduce the concept of barriers. Barriers are placed at specific intersections, preventing the taxi driver from passing through them.

Given the presence of these barriers, there are two objectives:

Determine the shortest possible route the driver can take to reach their destination.
Determine the minimum time required for the driver to reach the destination, assuming each step the taxi takes is equivalent to 1 second.
```

Legend:
        C: Cab
        D: Destination
        X: Barrier
                        
Grid with Barriers:
  
    Infinitely More Expansions
      . . . . . . . . . . .
    Y . . . . . . . . . . .
... 6 _ _ _ _ _ _ _ _ _ _ _ ...
... 5 _ _ _ _ _ _ _ _ _ _ _ ...
... 4 _ _ _ _ _ _ _ X _ _ _ ...
... 3 _ _ _ _ _ _ _ X D _ _ ...
... 2 _ _ _ _ _ _ _ X X _ _ ...
... 1 _ _ _ _ _ _ _ X _ _ _ ...
... 0 _ _ _ C _ _ _ X _ _ _ ...
     0 1 2 3 4 5 6 7 8 9 10 X
      . . . . . . . . . . .
      . . . . . . . . . . .

    Infinitely More Expansions
```
**Example 1:**
```
Input:         
        Cab: (3,0)
        Destination: (8,3)
        Barriers: (7,0), (7,1), (7, 2), (7,3), (7,4), (8,2)
Output:
            any path of length 12 is a valid solution.
                        path = "NNNNNEEEEESS"
                        path = "SEEEEEENNNNW"
```

[execution time limit] 3 seconds (java)
[memory limit] 2g

