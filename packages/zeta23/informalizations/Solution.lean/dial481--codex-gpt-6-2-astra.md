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

# Matching the zero counts and the Montgomery–Taylor constant

AI drafted this autoinformalization from the original source. It is open for mathematical review.

For the six initial zeta estimates the solution can cite the library theorems directly. For example, the dyadic simple-zero estimate has `Ncount T (2*T)` on the left, weighted by $2/3-ε$, and `N0simple T (2*T)` on the right. Its proof term is `Zeta23.thmB₀_mult`. The cumulative version cites a different theorem with lower endpoint zero. The same dyadic/cumulative pairing appears for distinct zeros on the critical line and for distinct zeros throughout the strip. [Solution.lean lines 52–74](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Solution.lean#L52-L74)

The sharper estimates need an extra identification. The library expresses its constant as `cStar 1`; the challenge uses `cMT`. A local lemma rewrites the former using the library’s tangent formula and unfolds both the challenge constant and the angle at parameter one. The expressions then agree by reflexivity. For each refined zeta bound the proof specializes a library theorem, unfolds the relevant proportion (`HD` or `GD`) and substitutes this equality. [Solution.lean lines 24–27](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Solution.lean#L24-L27) · [Solution.lean lines 44–50](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Solution.lean#L44-L50) · [Solution.lean lines 76–104](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Solution.lean#L76-L104)

For Dirichlet L-functions the arguments include a modulus greater than one and a primitive character. The solution passes those hypotheses to the Theorem E results for the $2/3$ and $5/6$ proportions. For the refined proportions it uses the combined D–E results and the same constant conversion. [Solution.lean lines 106–119](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Solution.lean#L106-L119) · [Solution.lean lines 121–140](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Solution.lean#L121-L140)

I read these proof terms and the challenge’s counting definitions. I did not build the Lean project or follow the imported analytic proofs. [Challenge.lean lines 50–80](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Challenge.lean#L50-L80) · [Challenge.lean lines 87–108](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Challenge.lean#L87-L108)
