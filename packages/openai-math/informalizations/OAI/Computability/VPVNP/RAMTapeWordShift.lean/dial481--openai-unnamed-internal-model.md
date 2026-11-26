---
{
  "module": "OAI/Computability/VPVNP/RAMTapeWordShift.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeWordShift.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeWordShift.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fixed-stack programs for variable word shifts

The decrement loop processes at most the width of the data word, including
when the shift amount represents an exponentially larger natural number.
Reversing the data before and after the loop implements a left shift. Both
variants leave a little-endian word and empty all their scratch stacks.


### `input`

 The entry port depends on the operation, so a left shift can first reverse
its input onto the data stack. 

### `output`

 Returned stack layout for a variable shift. Left shifts place the final word on the
temporary port, and right shifts place it on the output port. 

### `loop_run`

 The data prefix is dropped one bit at a time. The padding is limited by
the number of bits actually removed. 

### `shift_run`

 Both variable-shift opcodes have a width-independent control and five
stacks. The instruction bound is quadratic in the width, for every amount. 
