# LCIM: Mining Low Cost High Utility Itemsets

## Introduction

A popular subfield of data mining is pattern mining. The aim is to apply algorithms to find interesting patterns in data that meet some user-defined constraints.

Frequent itemset mining(FIM) $\rightarrow$ High utility itemset mining
(HUIM) 

High utility itemset is sets of values that bring high benefits, as measured by a utility function. 

Nonetheless, the focus of HUIM is on the utility of patterns and the cost associated with these patterns is ignored.

But jointly considering utility and cost in pattern mining is desirable but not simple and could be done in many ways. Because utility and cost may be expressed in different units. Like in e-learning, utility may be the grades you get, an cost may be the hours you spend.

Besides, for such applications, it is more meaningful to consider the average utility and the average cost of patterns rather than their sums.

Hence, this motivates us to separately model the utility and cost, and to consider their average.

The key contributions :

1. A novel problem called low cost high utility itemset mining is formalized to introduce the concept of cost in itemset mining. The aim is to find itemsets that have a high average utility, and a low average cost. 
2. An algorithm named LCIM (Low Cost Itemset Miner) is designed to solve this problem efficiently.  
3. To reduce the search space, LCIM applies a lower bound on the average cost called Average Cost Bound (ACB).

## The LCIM algorithm

