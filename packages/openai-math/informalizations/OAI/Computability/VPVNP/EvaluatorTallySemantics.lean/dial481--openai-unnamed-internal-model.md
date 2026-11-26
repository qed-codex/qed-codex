---
{
  "module": "OAI/Computability/VPVNP/EvaluatorTallySemantics.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorTallySemantics.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorTallySemantics.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Chronological semantics of a unary evaluator scan

Each iteration may branch. The remaining clock covers the index increment
and every later iteration on each branch. The final cleanup removes the
index accumulated throughout the scan.


### `TallyBank`

 The two physical stack counters represent the current index and the
number of callbacks still to be invoked. 

### `TallyBank.of_frame`

 The usual framed bank supplies these equations for any payload bank. 

### `loop_realizes`

 Starting with index `i` and `r` remaining marks composes the successive
callback effects in increasing index order. Each callback has its own paths
and may use fewer than `B` instructions on any of them. 
