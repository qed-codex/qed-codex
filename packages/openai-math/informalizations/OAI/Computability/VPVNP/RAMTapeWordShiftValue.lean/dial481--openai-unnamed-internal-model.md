---
{
  "module": "OAI/Computability/VPVNP/RAMTapeWordShiftValue.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeWordShiftValue.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeWordShiftValue.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Logical shifts on fixed-width bit tapes

A right shift drops the low bits and fills the high end with zeros. For a
left shift the tape is reversed before and after the same operation. The
number of zeros is capped at the width, so an overshift clears the tape.


### `result`

 Drop and fill in the orientation determined by the shift direction. 

### `result_wordBits`

 The bit-string shift computes the RAM shift for every width and amount. 
