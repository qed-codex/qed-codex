---
{
  "module": "OAI/Computability/VPVNP/LiveNominations.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveNominations.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveNominations.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native binary nominations in a first-half live group

Section 14.1 guesses exactly `2r` little-endian bits per production label.
This fixed RAM call takes the bit count and destination base as public words.
Its persistent state indexes the component. It writes one word and returns
the next component index. The same control works for any nomination width
that fits a RAM word.


### `flow`

 Registers 0, 1 and 2 accumulate the value, bit weight and iteration count. 

### `data`

 The nomination worker's public bit count and base address for the per-label output words. 

### `program`

 The instantiated burst program that guesses a label's bits, stores the nominated word, and
returns the next label cursor. 

### `component_native`

 The native microcall has exactly one write. Its binary choices are precisely
the bits of the nominated component, even when it has leading zeros. 

### `component_only`

 Every successful call consumes exactly one fixed-width component and has
its specified memory effect, for any amount of interpreter fuel. 
