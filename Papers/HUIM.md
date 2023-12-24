# HUIM

## Abstract

HUI-Miner uses a novel structure, called utility-list, to store both the utility information about an itemset and the heuristic information for pruning the search space of HUI-Miner.

### The TWU upper bound

 **<span style="color:red">TWU</span> of an itemset**:

​	the sum of the transaction utility for transactions containing the itemset.

Example:

$TWU(\{a,e\}) = TU(T_{0}) + TU(T_{3}) = 25 $ + 22 $ = 47 $ 

**Property:** The <span style="color:red">TWU</span> of an itemset is an upper bound on its utility, and all its supersets.

**Example:**

$\text{TWU}(\{a, e\}) = 47 \geq u(\{a, e\}) = 24$ and the utility of any superset of {a,e}