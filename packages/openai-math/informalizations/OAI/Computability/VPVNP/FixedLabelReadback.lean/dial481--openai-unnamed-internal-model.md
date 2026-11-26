---
{
  "module": "OAI/Computability/VPVNP/FixedLabelReadback.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/FixedLabelReadback.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/FixedLabelReadback.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reading a scalar from the joint integer label system

Equation addresses first enumerate input words by their binary digits, then
the fixed motif rows. The exponent vector is read in the arithmetic production
order used by the primed parser. A permutation encoded in polynomially many
advice bits reconciles this order with the finite coordinates of the joint
system. For a motif row it suffices to scan the fixed sparse coefficient table.


### `labelTotal`

 Number of formal labels, including all grammar productions and the compressor labels. 

### `productionCount`

 Number of terminal and binary production labels for a grammar with n input positions, n
degree indices and n^(c+5) nonterminal states. 

### `rowIndex`

 The row address is an input word or a fixed motif equation. 

### `labelOrder`

 The production block uses the dense triangular split index and the three
row-major state indices of the primed parser. The motif block follows it. 

### `orderBits`

 Bits occupied by the table of label ordinals, with a fixed-width word for each grammar or
compressor label. 

### `orderAdvice`

 The advice contains one fixed-width formal coordinate per dense label. 

### `coeff_of_rename_blocks`

 A renaming by a coordinate block preserves the coefficient if the
complementary block has only zero exponents. 

### `fixedTable`

 A fixed sparse table gives the motif coefficient by exponent comparison.
The size of this table depends only on the chosen motif data. 

### `tableLookup`

 Recover the integer coefficient of an exponent vector by summing all matching sparse table
rows. 

### `readDense`

 Combine the two counted predicates and the fixed motif table. The `parse`
argument receives the input word and its exponent vector in dense production
order. The clocked path count is requested only for the constant coefficient. 

### `readDense_correct`

 At every equation and monomial, the block reader returns the exact signed
integer coefficient. The two scalar callbacks can be replaced independently
by any implementations returning the parse and canonical path counts. 

### `getCoeff`

 The scalar accessor on the `Fin` equation addresses and plain exponent
arrays used by the indexed Macaulay matrix. 

### `readAdvice`

 Decode an address by binary arithmetic and fetch each exponent using the
fixed-width order advice. Unused motif coefficients are read as zero by the
sparse table. The entire reader apart from its supplied tables and callbacks
is uniform in the four dimensions. 

### `readAdvice_eq_getCoeff`

 The fixed motif table and the polynomial-size index advice suffice to
implement the indexed joint coefficient accessor. 
