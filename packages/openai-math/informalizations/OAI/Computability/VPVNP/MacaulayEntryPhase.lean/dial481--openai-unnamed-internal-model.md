---
{
  "module": "OAI/Computability/VPVNP/MacaulayEntryPhase.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayEntryPhase.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayEntryPhase.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Whole execution of a coefficient or powered-row arm

Every call starts with empty exponent and flag buffers, and returns with both
empty. An equation lookup is invoked only when all monomial coordinates can
be subtracted. A powered row selects a constant encoding directly. The space
budget accounts for a single live exponent buffer and a single scalar call.


### `phase`

 Run the appropriate monomial scan for an equation or powered row, then use its flag to
complete the scalar lookup. 

### `blank`

 Both of the Boolean-indexed temporary buffers contain empty bit stacks. 

### `selected`

 Place the given bits in the chosen buffer and leave the other buffer empty. 

### `transient`

 Common space for registers, immutable data, a dense residual vector and
flag, and either a scalar copy or final buffer cleanup. 

### `postTicks`

 Tick allowance after the monomial scan, including scalar selection or evaluation and
cleanup of the exponent and flag buffers. 

### `Preload`

 A common stack bound for the register words, unary arity markers, scalar constants and
auxiliary reader advice. 

### `complete_phase`

 Append a flag-selected coefficient or constant call to a native scan,
then reset both buffers. A coefficient routine may consume its exponent
buffer or leave it for the common cleanup stage. 
