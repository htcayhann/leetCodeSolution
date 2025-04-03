import java.util.*;

class Solution {
    public int partitionString(String s) {
        int count = 0;
        Set<Character> seen = new HashSet<>(); 
        
        for (char ch : s.toCharArray()) {
            if (seen.contains(ch)) { // If duplicate character found, start new partition
                count++;
                seen.clear();
            }
            seen.add(ch);
        }
        
        if (!seen.isEmpty()) {
            count++; 
        }
        
        return count;
    }
}
