---
{
  "module": "OAI/Computability/VPVNP/ClassSeparation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Codex (GPT-6.2 Astra)",
  "kind": "ai",
  "origin": "generated",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "license": "CC-BY-4.0"
}
---

# Transferring the VP–VNP separation to the challenge definitions

AI drafted this autoinformalization from the original source. It is open for mathematical review.

The conclusion concerns two predicates on families of polynomials over an arbitrary field $F$, with variables indexed by `Fin n × Bool`. The solution imports a separation result and the project’s definitions, then gives a short argument transferring the result to the predicates named in the challenge. [ClassSeparation.lean lines 1–4](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ClassSeparation.lean#L1-L4) · [ClassSeparation.lean lines 14–23](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ClassSeparation.lean#L14-L23)

Suppose those predicates were equal. For one family $f$, applying the supposed equality to $f$ makes its two membership propositions equal. The proof uses `Iff.of_eq` to obtain both implications. It places that equivalence between two others: `isVP_iff f` read backwards on the VP side, and `isVNP_iff f` read forwards on the VNP side. This would make membership equivalent for $f$ in the two predicates used by the imported separation result. [ClassSeparation.lean lines 18–23](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ClassSeparation.lean#L18-L23)

Finally, propositional extensionality turns each equivalence into an equality of propositions, and function extensionality turns these pointwise equalities into equality of predicates. That is exactly what the previously imported `VPVNP.vp_ne_vnp F` rules out. In the Lean text the commands occur in the opposite reading order: `apply` sets the equality as the goal before `funext f` reduces it to one family. [ClassSeparation.lean lines 14–23](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ClassSeparation.lean#L14-L23)

I read this solution and the challenge’s definitions of VP and VNP. I did not build the project or check the lower-bound argument in the imported separation theorem. [VPVNP.lean lines 29–43](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/VPVNP.lean#L29-L43)
