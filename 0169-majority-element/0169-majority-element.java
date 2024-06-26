import java.util.*;
public class Solution {
 public int majorityElement(int[] nums) {
        // Arrays.sort(nums);
        Arrays.sort(nums); // Sort the array
        
        int maxCount = 1; // Initial max count of elements is at least 1
        int count = 1; // Start counting from the first element
        int majorityElement = nums[0]; // Initialize majority element
        
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == nums[i - 1]) {
                count++; // Increment the count if the same element repeats
            } else {
                count = 1; // Reset count if a different element is found
            }
            
            if (count > maxCount) {
                maxCount = count; // Update max count
                majorityElement = nums[i]; // Update majority element
            }
        }
        
        return majorityElement;
    }
}