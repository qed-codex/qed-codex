---
{
  "module": "OAI/Computability/VPVNP/PairSimulationReadDecode.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationReadDecode.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationReadDecode.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reading and decoding one selector inside a vertex call

The field loop exits directly at the selector table's first instruction.
Both fragments use the same accumulator for the raw tag and the same
temporary. The ordinal can replace the accumulator or be retained in a
separate register. Unused codes go to the rejecting exit.


### `selectorFlow`

 The code table for one selector uses the field reader's result and
temporary registers. 

### `Runs`

 The complete in-call result, including the raw tag when the output is
allocated separately. The cursor points at the low end of the field. 

### `Runs.rejects`

 A missing selector rejects even if the budget expires before the lookup. 

### `native`

 From the field loop entry, read the actual private bits and compare the
result against the public code table. A field in the padded tail needs no
additional initialized cells. The two bounds are instruction dispatches. 

### `tag_fits`

 The selector read for copy i starts above the payload. Its two absolute
endpoints fit whenever the incident wire's exclusive end fits. 

### `native_tag`

 Decode the exact selector used by the motif evaluator on an incident
wire. The program and its public code ports are fixed across copy indices. 
