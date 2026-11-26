# A 2<sup>o(*n*)</sup> Time Algorithm for 3-SAT

A deterministic algorithm solves 3-SAT on *n* variables in time 2<sup>o(*n*)</sup>, which refutes the Exponential Time Hypothesis (ETH). The algorithm in fact solves the harder problem #3-SAT, counting the satisfying assignments, in time 2<sup>O(*n* log log *n* / √log *n*)</sup>.

The result is purely asymptotic and says nothing about solving formulas in practice.

The result was discovered by an internal research Claude model. This folder holds the paper and its Lean 4 formalization, which was written by AI models.

Research artifact. Not maintained and not accepting contributions.
