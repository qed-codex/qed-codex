---
{
  "module": "OAI/Computability/VPVNP/FixedProgramTailContinuation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/FixedProgramTailContinuation.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/FixedProgramTailContinuation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The fixed diagonal program realizes its model's evaluator half

This identifies the physical table's continuation with the certificate's
initial-code function, using the actual model advice, row permutation and
integer counter widths. The program geometry fixes the remaining dimensions.


### `fixedTailObligation`

 Native realization used by `assembleLocalCertificate`. The model
provides the raw input, its exact ordering, and the occupied initial tape
interval. Only the numerical caps on the common table enter separately. 
