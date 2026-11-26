---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutScaledMatrices.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutScaledMatrices.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutScaledMatrices.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Cleared integer matrices and exact ring-valued source rows

The rational spectral argument will supply integer numerators `N` and a
power-of-two denominator `d`. Over the target coefficient ring only the
unit representing `d` is inverted. Exact integer equations `d I - N`
therefore imply the fixed-vector equations needed by the original
multicolor row construction, without a map from `ℚ` to the target ring.


### `sourceRow_annihilates`

 This is the actual multicolor path from the immutable library, with
cleared integer source constraints and a unit denominator. 
