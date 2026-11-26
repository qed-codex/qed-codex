---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutNumeratorBridge.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutNumeratorBridge.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutNumeratorBridge.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# From the rational spectral matrix to the integer constraint family

The integer constraints are literally `d I - N`. Their rational range has
exactly the dimension of `I - M`, and the same numerators supply the ring
row construction from `LayoutScaledMatrices`.


### `rationalDefect`

 The rational matrix obtained by casting the literal integer constraints. 

### `centered_rationalDefect_rank_relative`

 The actual cleared integer matrix inherits the centered spectral bound. 

### `family_sourceRow_annihilates`

 The explicit integer numerators now discharge the support hypothesis of
the existing ring-valued interpolation rows. 
