---
{
  "module": "OAI/Computability/VPVNP/PairSimulationLeafImageWrites.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafImageWrites.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafImageWrites.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Register writes of the native cursor leaf

The destination of every writing instruction belongs to the leaf's allocated
registers. An enclosing machine may keep its virtual public operands in any
disjoint bank, including during external reads and on rejected paths.


### `destination_mem`

 Every register written by the composite leaf belongs to its physical register
embedding. This statement covers every opcode, independent of reachability. 
