Idea = using loop only and del function

Time Complexity: O(n) 

Space Complexity: O(1)

At first I started with for loop, and then checking the value a the i_th place is equals to the value to be removed or not, but it was going out of index as everytime the it removes the element the length gets updated but not the for loop.

Then used while loop and also added else condition as if the values doesnt match then loop should move ahead but when it matches then the loop should start from 0 again.

This creates some unnecessary comparisions but still makes the overall TC as factor of n. 