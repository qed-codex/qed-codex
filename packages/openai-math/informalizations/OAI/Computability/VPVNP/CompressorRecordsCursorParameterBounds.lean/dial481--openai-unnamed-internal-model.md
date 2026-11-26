---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsCursorParameterBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsCursorParameterBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsCursorParameterBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Integer bounds for producing the cursor parameter frame

A single length threshold permits every split of the virtual address into
base and lane bits. The same live RAM word holds the eight public inputs,
the intermediates of the width calculation, and the exclusive ends of the
parameter frame, scheduler row and six incidence columns.


### `inputValues`

 Natural values of the eight public words of the parameter initializer. 

### `widthOperands`

 The successive integer values of the straight-line width computation. 

### `Capacity`

 Simultaneous bounds at one length, with the actual frame and directory offsets. 

### `Capacity.shiftResults_lt`

 Each shift in the parameter suffix yields its full integer power of two. 

### `eventually_capacity`

 For fixed address and degree exponents and polynomially bounded frame and
directory locations, one threshold works for every admissible lane exponent. 

### `publicInputs`

 The public parameter vector for the native initializer, in live-width words. 

### `eventually_scheduler_prefix`

 The two native bursts install the scheduler row from encoded public inputs
at every sufficiently large length. The threshold is independent of the lane
split, the entry state and the initial contents of memory. 
