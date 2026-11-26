---
{
  "module": "OAI/Computability/VPVNP/PrimedCounterPreorder.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterPreorder.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterPreorder.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Preorder choices for the coefficient counter

A terminal choice names its input position. The terminal bit comes from that
position in the assembled word. A binary choice gives the ordered child states
and their split. Its legal range depends on the pending subtree's degree.


### `Token`

 Branch data at one pending node. The stack determines the required constructor. 

### `preorder`

 Serialize an ordered parse by visiting the parent before either child. 

### `Agrees`

 Every terminal of the parse reads the bit in its specified position. 

### `readTree`

 Decode one tree and return the unconsumed choices. 

### `positions`

 Leaf locations encountered by the mark array, in visitation order. 

### `checkedTree`

 Complete decoder with the distinct-position check used by the counter.
The computation returns the unique decoded parse and rejects trailing tokens. 

### `choiceEquiv`

 Accepting token lists retain every ordered parse and its unique matching
leaf bijection. The two domain sizes agree since the parse has exactly one
leaf per bit of the input. 
