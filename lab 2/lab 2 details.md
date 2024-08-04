# LCFSFrontier.py
Write a class LCFSFrontier such that when an instance of this class along with a graph object is passed to generic_search, lowest-cost-first search (LCFS) is performed. Your answer must also include the code for LocationGraph class since it is used in some test cases.

Notes
The search module is available here: search.py.
We require priority queues to be stable. We recommend you use heapq from the standard Python library. Read the documentation and pay attention to the "implementation notes" to see how you can make it stable.
It is recommended that you write LCFSFrontier as a subclass of Frontier class (instead of writing it from scratch). Although the Frontier class does not provide any functionality to reuse, subclassing makes it easier to check whether the new class implements all the methods required by the abstract base class. 

# location.py
In this question, you have to write a graph class for an agent that can be at certain locations on a 2D plane. The graph class is called LocationGraph. An object of this class is initialised with a dictionary called location and a non-negative number called radius. The keys of the dictionary are of type string and are the nodes of the graph. The value of each key is a pair of numbers (x, y) that designate the location of the node on the plane.

From a node, there will be an outgoing arc to every other node in the graph that is within the given radius. The action field of the arc must of the form "A->B" where A and B are placeholders for the tail node and the head node of the arc respectively. The cost of the arc is the straight-line distance between the tail node and the head node. The outgoing arcs of a node must be in the alphabetical order of the head nodes.

Notes

The search module is available here: search.py.
On a 2D plane, two points are within a radius r of each other if (and only if) the euclidean distance between the two points is less than or equal to r.
While from a scalability perspective, it makes sense to use an efficient data structure for querying points on a plane or to cache the edges explicitly, for this exercise, simply iterate through the sorted location dictionary every time the outgoing arcs of a node needs to be computed.
Remember to include all the import statements in the solution (or just paste your entire file if it does not produce unwanted output when it is imported by another module).
