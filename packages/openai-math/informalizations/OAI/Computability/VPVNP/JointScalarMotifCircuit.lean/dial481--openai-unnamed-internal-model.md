---
{
  "module": "OAI/Computability/VPVNP/JointScalarMotifCircuit.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/JointScalarMotifCircuit.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/JointScalarMotifCircuit.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A signed coefficient circuit for the fixed motif rows

The row selector and the motif exponent wires may be placed anywhere in the
joint query. The sparse tables and their integer coefficients are fixed for
the motif. The circuit compares one unsigned witness against the selected
positive or negative part. Repeated table keys are combined using the same
integer lookup as the scalar reader.


### `Table`

 Sparse representation of one motif equation as exponent vectors paired with integer
coefficients. 

### `part`

 Natural magnitude of the selected sign of an integer, equal to zero when that sign
contributes nothing. 

### `below`

 Compare an unsigned word to a static threshold, from the high bit down.
Every level uses just one copy of the lower-bit comparison. 

### `height`

 The largest magnitude in the fixed motif table after equal keys are combined. 

### `witnessBits`

 Width of an unsigned witness whose initial segment can count either sign of every
coefficient in the motif tables. 

### `part_fits`

 The fixed witness width covers both polarities of every sparse lookup,
including a key absent from the table. 

### `expr`

 A true selector enables one sparse row. Non-motif coordinates are checked
by the enclosing joint-query circuit. 

### `eval_unselected`

 Addresses outside the motif range produce zero for every witness. 

### `sizeBound`

 Number of expression nodes, uniformly in the table entries' magnitudes.
`R` bounds a row selector and `L` bounds the length of a sparse row. 

### `frame`

 Gate compilation of the predicate, using the joint verifier's network. 

### `count_selected`

 Summing over the physical little-endian witness bank yields precisely the
selected part. This includes zero coefficients and a threshold equal to the
full word capacity. 
