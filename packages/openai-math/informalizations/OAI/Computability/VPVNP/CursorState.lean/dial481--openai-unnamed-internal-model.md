---
{
  "module": "OAI/Computability/VPVNP/CursorState.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CursorState.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CursorState.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The initial state of the compressor

Reindex the physical padded cursor network as the dyadic-degree state of
Section 7. The site map selects the designated address bits as lanes. The
edge map preserves the original parallel-arc index. The payload bijection
concatenates the fields reserved for the individual mask systems.


### `stateEdges`

 Padded physical arc IDs in the compressor's site-first numbering. 

### `stateWidth`

 Actual width on one outgoing slot at one source lane, as indexed by a state. 

### `cursorState`

 The Section 12 state with degree and designated lane count as indices. 

### `cursorStateIso`

 Match the tensor network of the original cursor validators with the
input network of a typed compressor execution. 

### `cursorState_positions`

 The state position count still includes every processor and every cursor. 

### `cursorState_energy`

 The energy charged to the initial state is the energy of the actual
physical fields and all of its zero-width padding. 

### `cursorState_sqrtEnergy_le`

 Initial square-root energy at the state's normalized arc mass. 
