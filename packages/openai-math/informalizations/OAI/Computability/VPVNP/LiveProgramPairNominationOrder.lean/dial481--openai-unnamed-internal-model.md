---
{
  "module": "OAI/Computability/VPVNP/LiveProgramPairNominationOrder.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramPairNominationOrder.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramPairNominationOrder.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # The live nomination order and the auxiliary machine's initial memory 

### `states`

 Concrete grammar state count used when interpreting the live histogram, `n^(circuitExponent
+ 5)`. 

### `FormalNom`

 Formal nomination assigning a count of width twice the site-address width to each grammar
production over the group’s state set. 

### `order`

 Lexicographic production positions in the grammar are exactly the
positions of the dense array guessed by the live nomination stage. 

### `nominationEquiv`

 Relabel the dense live nomination array by the grammar’s lexicographic production order,
preserving every count word. 

### `shadow_initial`

 Every address of the actual auxiliary RAM, including unused addresses,
has its prescribed value immediately after the linked copy stage. 
