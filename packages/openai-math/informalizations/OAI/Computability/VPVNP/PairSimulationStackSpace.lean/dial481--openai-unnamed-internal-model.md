---
{
  "module": "OAI/Computability/VPVNP/PairSimulationStackSpace.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationStackSpace.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationStackSpace.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Space and instruction bounds for private simulation of a virtual cursor leaf

Stack ports occupy consecutive, equal-sized intervals in private memory. At a
virtual site the initial stacks contain only public operand bits, unary clocks,
and the site's incident data. One additional bit per simulated step suffices
even when a malformed candidate uses its entire clock.


### `Layout.consecutive`

 Consecutive port intervals, each with one-past-top pointer representable. 

### `eventually_port_space`

 A fixed polynomial-size scratch arena, after any polynomial-size prefix,
fits in a live RAM word. 

### `eventually_steps`

 The complete source interpreter clock of this leaf, uniformly in the
address and all input bits. It includes nomination, execution and sorting. 

### `bank_length_le`

 Initial stack lengths, including the routing fields and all public
operands, fit a single polynomial bound before the first stack instruction. 

### `eventually_bank_and_clock`

 One interval per stack suffices on every path of the actual processor,
including the closing halt and a full initial incident bank. 
