## 2.20

[15. 三数之和](https://leetcode.cn/problems/3sum/)

中等

给你一个整数数组 `nums` ，判断是否存在三元组 `[nums[i], nums[j], nums[k]]` 满足 `i != j`、`i != k` 且 `j != k` ，同时还满足 `nums[i] + nums[j] + nums[k] == 0` 。请你返回所有和为 `0` 且不重复的三元组。

**注意：**答案中不可以包含重复的三元组。



**示例 1：**

```
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。
```

**示例 2：**

```
输入：nums = [0,1,1]
输出：[]
解释：唯一可能的三元组和不为 0 。
```

**示例 3：**

```
输入：nums = [0,0,0]
输出：[[0,0,0]]
解释：唯一可能的三元组和为 0 。
```

```Java
public static List<List<Integer>> threeSum(int[] nums) {

    Arrays.sort(nums);

    List<List<Integer>> res = new ArrayList<>();
    for (int i = 0; i < nums.length; i++) {
        if(i>0&&nums[i] == nums[i-1]) continue;
        for (int j = i+1 ; j<nums.length; j++){
            if(j >i+1 && nums[j] == nums[j-1]) continue;
            for (int k = nums.length-1 ; k > j ;k--){
                if (nums[i] + nums[j] +nums[k] == 0){
                    List<Integer> group = new ArrayList<>();
                    group.add(nums[i]);
                    group.add(nums[j]);
                    group.add(nums[k]);
                    group.sort(null);

                    res.add(group);
                }
                if (nums[i] + nums[j] +nums[k] < 0) break;
            }
        }
    }

    return res;
}
```

问题：有使用双指针的思想，但时间复杂度太高，三个n的循环导致O(n^3) 的时间复杂度

解决思路：用双指针的时候利用三数之和为0的特性，以及数组已经排好序的特性，若此时三数之和小于0，则应增大第二指针，使得三数之和变大，若三数之和小于0，则减小第三指针，使得三数之和变小。同时这样的思路可以减少时间复杂度，因为最多移动n次，而不是循环套循环

```Java
public List<List<Integer>> threeSum(int[] nums) {
    Arrays.sort(nums);

    List<List<Integer>> res = new ArrayList<>();
    for (int i = 0; i < nums.length; i++) {
        if (i > 0 && nums[i] == nums[i - 1]) {
            continue;
        }
        int left = i + 1;
        int right = nums.length - 1;
        while (left < right) {
            int sum = nums[i] + nums[left] + nums[right];
            if (sum == 0) {
                res.add(Arrays.asList(nums[i], nums[left], nums[right]));
                while (left < right && nums[left] == nums[left + 1]) {
                    left++;
                }
                while (left < right && nums[right] == nums[right - 1]) {
                    right--;
                }
                left++;
                right--;
            } else if (sum < 0) {
                left++;
            } else {
                right--;
            }
        }
    }

    return res;
}
```

## 2.21

[42. 接雨水](https://leetcode.cn/problems/trapping-rain-water/)

已解答

困难

给定 `n` 个非负整数表示每个宽度为 `1` 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

 

**示例 1：**

![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/22/rainwatertrap.png)

```
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 
```

**示例 2：**

```
输入：height = [4,2,0,3,2,5]
输出：9
```

一开始采用遍历的思想，对于每个位置往左和往右找到maxHeight，为leftMax和rightMax，根据每个点的leftMax和rightMax以及当前位置的值来得到当前位置可以容纳的雨水。

```Java
public int trap(int[] height) {
        int[] leftMax = new int[height.length];
        int[] rightMax = new int[height.length];
        for (int i = 0; i < height.length; i++) {
            leftMax[i] = 0;
            rightMax[i] = 0;
            for (int j = i-1; j >= 0; j--) {
                if (height[j] > leftMax[i]){ leftMax[i] = height[j];}
            }
            for (int k = i + 1; k < height.length;k++){
                if (height[k] > rightMax[i] ){ rightMax[i] = height[k];}
            }
        }
        int rain = 0;
        for (int i = 0; i < height.length; i++) {
            if (Math.min(leftMax[i], rightMax[i] ) - height[i] > 0)
                rain += Math.min(leftMax[i], rightMax[i] ) - height[i];
        }

        return rain;  
    }
```

上面这段代码在逻辑计算上是正确的，但是在计算时间上过多了。时间复杂度为O(n^2)。

优化思路：使用动态规划的思想，对这个数组遍历两次，维护leftMax数组和rightMax数组。根据上一个位置的leftMax值来计算当前位置的leftMax值。

```Java
public static int trap(int[] height) {
    int[] leftMax = new int[height.length];
    int[] rightMax = new int[height.length];
    leftMax[0] = height[0];
    rightMax[height.length-1] = height[height.length-1];
    for (int i = 1; i < height.length ; i++) {

        if (height[i] > leftMax[i-1]){
            leftMax[i] = height[i];
        }else leftMax[i] = leftMax[i-1];

    }
    for (int j = height.length-2 ; j >=0 ;j--){
        if (height[j] > rightMax[j+1]){
            rightMax[j] = height[j];
        }else rightMax[j] = rightMax[j+1];
    }
    int rain = 0;
    for (int i = 0; i < height.length; i++) {
        if (Math.min(leftMax[i], rightMax[i] ) - height[i] > 0)
            rain += Math.min(leftMax[i], rightMax[i] ) - height[i];
    }

    return rain;
}
```

动态规划优化后的时间复杂度:O(n)

[3. 无重复字符的最长子串](https://leetcode.cn/problems/longest-substring-without-repeating-characters/)

已解答

中等

给定一个字符串 `s` ，请你找出其中不含有重复字符的 **最长 子串** 的长度。

 

**示例 1:**

```
输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
```

**示例 2:**

```
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
```

**示例 3:**

```
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
```

 

**提示：**

- `0 <= s.length <= 5 * 104`
- `s` 由英文字母、数字、符号和空格组成

思路：采用滑动窗口，





# 3.3

46. 全排列

给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

示例 1：

输入：nums = [1,2,3]

输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

思想：回溯法

我的代码问题：

* 直接修改原数组导致状态污染
* 在递归中直接调用arrayList.remove(num)，这会永久修改原始数组，导致后续递归无法获取完整的元素集合。
* 路径列表 (list) 未回溯
* list.add(num)后没有在递归返回时移除元素，导致所有分支共享同一个列表对象，路径被错误叠加。
* 结果列表存储引用而非拷贝
* res.add(list)直接添加了list的引用，所有结果最终指向同一个列表对象，内容会被覆盖为最后一次递归的结果。
* 主循环逻辑错误
* 外层循环试图以每个元素为起点生成排列，但第一次递归后原数组已被清空，后续循环无法执行。

代码：

```java
public static List<List<Integer>> permute(int[] nums) {
    List<List<Integer>> res = new ArrayList<>();
    backtrack(nums, new ArrayList<>(), res, new boolean[nums.length]);
    return res;
}    
private static void backtrack(int[] nums, List<Integer> current, List<List<Integer>> res, boolean[] used) {
    if (current.size() == nums.length){
        res.add(new ArrayList<>(current));
        return;
    }
    for (int i = 0; i < nums.length; i++) {
        if (!used[i]) {
            current.add(nums[i]);
            used[i] = true;
            backtrack(nums, current, res, used);
            current.removeLast();
            used[i] = false;
        }
    }
}
```



## 3.5

78. 子集

给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

示例 1：

输入：nums = [1,2,3]

输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

开始的思路：使用回溯法，从[1,2,3]开始逐个减少元素

* 导致的问题：如果包含所有节点，会有多余元素。并且直接将原数组添加到结果集中，然后再进行子集生成，这种处理方式不符合子集生成的逻辑，应该从空集开始逐步生成所有子集。

正确思路：从空集开始生成，用是否考虑每一个元素的思路，得到全部子集。再使用一个记录步骤数的变量来控制最后的子集添加进res

代码：

```java
public static List<List<Integer>> subsets(int[] nums) {
    List<List<Integer>> res = new ArrayList<>();
    allSubsets(nums, new ArrayList<>(),res,0);
    return res;
}

public static void allSubsets(int[] nums, List<Integer> cur, List<List<Integer>> res, int l){
    if (l == nums.length){
        res.add(new ArrayList<>(cur));
        return;
    }
    cur.add(nums[l]);
    allSubsets(nums,cur,res,l+1);
    cur.removeLast();
    allSubsets(nums, cur, res,l+1);
}
```





## 3.7

[105. 从前序与中序遍历序列构造二叉树](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

中等

给定两个整数数组 `preorder` 和 `inorder` ，其中 `preorder` 是二叉树的**先序遍历**， `inorder` 是同一棵树的**中序遍历**，请构造二叉树并返回其根节点。

**示例 1:**

![img](./assets/tree.jpg)

```
输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
输出: [3,9,20,null,null,15,7]
```

我的思路：递归，找到每一个节点左子树和右子树的先序遍历和中序遍历，根据这些遍历数组来判断，递归直到子树为null

我的代码：

```java
public static TreeNode buildTree(int[] preorder, int[] inorder) {
    TreeNode root = new TreeNode(preorder[0]);
    ArrayList<Integer> leftInorder = new ArrayList<>();
    ArrayList<Integer> leftPreorder = new ArrayList<>();
    ArrayList<Integer> rightInorder = new ArrayList<>();
    ArrayList<Integer> rightPreorder = new ArrayList<>();
    for (int i = 0; i < inorder.length; i++) {
        if (inorder[i] == root.val){
            for (int i1 = 0; i1 < i; i1++) {
                leftInorder.add(inorder[i1]);
                leftPreorder.add(preorder[i1+1]);
            }
            for (int j = 0; j < inorder.length-i-1; j++) {
                rightInorder.add(inorder[i+j+1]);
                rightPreorder.add(preorder[leftPreorder.size()+1+j]);
            }
        };
    }
    if (leftPreorder.isEmpty()){
        root.left = null;
    }else root.left = new TreeNode(leftPreorder.getFirst());
    if (rightPreorder.isEmpty()){
        root.right = null;
    }else root.right = new TreeNode(rightPreorder.getFirst());
    recurBuild(root.left,leftInorder,leftPreorder);
    recurBuild(root.right,rightInorder,rightPreorder);
    return root;
}

public static void recurBuild(TreeNode root, ArrayList<Integer> inorder, ArrayList<Integer> preorder){
    if (root == null) return;
    ArrayList<Integer> leftInorder = new ArrayList<>();
    ArrayList<Integer> leftPreorder = new ArrayList<>();
    ArrayList<Integer> rightInorder = new ArrayList<>();
    ArrayList<Integer> rightPreorder = new ArrayList<>();
    for (int i = 0; i < inorder.size(); i++) {
        if (inorder.get(i) == root.val){
            for (int i1 = 0; i1 < i; i1++) {
                leftInorder.add(inorder.get(i1));
                leftPreorder.add(preorder.get(i1+1));
            }
            for (int j = 0; j < inorder.size()-i-1; j++) {
                rightInorder.add(inorder.get(i+j+1));
                rightPreorder.add(preorder.get(leftPreorder.size()+j+1));
            }
        };
    }
    if (leftPreorder.isEmpty()){
        root.left = null;
    }else root.left = new TreeNode(leftPreorder.getFirst());
    if (rightPreorder.isEmpty()){
        root.right = null;
    }else root.right = new TreeNode(rightPreorder.getFirst());
    recurBuild(root.left,leftInorder,leftPreorder);
    recurBuild(root.right,rightInorder,rightPreorder);

}
```

**问题：**

* 数组复制导致的高时空开销
  * 改用数组中的索引来代替数组复制，直接在原数组上操作。
* 线性查找根节点效率低
  * 预处理中序数组，用**哈希表**来存储**值到索引**的映射，实现O(1)查找

* 边界处理条件不足
  * if (preorder.length == 0 || inorder.length == 0) return null;

改进代码：

```java
public TreeNode buildTree(int[] preorder, int[] inorder) {
    this.preorder = preorder;
    this.inorder = inorder;
    // 预处理中序的哈希映射
    for (int i = 0; i < inorder.length; i++) {
        inorderMap.put(inorder[i], i);
    }
    return build(0, preorder.length-1, 0, inorder.length-1);
}

private TreeNode build(int preStart, int preEnd, int inStart, int inEnd) {
    if (preStart > preEnd || inStart > inEnd) return null;
    
    int rootVal = preorder[preStart];
    TreeNode root = new TreeNode(rootVal);
    int rootIdx = inorderMap.get(rootVal); // 中序根的位置
    int leftSize = rootIdx - inStart; // 左子树节点数
    
    root.left = build(preStart+1, preStart+leftSize, inStart, rootIdx-1);
    root.right = build(preStart+leftSize+1, preEnd, rootIdx+1, inEnd);
    return root;
}
```
综合来说思路没有问题，但是对于一些数据的处理不够熟悉，造成了太多空间和时间的浪费。