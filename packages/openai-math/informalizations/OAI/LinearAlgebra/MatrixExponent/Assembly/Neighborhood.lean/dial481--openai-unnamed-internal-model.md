---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Assembly/Neighborhood.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Assembly/Neighborhood.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Assembly/Neighborhood.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The exterior payload bank of a stage

Only the occupied prefix of each assigned slot stores data.
All other positions are pinned to zero. The physical width
depends on the total length allowance, up to a factor for the
number of dyadic levels.


### `Payload`

 An empty host takes one unit, so the usual dyadic capacity
bounds apply without an exception at zero. 

### `wire`

 Number each channel's bits in their original order. 


# Ordered bundles on a common host

Patterns use short neighbor indices at every occurrence. The decoding
table is independent of the global host names and the block number.
Port order inside each span is the same at its two ends. Width zero
permits unused seats, including a scalar with no arguments.



# Station tables in span order

Each side lists the spans in increasing order and the bits of each
span in increasing offset. Only the pattern and local station label
are needed to construct the table.



# Computing the matching at one host position

The neighbor list is common to all blocks of the position. Only a
short index into that list and the neighbor's colony key enter a row.


 # Packing the exterior bits of a scheme by host and occurrence 

### `serial`

 Order within one host is lexicographic by block, station, span
and offset within the span. 


# Matching reciprocal neighbor names

Sort by the unordered pair of names and return the other row with
that key. A row naming its own host stays fixed, so self-contacts
may have arbitrary multiplicity.



# Exchanging full block records across a variable host

Long names are routed only once per incident neighbor, independently
of the number of blocks carried by a record. Empty neighbor entries
name their own host. They need not be distinct.



# Closed neighborhoods of a reciprocal host graph

A walk may stay put at any step. A fixed dictionary enumerates all
walk instructions. At each center keep the first occurrence of each
destination and replace every repeated occurrence by the center.

