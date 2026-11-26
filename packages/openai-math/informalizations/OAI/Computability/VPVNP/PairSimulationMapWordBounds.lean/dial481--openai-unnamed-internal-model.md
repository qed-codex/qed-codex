---
{
  "module": "OAI/Computability/VPVNP/PairSimulationMapWordBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapWordBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapWordBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Word capacity for the motif's private field reads

On any decoded selector sequence, all its running payload offsets are
bounded by its length times the largest width in the fixed table. This bound
also covers sequences whose totals disagree with the descriptor. Demand
padding and selector offsets likewise remain addressable on the live RAM.


### `eventually_polynomial_field_addresses`

 All fixed table words fit, and every field-read start and end below the
indicated private workspace prefix fit without modular wraparound. Each
incident payload limit may be an arbitrary word width up to the branch cap. 

### `eventually_field_addresses`

 Specialize the address bound to a packed local field workspace. 
