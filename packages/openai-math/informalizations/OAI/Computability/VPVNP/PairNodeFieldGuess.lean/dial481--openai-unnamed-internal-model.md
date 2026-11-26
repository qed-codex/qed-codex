---
{
  "module": "OAI/Computability/VPVNP/PairNodeFieldGuess.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNodeFieldGuess.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNodeFieldGuess.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native width lookup and independent child-slot guesses

The outgoing and incoming branches enter the same width-reading and bit-guess
instructions. An incoming slot first reads the inverse arc directory. The
guessed bits are written consecutively to the child's argument interval.


### `instruction`

 Registers 0--4 form the native private-field ABI. Registers 5--7 hold
physical port ID, inverse incidence base, and source width base. 

### `entry`

 Selects the width-lookup entry instruction for a slot. Incoming slots enter at instruction
zero to read the inverse incidence table, and outgoing slots enter at instruction two with
their port already known. 

### `fieldRegs`

 The first five registers of the eight-register width routine, passed to the private
bit-guessing loop after the field end address has been computed. 

### `Linked`

 Requires the six installed width-lookup instructions to use the specified register
placement and transfer control to the bit-guessing entry. 

### `headerEvents`

 Trace that determines the width of one port before any bit choices. An incoming port first
reads its arc ID from the inverse incidence table, then both directions read the width at
the resulting ID. 

### `header`

 Exact header continuation. No private field, histogram cell, or branch bit
is touched while following the two real incidence columns. 

### `guess_slot`

 The concrete slot of a child is read from the packed incidence table, then
its independently guessed payload is written at the declared private address. 

### `reject_short`

 A truncated choice stream cannot return through a field, regardless of the
machine's continuation. This also applies after an arbitrary prefix of old slots. 
