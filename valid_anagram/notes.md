I first thought that it can be solved via hashset, so I used that approach then gor into the very basic error that if the lengths of the two strings are not same then they are not a valid anagram. Added that edge case.\
Got stuck in a test case where the length of strings were same and characters were also same, so hashset returns the valid anagram which was not the case as the counts were different.\
Then I tried hashmap using counters solved it but again I failed becuase I was not considering what if that key is not in the hashset at first place. after that used .get(value,0 //default value) function then solved this question successfully.\

Idea: Hashmap
Edge Case: If length not same then not an anagram, and whether that key is in the hashmap.
Time Complexity: O(n)
Space Complexity: O(1)