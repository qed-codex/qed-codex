---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Assembly/RetagStore.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Assembly/RetagStore.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Assembly/RetagStore.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Pinning the unused suffix of each payload slot 

 Circuit for gathering a packet from span metadata. 

### `cheap`

 The two vector heights are independent of the pointer width.
Padding reads existing rows repeatedly, so it never introduces new
intervals into a query. 

 Pointers from channel starts, span lengths and local bank addresses. 

### `encode`

 Metadata is (channel start, length, bank start). 

### `cheap_neg`

 After k doublings the coefficient 2^k vanishes modulo 2^k. 

 A sparse edge list determines the global peer permutation. 

 Expand compact interval metadata only at the local channel endpoints. 


# Encoding active gathers by disjoint runs

A run specifies its first position in the packed lane, length and
first bank address. No condition is needed on unused ports, whose
permutation is the identity.


### `Represents`

 Equality of commands where they are actually read. 

 # Expanding a description by contiguous intervals 

### `Runs`

 Span starts are measured from the start of the whole packed
buffer. The first bit of lane `i` in a level-`j` buffer is at
`i*2^j`. 


# Changing the station number of the exterior

At a host, all exterior bits use a common station number. Changing
this number preserves their order by block, span and bit offset.
Thus the same physical payload can be used before and after the cut.


 # Uniqueness of the order-preserving enumeration in a payload bank 

 Expand sparse peers as singleton intervals. 

 Reading physical port addresses from fixed slot-and-lane lookup tables. 
