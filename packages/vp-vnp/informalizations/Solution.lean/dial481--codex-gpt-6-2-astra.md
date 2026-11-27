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

# How the five circuit statements acquire proof terms

AI drafted this autoinformalization from the original source. It is open for mathematical review.

The solution imports the statement definitions and `Paper.Approximate`. It defines two conversions between polynomial-family records. Both preserve the variable type at each index, the finite-type instance and the polynomial itself. They let the proof apply a library result about one representation of a family to a goal about the other. [Solution.lean lines 6–23](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Solution.lean#L6-L23)

For the exact lower bound the file takes a constant $c$ and its positivity from `Paper.thm_allfields`. The challenge quantifies over every natural number $p$ as a possible characteristic. When $p$ is zero or prime, the imported bound supplies the result. In the remaining case Lean can choose threshold zero: a field of characteristic $p$ would contradict the theorem that a field’s characteristic is prime or zero. The approximate lower bound uses the same split, taking its estimate from the first component of `Paper.thm_approx`. [Solution.lean lines 25–31](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Solution.lean#L25-L31) · [Solution.lean lines 38–44](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Solution.lean#L38-L44)

For proper inclusion the proof transports both parts of `Paper.cor_allclasses` through the family conversions: inclusion forwards and the contradiction from a supposed reverse inclusion backwards. The second component of `Paper.thm_approx` rules out containment in the approximate class. The real-permanent conclusion is supplied directly by `Paper.thm_main`. [Solution.lean lines 33–36](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Solution.lean#L33-L36) · [Solution.lean lines 46–53](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Solution.lean#L46-L53)

I read the solution file and its challenge statements. I did not build the project or inspect the internal proofs of the imported paper theorems. [Challenge.lean lines 17–31](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Challenge.lean#L17-L31)
