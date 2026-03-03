# Solution 1

Idea = Brute force

Edge Case: Indices should not be same. 

Time Complexity: O(n^2) 

Space Complexity: O(1)

I tried first via brute force and got correct in one go

# Solution 2

Idea = Sorting + two Pointer

Edge Case: Indices should not be same. 

Time Complexity: O(n log n) 

Space Complexity: O(n) # created a separate sorted list using its indices

For optiimization I thought of sorting the lsit and then using two pointers get to the desired output b. Initially I got stuck in how to get the indices of the original unsorted list as I was returning the sorted list's indices. 


# Solution 3

Idea = Hashmap

Edge Case: Indices should not be same. 

Time Complexity: O(n) 

Space Complexity: O(n) # created a hashmap

Final optimization thought was of using hashmap, first took difference of current number from target, then searched the difference value in the hashmap as searching in the hashmap take constant time complexity. 
