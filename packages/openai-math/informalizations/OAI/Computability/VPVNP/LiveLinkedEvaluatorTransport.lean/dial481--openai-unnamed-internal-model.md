---
{
  "module": "OAI/Computability/VPVNP/LiveLinkedEvaluatorTransport.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveLinkedEvaluatorTransport.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveLinkedEvaluatorTransport.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Preservation of the outgoing physical cut during incoming preparation

The last-group flag, the outgoing header configuration field, and the outgoing
configuration bank suffice to reuse the same output data after initialization.
The incoming gather leaves these cells unchanged by disjoint allocation.


### `OutputFrame`

 The two memories agree on the last-group flag, all outgoing configuration bits, and every
word of the proposed output state bank. 

### `transport`

 Reuse an outgoing cut or endpoint witness in a new memory that agrees on the output frame. 

### `empty_initial_image`

 An empty evaluator starts in its canonical accepting state, and the
first router skips all input-tape preparation. 
