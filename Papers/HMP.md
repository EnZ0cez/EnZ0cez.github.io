# HMP: Efficient Heuristic Algorithms for MDL-Based Itemset Mining

**Enze Chen**, Muhammad Zohaib Nawaz, M. Saqib Nawaz, Philippe Fournier-Viger

*Applied Soft Computing*, Volume 187, Article 114314, February 2026 (Elsevier)

DOI: [10.1016/j.asoc.2025.114314](https://doi.org/10.1016/j.asoc.2025.114314) · [ScienceDirect](https://www.sciencedirect.com/journal/applied-soft-computing/vol/187/suppl/C)

## Abstract

Frequent itemset mining often overwhelms users with large pattern sets that hinder interpretation, so recent research has turned to discovering compact and informative pattern sets based on the Minimum Description Length (MDL) principle. Existing MDL-based algorithms, however, still suffer from long runtimes and do not guarantee optimal compression.

This paper introduces **HMP** (Heuristic MDL-based Pattern mining), a framework with two alternative heuristic algorithms for MDL-based pattern selection:

- **HMP-Sa** — a Simulated Annealing (SA) based optimization process that explores the search space more efficiently, reducing computational time while producing more representative itemsets.
- **HMP-Hc** — a Hill Climbing (HC) based approach.

Both algorithms adopt a partial coverage function that enables partial and heuristic MDL-based compression, and rely on a binary matrix optimization to efficiently generate and evaluate item pairs. Extensive experiments show that HMP-Sa and HMP-Hc outperform the state-of-the-art GRIMP algorithm as well as the earlier KRIMP and SLIM algorithms in both runtime and compression ratio, with HMP-Sa also demonstrating strong downstream classification performance.

## Keywords

Itemset mining · Minimum Description Length (MDL) · Simulated annealing · Hill climbing · Pattern selection

## BibTeX

```bibtex
@article{ChenNNF26,
  title   = {HMP: Efficient heuristic algorithms for MDL-based itemset mining},
  author  = {Enze Chen and Muhammad Zohaib Nawaz and M. Saqib Nawaz and Philippe Fournier-Viger},
  journal = {Applied Soft Computing},
  volume  = {187},
  pages   = {114314},
  year    = {2026},
  doi     = {10.1016/j.asoc.2025.114314}
}
```

## Related notes on this site

This work grew out of my earlier study notes and experiments:

- [KRIMP](Papers/KRIMP.md) · [SLIM](Papers/SLIM.md) · [GRIMP](Papers/GRIMP.md) · [MDL](Papers/MDL.md)
- [Simulated Annealing](Papers/Simulated%20Annealing.md)
- [Pre-SA_KRIMP](Programming/Pre-SA_KRIMP.md) · [SA-KRIMP 实验结果](Programming/Expriment%20Result%20for%20SA-KRIMP.md)
