---
{
  "module": "OAI/Computability/VPVNP/LiveAuxiliaryHeaderSweep.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveAuxiliaryHeaderSweep.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveAuxiliaryHeaderSweep.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Copying the seven populated auxiliary header fields

The persistent cursor ranges over a packed interval even though the virtual
header reserves space for both exterior fields at full capacity. The actual
machine reads the seven descriptors from external memory and writes the selected
word into the separate auxiliary region.


### `records`

 Descriptor ends are packed cursor positions; targets use sparse virtual offsets. 

### `sourceAddress`

 The original, contiguous array address of each word in the packed iteration. 

### `Separated`

 Working areas and the dispatcher table are disjoint from every destination
word written by the sparse copy. Only the addresses actually read are required. 

### `Prepared`

 State of the read-only arrays required for the copy. The three length words
and all populated data bits match the auxiliary machine's prescribed header. 

### `sweep_native`

 The compiled fixed dispatcher writes precisely the auxiliary header memory.
The count of calls is the number of populated words. No call visits a reserved
exterior padding slot. 
