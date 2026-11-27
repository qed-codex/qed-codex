---
{
  "module": "Challenge.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Codex (GPT-6.2 Astra)",
  "kind": "ai",
  "origin": "generated",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "license": "CC-BY-4.0"
}
---

# Two bounds for satisfiability, with different quantifiers

AI drafted this autoinformalization from the original source. It is open for mathematical review.

How fast can a deterministic machine decide whether a 3-CNF formula is satisfiable? For a nonnegative exponent $δ$, the source asks for a machine and a constant $c$ that work for every number of variables $n$ within $c 2^{δn}$ steps, rounded down. Take the infimum of the admissible exponents. The first challenge statement says this number is zero. Thus every positive exponent is attainable, with a machine and constant allowed to depend on the exponent. [MainResults.lean lines 92–107](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/MainResults.lean#L92-L107) · [MainResults.lean lines 117–122](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/MainResults.lean#L117-L122) · [Challenge.lean lines 8–13](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/Challenge.lean#L8-L13)

The second statement asks for a single machine that **counts** assignments. The machine and its constant $C$ are chosen before the clause width $k\ge1$. On the specified inputs, every variable occurs, $n\ge4$, the number of clauses $m$ is at least two, the clauses are distinct, and each has at most $k$ literals. The machine returns the count in $n+1$ bits, least significant first. [Challenge.lean lines 15–17](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/Challenge.lean#L15-L17) · [MainResults.lean lines 127–139](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/MainResults.lean#L127-L139) · [MainResults.lean lines 156–180](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/MainResults.lean#L156-L180)

The time bound takes the smaller of two exponents, one expressed through the number of clauses and the other through the number of variables. With logarithms to base two, the step budget is the integer part of $2^{C\min\{km/\sqrt{\log m},\, k^2n\log\log n/\sqrt{\log n}\}}$. Both declarations in the challenge have placeholder proof terms. [MainResults.lean lines 141–155](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/MainResults.lean#L141-L155) · [Challenge.lean lines 11–17](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/Challenge.lean#L11-L17)

I read this challenge and the cited definitions in MainResults. I did not build the project or check the counting algorithm.
