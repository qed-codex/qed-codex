---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Upper/Character/ChargedSeparation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Upper/Character/ChargedSeparation.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Upper/Character/ChargedSeparation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The charged separation inequality for actual characters

The output is evaluated using full direct-sum additivity.  Exactly `5*M`
source copies are paid for, and the auxiliary dot product is retained.  In
the equal-value case the number of output blocks cancels the factor `M` in
that source cost, but never the auxiliary dot-product factor.


### `Character.charged_separation_equal`

 The block count pays the growing part of the separation cost.  The
remaining factor five is fixed, and is removed only in a later power limit. 
