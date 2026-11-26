---
{
  "module": "OAI/Computability/VPVNP/LiveEvaluatorNativeGroup.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorNativeGroup.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorNativeGroup.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Path counts of the literal scheduled tail-group program

A complete native RAM segment includes the preparing call, each cell call
on both tapes, and the final acceptance of the cursor. Its accepting paths
on the two decoded cut configurations have exactly the local multiplicity
used in the live chain contraction.


### `nativeGroupEquiv`

 Every successful native RAM path has one semantic branch choice and
conversely. Deterministic calls use the empty choice stream. 

### `tailCount_eq_native`

 For any two successfully decoded boundaries of a tail group, its factor
in the contraction is the number of accepted segments of the compiled table. 
