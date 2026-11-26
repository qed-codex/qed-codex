---
{
  "module": "OAI/Computability/VPVNP/PairSimulationLeafNativeCount.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafNativeCount.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafNativeCount.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native stack nominations at cursor leaves

The virtual validator first nominates a finite private stream, then checks
it. The binary instructions of this nomination program have their own
complete words. The reader below consumes those actual instruction choices.
At a leaf each accepted occurrence has exponent zero, so a bijection of
finite choices transports its contribution to the original cursor factor.


### `completeReader`

 Parse the actual stack nomination bits and return the exact consumed
word as the occurrence, keeping the unconsumed suffix for the next leaf. 

### `completeReader_suffix`

 Projecting away the occurrence recovers the stack interpreter's
actual remaining input. 

### `auxiliaryProcessor`

 The validator has direct accepting/rejecting halts. A normal fall-through
of this closed stack program rejects. 

### `auxiliaryCode`

 The closed stack program for the auxiliary validator, with rejection on ordinary
fall-through. 

### `auxiliaryEntry`

 The initial control state of the closed auxiliary stack program. 

### `auxiliaryBank`

 The auxiliary validator's initial stacks built from the cursor position, four supplied
buffers, and primed counter's public operands. 

### `auxiliary_native`

 Execution on the actual bank built from the auxiliary public operands
and four independent half-wire buffers. Every true halt goes to the
linked native continuation with its suffix and framed private memory. 

### `auxiliary_native_card`

 The instantiated, accepting native burst counts exactly the choices
of the original cursor on these supplied buffers. 

### `nominationEquiv`

 Occurrences at a leaf carry zero exponent. A finite bijection transfers
the validated stack nomination multiplicity to the initial cursor factor. 

### `nominationReader`

 At cursor zero read the actual stack program's choices. A valid transit
site uses the empty word and a failed routing test rejects before nomination. 

### `nominationReader_suffix`

 On every local input the reader returns exactly the suffix left by the
native nomination parser, the deterministic transit, or the failed guard. 
