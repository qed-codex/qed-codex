---
{
  "module": "OAI/Computability/VPVNP/PrimedInputRAMHeaders.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMHeaders.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMHeaders.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Prescribed headers for the auxiliary RAM

The pair's cut lengths occupy words 0, 1 and 2. After them come the two
fixed-width group index fields, the advice field, and two equal-capacity
exterior fields. Each bit occupies one word. The nominated histogram
follows these fields, and all unused header positions are zero.


### `encodeBit`

 Represent a Boolean header or shared bit by a zero or one RAM word. 

### `cutLength`

 The left, middle or right cut length stored in the corresponding one of the first three
header words. 

### `headerMemory`

 Lay out the three cut lengths, group indices, advice, exterior bits and nominated histogram
in external memory, padding the unused cells with zero. 

### `headerMemory_hist`

 Read the supplied word for one histogram entry, or zero if it lies beyond the end. 

### `streamEquiv_symm`

 The stream obtained from the inverse path-counting equivalence consists
of exactly the bits consumed by the first pass, in physical order. 

### `assemble_stream`

 A parser can read each output bit directly from RAM following any admissible
first-pass branch sequence. The three cut lengths and the actual bit-valued
words in the initialization are fixed by the header format above. 
