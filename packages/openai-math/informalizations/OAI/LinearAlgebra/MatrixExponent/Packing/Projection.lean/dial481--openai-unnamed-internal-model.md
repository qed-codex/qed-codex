---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Packing/Projection.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Packing/Projection.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Packing/Projection.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Placing bundles on permutation layers

A layer is a permutation of the terminals. To complete a matching we
allow a zero demand between a slack row and a slack column. Hall's
condition follows by counting either saturated rows or saturated columns.


### `permutation_layers`

 A nonnegative integral demand matrix with row and column sums at most
`n` is dominated entrywise by a sum of `n` permutation matrices. 

### `rotor_placement`

 Place each requested unit on a layer and port carrying its ordered
pair of terminals. Different pairs cannot collide at a terminal, since
each layer routes a permutation. 

### `rotor_cost`

 Capacity in scalar bits, with `Y` terminals, unit size `u` and
budget `b = F B`. The rounding overhead costs at most one budget. 

 # Common support after relocating the ends of a contact 

 # Placing the six parties of each matched pair on the contracted host 

### `rep`

 The last two parties charge their incidences to the indicated old endpoint. 

### `party_closed`

 Each profile class is internal on its designated side. 

### `party_internal`

 Every replacement wire is internal in at least one layout. 

### `party_near`

 All six parties lie among three sites on a path of length at most three. 

 # Splitting the original unit wires into matched pairs and untouched wires 

### `contact`

 Endpoints before removing loops. A replacement edge has width
one `b`-th of an original unit. 

 # Treating a group index as an extra host coordinate 

 # Projecting simultaneous contractions onto a common host 

### `Projection`

 Separate group labels from the slots of the common host. 


# Sums of networks sharing a fringe

The budget `n` bounds the selector length in bits. Composition with
selector-dependent choices uses a dependent sum, so each term keeps its
multiplicity even when some of the resulting networks coincide.



# Tether ends through a sequence of core contractions

The set of possible source positions of a tether depends only on core
degrees, even when the full host has much larger degree. Counting
destinations also pays the ratio of block counts.


### `tracks_of_slots`

 Individual stations can move to a neighbor's slots. 


# Composing grouping steps

The width estimate is affine in the old width and the sum of frozen
charge and slack. The other bounds are multiplicative. Counting seats
(host positions times blocks) makes the slack estimate independent of
how many blocks are grouped at a step.


### `Reduction`

 A reduction with subdivision factor `b`, using `n` grouping steps,
full-degree exponent `e` and overhead `K`. The selector length is
bounded in units of the output width, even across composed reductions. 
