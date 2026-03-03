# Solution 1

Idea = Hashmap 

Time Complexity: O(nm) m = length of the hashmap

Space Complexity: O(m)

As I saw that it need comparison my first thought went into using hashmap, first store the cahracters as per their indices, then compare, after some time I realised that this appraoch is not suitable, but still went to solve by it using hwlp from  chatgpt

First build a hashmap for first string, then based on that check the other string, if any changes in the character occur break the loop and make a new hashmap till that string, simply do the same with other string.

Sort the hashmap based on the keys, I know this was overkill but still I did that and returned the result by adding the elements in that hashmap in a string.

# Solution 2

Idea = String 

Time Complexity: O(nm) m = length of the list

Space Complexity: O(1)

I couldn't come up with this solution on my own, so watched the neetcode video, then got on to solve this on my own.

The approach was take first string as the reference and then check that string with other strings character by character, if any difference then break the loop otherwise add that character in the result and return the result.