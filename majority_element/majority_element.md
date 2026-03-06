Idea = Using Hashset

Edge Case: Return max element. 

Time Complexity: O(n) 

Space Complexity: O(n)

I immedieately got to understood the problem that this was of counter, Python has inbuilt counter but I made counter of my own, initially i also initiated an integer called counter which would chaeck the number of occurences of that element, but that thing was redundent as we can add occurences with the help of old values in the hashmap itself.

I strugelled to return the element as max was not returning the key it was returning the value, then searched about the key = nums.get method in the max function. 