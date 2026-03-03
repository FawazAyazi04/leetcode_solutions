# Solution 1

Idea = Hashmap 

Time Complexity: O(n) 

Space Complexity: O(m)

First initialised hashmap and for collision used list with the help of defaultdict(lsit), loop over the strings in the list and sort the pertcular character in that element and treated them as keys.

Add the strings in the hashmap, if collision occurs then append as a list.

Append the values in the hashmap in another list and return 