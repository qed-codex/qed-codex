---
{
  "module": "OAI/Computability/VPVNP/PairShrinkResidentMemory.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkResidentMemory.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkResidentMemory.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Child and hidden operands across the resident map loop

Every selected map reads its input packets below the histogram and its
shared hidden fields above it. Its writes affect the histogram, its own
operand staging and its grouped-map workspace. The two input regions thus
agree with the memory at the start of the loop after every successful map.


### `Preserved`

 The two scratch memories agree below the histogram base and from the hidden base up to the
staging base. 

### `Invariant`

 Loop inputs include the live register words supplied by the locator and
the resident operand cells carried across previous calls. 

### `histogram_before_hidden`

 The histogram block of the terminal allocation precedes the first
shared shrinking word. 

### `resident_exterior`

 Every word preceding operand staging and outside the actual histogram
survives a successful resident gather and grouped-map execution. 

### `resident_preserved`

 Apply the exterior frame returned by the installed gather and grouped
matrix to both resident input regions. Each valid call preserves every
other resident's child and shared words, regardless of its own motif or
party. 

### `Job.childWords_preserved`

 The lower arena still holds every independently chosen old half after a
previous map has updated its own selector, labels and histogram. 

### `Job.packets_preserved`

 All child and parent packet premises used by the actual party gather
survive in the common input region. 

### `Job.absorbed_preserved`

 Hidden fields belonging to the current motif survive calls for any
earlier resident, including a different party at the same packed site. 

### `Job.resident_preserved`

 The private-memory conclusion of the scheduled row interpreter maintains
the resident loop's invariant for the actual selected map workspace. 

### `Job.descriptor_address`

 The job header places the map descriptor sixteen words after its
private pointer directory. This recovers the pointer in the exterior frame
from the actual level fields and the live register bank. 

### `Job.keepsInputs`

 Maintain the full loop invariant using the frozen live registers and
the exterior memory clause of a successful selected resident map. 
