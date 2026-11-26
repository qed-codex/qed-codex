---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/BatchDescent/PortRelay.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/BatchDescent/PortRelay.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/BatchDescent/PortRelay.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Exclusive prefix sums of modular addresses 

### `prefix_sum`

 Output the incoming accumulator at every position, then add the
current record modulo the address-space size. 

 # The exterior bits of each stack stay together in ordered units 

### `Strips`

 Each unit is one aligned interval of an exterior span. 

 # Exclusive address sums from short length fields 


# Relaying long headers inside bins

A short description selects the source header for each target row;
sources may be reused. Work on narrow vertical slices of the entire
bin. Lengths need not be divisible by the slice count.



# Recovering the ordered exterior units

An aligned equivalence on bits descends to an equivalence on units
without changing the within-unit index.



# Placing host descriptors at their start offsets

A shared dictionary computes lengths. Exclusive prefix sums give
destinations; scattering checks the entire proposed output including
the blank positions. Arithmetic cannot wrap at a valid destination.


### `Addresses`

 A named array of binary addresses of width `j` bits. 

### `scatter_with`

 Compute destinations from the exclusive count offsets before
scattering a possibly different collection of records. 

 # Binary addresses of consecutive port headers 

### `portOffset`

 Double the bin stride, preserving the offset and adding the port number. 


# Scattering short and long headers into bins

Short headers use a bin stride of one half-bin. Long headers use the
full stride and one row per port. The packing inequalities exclude
modular wraparound in both address calculations.



# Long port descriptors with private anchor tapes

Scatter one descriptor per port to its anchor and relay it within
the bin. The activity bits and contents of every anchor are forced,
so summing over this intermediate tape has multiplicity one.


### `hide_unique`

 Hide a witness tape that is uniquely determined on valid inputs. 
