---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Processor/PacketNet.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Processor/PacketNet.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Processor/PacketNet.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reading a compact sequence at the marked slots

The prefix counter and the indirect reader use the same address
width. Doubling the array avoids truncating the extra counter bit.


 # Relating marked positions to ordered block concatenation 

### `rank_image`

 The rank at a marked position is its index in the list of marks. 

### `matches_pack`

 Any order-preserving placement of the active cells works. Slots
between them, and compact-array positions past the last cell, are ignored. 

### `grid`

 Absolute positions in the uncompressed array. Its first `s`
bits are reserved for the fixed-length selector prefix. 

### `matches_grid`

 Mark the entire fixed prefix and the initial `f p` slots of each
reserved block. The comparison checks the prefix and packed blocks. 

### `matches_alphabet`

 A shared class uses all the bits charged by its report. A single
prefix-count check therefore verifies its entire symbol. 


# Fixed-width private packet records

The selector and its crossing bits fit in one record of constant size
for a fixed cube identity. Out-of-range selector codes and nonzero
padding bits carry zero weight.


### `address`

 Uncompressed addresses reserve the full selector prefix and a
fixed crossing capacity for every packet in order. 

 # An exact count check on fixed-width packet records 


# A trivalent network for one packet class

Prepare marks and values with bounded input dependence. The remaining
work is one batched read, histogram comparisons, and independent
constant-arity weights.


### `switched_net`

 A two-bit mode can vary with the report. The cost per member is
polynomial in the width of the count fields and independent of the cut. 

 # Private assignments for a fixed class and public report 

 # Checking a packed shared symbol in a fixed rectangular layout 
