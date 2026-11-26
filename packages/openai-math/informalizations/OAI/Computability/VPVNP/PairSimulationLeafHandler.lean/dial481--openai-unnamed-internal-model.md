---
{
  "module": "OAI/Computability/VPVNP/PairSimulationLeafHandler.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafHandler.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafHandler.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The cursor-leaf handler inside the descriptor traversal

The deterministic prefix decodes the genuine site address, reads the shadow
header, runs the local routing tests, and initializes the virtual bit stacks
at cursor zero. The remaining native instructions implement the auxiliary
machine on those supplied bits. The handler returns the entire unused
choice suffix, including when the next descriptor needs no choices.


### `Input`

 Data and effects of the deterministic leaf prefix on the supplied private
argument buffer. 

### `Input.pos`

 The cursor coordinate and site decoded from the leaf's physical node address. 

### `Input.buffers`

 The four half-wire buffers supplied by the parent to this cursor visit. 

### `Input.trace`

 The RAM events of the deterministic prefix before the transit return or auxiliary
  interpreter call. 

### `Input.prepared`

 The private scratch after routing and any stack initialization needed at cursor zero. 

### `Routed`

 The local routing check accepts the decoded site position and the bits read from its four
buffers. 

### `parser`

 A linked leaf visit, using the exact push footprint also for cells of
stacks later popped back to their original size. 

### `Preparation`

 Native prefix specification, ending at either the verified stack
interpreter's first row or the caller's continuation for a transit site. 

### `parser_exactOn`

 Exactness on the actual node and typed buffer domain, with arbitrary
independent input bits, arbitrary used scratch, and arbitrary stream suffix. 
