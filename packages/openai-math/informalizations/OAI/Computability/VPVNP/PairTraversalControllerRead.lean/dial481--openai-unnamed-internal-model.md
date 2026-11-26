---
{
  "module": "OAI/Computability/VPVNP/PairTraversalControllerRead.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalControllerRead.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalControllerRead.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Readback of the traversal controller's loaded register bank

The register formulas read the level headers with the packed persistent
ordinal. Their two branchless count selections use self-division and
subtraction in the word ring. This also accounts for the initial-only
schedule and for the final controller sentinel.


### `Readback`

 The meanings of the eighteen loaded registers. The fiber worker executes
at a positive layer index. Its four producer fields are loaded also at index zero. 

### `readback`

 Reading the operand bank from the terminal and level headers gives every
dispatch operand and worker parameter, including the next-state words. 
