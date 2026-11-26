---
{
  "module": "OAI/Computability/VPVNP/PrimedCounterFold.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterFold.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterFold.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# One logical transition per scheduled parser call

The root initialization overwrites the pending stack. Each of the preceding
calls erases one mark. Comparison looks up the grammar label corresponding
to its dense histogram address. All administrative calls consume empty tapes.


### `PostItem`

 One call after input assembly, either a parser operation at a site or a comparison of a
dense production count. 

### `slot`

 Absolute cursor of a post-assembly item in the complete pair schedule. 

### `rowItems`

 Calls at a given site in execution order, clearing marks, installing its root and then
visiting its nodes. 

### `items`

 Chronological list of every site's parser calls followed by all production-count
comparisons. 

### `call`

 The current absolute cursor selects a complete local choice tape.
Clear, initialize and compare reject a nonempty tape. 
