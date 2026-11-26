---
{
  "module": "OAI/Computability/VPVNP/SliceArithmeticConstantEmit.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticConstantEmit.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticConstantEmit.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Emitting a prime-field coefficient in the extension-field representation

A scalar from the prime field occupies the low limb of its power-basis
representation. The unary extension degree supplies one marker per limb.
The machine copies these markers, discards the one for the low limb, then
prepends one zero word per remaining marker before emitting the low limb.


### `Port`

 Ports for the extension degree, zero-word template, prime-field limb, output, and temporary
marker and copy stacks. 

### `frame`

 Initial or intermediate state of the constant emitter, including the current marker count
and output suffix. 

### `machine`

 Fixed instruction table for prepending a scalar with one significant limb. 

### `cost`

 Time for copying the degree, dropping the first marker, scanning the
remaining markers and storing the low limb. 

### `machine_runs`

 The scalar is written before an arbitrary output suffix, least-significant
limb first. The three input ports are preserved and both temporary ports
return empty. 
