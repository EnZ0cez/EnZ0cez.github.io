# LeetCode

## [169. 多数元素](https://leetcode.cn/problems/majority-element/)

给定一个大小为 `n` 的数组 `nums` ，返回其中的多数元素。多数元素是指在数组中出现次数 **大于** `⌊ n/2 ⌋` 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

**示例 1：**

```
输入：nums = [3,2,3]
输出：3
```

**示例 2：**

```
输入：nums = [2,2,1,1,1,2,2]
输出：2
```

 

**提示：**

- `n == nums.length`
- `1 <= n <= 5 * 104`
- `-109 <= nums[i] <= 109`

 

**进阶：**尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。

```java
class Solution {
    public int majorityElement(int[] nums) {
        int max = 0;
        int res = 0;
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int num : nums) {
            if (!map.containsKey(num)){
                map.put(num,1);
            }else {
                map.put(num,map.get(num)+1);
            }

        }
        //第一种遍历方式
        for (Map.Entry<Integer, Integer> entry : map.entrySet()){
            if (entry.getValue()>max){
                max = entry.getValue();
                res = entry.getKey();
            }
        }
        //第二种遍历方式
        for (Integer key :
                map.keySet()) {
            if (map.get(key) > max){
                max = map.get(key);
                res = key;
            }
        }
        return res;
    }
}
```

tips：注意Hashmap的两种遍历方式以及Hashmap的使用