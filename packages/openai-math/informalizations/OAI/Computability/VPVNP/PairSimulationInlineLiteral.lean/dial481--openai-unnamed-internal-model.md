---
{
  "module": "OAI/Computability/VPVNP/PairSimulationInlineLiteral.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationInlineLiteral.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationInlineLiteral.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native synthesis of a fixed table word

A fixed instruction block loads a natural constant modulo the current word modulus.
Its only literal operands are zero and one. Every block of the same capacity takes the
same number of local steps, including at width zero and after the accumulator wraps.


### `literalInstruction`

 The first two instructions initialize the unit and accumulator registers. Each
remaining instruction either increments the accumulator or copies it to itself. 

### `literal_prefix`

 Executing the constant block uses exactly two initializations and one tick for
each reserved position. It preserves the private memory and every other register. 
