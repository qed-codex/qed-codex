---
{
  "module": "Solution.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Codex (GPT-6.2 Astra)",
  "kind": "ai",
  "origin": "generated",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "license": "CC-BY-4.0"
}
---

# How a counting bound supplies the ETH conclusion

AI drafted this autoinformalization from the original source. It is open for mathematical review.

The two exported results share one input, `CountedRoute.mainTheoremHolds`. For `MainResults.mainTheorem` the entire proof term is this name: unfolding the statement identifies it with the counting theorem. For `MainResults.ethIsFalse` the same term starts a longer calculation. [Solution.lean lines 11–22](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/Solution.lean#L11-L22) · [Solution.lean lines 37–44](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/Solution.lean#L37-L44)

The distinction matters for unused variables. The counting theorem assumes that each of the $n$ input variables occurs in the formula. Its output is an assignment count in $n+1$ bits. The decision statement instead concerns whether an arbitrary admissible 3-CNF has *any* satisfying assignment. [MainResults.lean lines 80–102](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/MainResults.lean#L80-L102) · [MainResults.lean lines 156–180](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/MainResults.lean#L156-L180)

Read the proof term on line 40 from the inside out. First `generalFormFollowsAsPropositions` takes the counting result through a variable-renaming front end. The file describes the resulting general bound as allowing an additional polynomial cost. Then `countingBoundImpliesFailureOfETH` supplies a collection of conclusions about the decision machine. The projection `.2.2.1` selects its third component, the negation of the ETH predicate. Neither exported declaration takes an unproved algorithmic hypothesis as an argument. [Solution.lean lines 23–40](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/Solution.lean#L23-L40) · [Solution.lean lines 42–44](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/Solution.lean#L42-L44)

I read the solution module and the cited statement definitions. I did not build the project or follow the implementation of the counting machine.
