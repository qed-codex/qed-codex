---
{
  "module": "OAI/Computability/VPVNP/RAMTapeInputParametersFromSize.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeInputParametersFromSize.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeInputParametersFromSize.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Computing the live bucket from the unary input length

The fixed rational exponent has numerator `p` and positive denominator `q`.
The potentially large integer `n^p` stays in a padded binary word. Only its
binary logarithm and the final bucket size are expanded as unary tallies.


### `Port`

 Stack labels for converting unary size to a padded word, exponentiating, taking its
logarithm, and producing the unary bucket. 

### `store`

 Initialize the named size, base, power accumulator, logarithm, and bucket stacks with empty
arithmetic scratch. 

### `unaryPort`

 Connect unary-to-word conversion to the size, pending marks, base, initial unit, and
temporary stack of bucket preparation. 

### `powerPort`

 Connect repeated multiplication to the base, accumulator, factor, product, shifted factor,
sum, and temporary stack. 

### `logPort`

 Feed the power accumulator to the word ceiling-log scan and collect its marks on the
logarithm stack. 

### `bucketPort`

 Feed logarithm marks into the block-doubling routine and collect the resulting unary
bucket. 

### `routine`

 One finite control per fixed rational parameter, independent of input length. 

### `power_fits`

 The allocated width suffices even when the rational numerator is large. 

### `bucket_le`

 With exponent at most one, rounding to a binary power costs at most a
factor of two in the live bucket size. 

### `clockCoefficient`

 The clock's coefficient depends on the fixed rational. Its degree in
the input length is two for all numerators and denominators. 
