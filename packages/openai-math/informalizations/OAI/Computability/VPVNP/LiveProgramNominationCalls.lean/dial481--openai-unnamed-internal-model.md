---
{
  "module": "OAI/Computability/VPVNP/LiveProgramNominationCalls.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramNominationCalls.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramNominationCalls.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Actual nomination calls in the linked first-half group 

### `width`

 Width in bits of each nominated grammar-production count, twice the site-address width. 

### `labels`

 Number of grammar-production positions visited by the nomination stage. 

### `base`

 RAM word addressing the first counter to which a nominated production count is written. 

### `limit`

 Grammar-label count encoded as the terminating cursor value in the group’s word width. 

### `fuel`

 Instruction fuel available to a nomination call after outer dispatch. 

### `P`

 Nomination-stage source program with the linked table’s actual public operands. 

### `active`

 A forward component and its unique successful decoding, with the actual
common outer clock after deducting dispatch. 

### `closing`

 Three-tick closing nomination report with no returned state. 
