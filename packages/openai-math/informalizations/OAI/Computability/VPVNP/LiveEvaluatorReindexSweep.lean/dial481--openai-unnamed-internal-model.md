---
{
  "module": "OAI/Computability/VPVNP/LiveEvaluatorReindexSweep.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorReindexSweep.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorReindexSweep.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native permutation of all dense exponent bits

The incoming scratch stores one binary digit per word. The decoded order
table names its formal row. Every native scatter reads exactly these two
words, computes the reversed tagged payload position, and writes one tape
symbol. Its last burst accepts, including the empty permutation.


### `Layout`

 Length parameters and disjoint intervals used by the native scan. 

### `Sources`

 Values of the incoming digit and order-advice buffers after the live
header scan and advice unpacking stages. 

### `sweep_native`

 The real native phase accepts after exactly one call per input bit, or
one no-op call if the dense vector is empty. Its final bank is the exact
two-tape initial configuration expected by the formal-coordinate evaluator. 
