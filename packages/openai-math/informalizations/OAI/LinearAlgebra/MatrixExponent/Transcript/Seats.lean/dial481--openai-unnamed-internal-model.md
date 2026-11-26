---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Transcript/Seats.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Transcript/Seats.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Transcript/Seats.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Canonical dyadic allocation

A slot contains a processor number or a sentinel larger than every
processor number. Ordering the slots of each capacity makes the assignment
unique. Otherwise the contraction could count a transcript several times.


### `bucket`

 All processors charged in the dyadic interval ending at `2^j`. 

### `OrderedSeats`

 Every listed processor occurs once, in the initial sorted segment.
The last element of `Fin (P+1)` denotes an unused slot. 


# Realizing a weighted sum of products

Each factor receives its own list of argument positions from a common
tape. Positions may be repeated or unused. Summation is over all private
bits, with multiplicity, in the ground field.


 # A fixed weighted transcript on named bits 

### `weightedSum`

 A value for each possible assignment, obtained by summing over all
hidden bits. Each local factor addresses the public or the hidden tape. 

### `WideWeight`

 The cost here counts all ports, including both ends of every wire. 
