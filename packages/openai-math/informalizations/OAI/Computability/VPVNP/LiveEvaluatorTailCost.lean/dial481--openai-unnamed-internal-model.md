---
{
  "module": "OAI/Computability/VPVNP/LiveEvaluatorTailCost.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorTailCost.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorTailCost.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Cost of the evaluator stages in the linked live program

Starting at the first-tail router, the native trace initializes the evaluator
or gathers its incoming configuration, then prepares or gathers its outgoing
configuration and runs one transition. The bounds include framed operand
loads, the dispatcher tag read, and the transfer write. Header preparation
and the earlier live-mode router are outside this interval.


### `Parameters`

 Raw prefix bit length, row width and row count are taken before choosing
the transcript capacity. The order-advice row has `clog 2 t` bits. 

### `Parameters.advice`

 The advice prefix size used to bound the number of native packing calls. 

### `Parameters.rows`

 The number of exponent rows whose label ordinals and digits are prepared for the
  evaluator. 

### `Parameters.rowWidth`

 The number of binary exponent digits per row. 

### `Parameters.radius`

 The radius on either side of the head in each finite evaluator tape window. 

### `Parameters.wordWidth`

 The number of bits packed into a native advice word. 

### `Parameters.exponentBits`

 Total number of exponent digits across all label rows. 

### `Parameters.runtimeBits`

 Length of the serialized runtime skeleton, including exponent payloads, width fields, and
delimiters. 

### `Parameters.configWords`

 Number of words needed for the control state and both full radius-bounded tape windows. 

### `Parameters.transitionCost`

 The linked cost allowance for one instruction-preparation call and the two windows'
cell-check calls. 

### `Parameters.lengthPackCalls`

 Number of cursors used to pack the length word, including its initial clear. 

### `Parameters.prefixPackCalls`

 A call bound for packing the advice prefix into rounded-up word rows, including the
empty-prefix case. 

### `Parameters.orderPackCalls`

 A call bound for packing one binary ordinal per label, including each row's initial clear
and the empty-table case. 

### `tailStages`

 The component stages that run between mode dispatch and termination. 

### `groupBound`

 The linked cost of all the tail stages following mode dispatch. 

### `rawBudget`

 The first component is the number of calls. The second is the cost
including probes but before operand loading and stage dispatch. 

### `frameReads`

 Exactly the prefix pack, prefix copy, skeleton and scatter use operand
frames among these stages, with the arities of the tables in `LiveProgram.rows`. 

### `linked`

 Apply the two native report transformations at a stage boundary.
Each report retains the memory at its call entry for the frame read values. 

### `Bounded`

 Per-stage facts furnished by the component execution theorems. 

### `tail_group_cost`

 A single symbolic RAM-cost bound for a first, interior, last, or sole
tail group. The hypothesis concerns its component traces. The conclusion
charges the framed reports and the real dispatcher/transfer reports. 
