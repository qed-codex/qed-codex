---
{
  "module": "OAI/Computability/VPVNP/EvaluatorWeightedStep.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorWeightedStep.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorWeightedStep.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The weighted matrix-step callback

After a legal next index has been chosen, the deterministic query writes its
field entry onto the multiplication input. The actual Horner bit-stack code
multiplies that entry by the running field product and clears its workspace.
Committing the ordinal leaves exactly the payload expected by the next call.


### `Port`

 The basis-index registers, field multiplication registers, limb-width tally and auxiliary
ports of a weighted matrix step. 

### `bits`

 Physical coefficient representation used by the entry-query and
multiplication routines. 

### `bank`

 Call boundary, with an optional pending ordinal and a possibly occupied
query result port. The unary width register serves the terminal residue test. 

### `callback`

 The query may use additional disjoint ports of the enclosing caller.
The selection, field multiplication and commit instructions are fixed. 

### `ticks`

 Per-step bound, with the advised coordinate query as its only
singly-exponential operation. This bound does not involve the exponent width. 

### `callback_count`

 Each distinct next ordinal is presented to the scalar query exactly once.
The branch leaves the product of the chosen entry and the previous accumulator
in the canonical representation, with a bounded index-dependent delay. 
