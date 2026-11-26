---
{
  "module": "OAI/Computability/VPVNP/CompressionParameters.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressionParameters.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressionParameters.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Rounded compression and bucket exponents

Section 9.1 of *VP and VNP differ over every field* chooses the number of
compressor blocks and the sizes of the live and virtual transcript buckets
by rounding multiples of the binary logarithm of the input length.


### `blockCount`

 Number of compressor blocks used in §12. 

### `bucketExponent`

 Binary exponent of a transcript bucket. 

### `liveBucket`

 The live group uses buckets of size `K`. 

### `virtualBucket`

 The virtual network uses buckets of size `K′`. 

### `le_blockCount_ratio_iff`

 Comparing a rounded-down rational exponent requires only an integer power comparison. 

### `bucketExponent_ratio_le_iff`

 Comparing a rounded-up rational exponent requires only an integer power comparison. 

### `blockCount_ratio_eq`

 An executable integer formula for the number of compressor blocks. 

### `bucketExponent_ratio_eq`

 An executable integer formula for the binary exponent of a transcript bucket. 

### `bucketExponent_bounds`

 Rounding a nonnegative bucket exponent upwards costs at most a factor of two. 

### `inv_two_pow_blockCount`

 Rounding the number of blocks down costs at most a factor of two in
the compression estimate. 

### `history_pow_blockCount_le`

 The growth of histories through all blocks fits the power slack fixed in §9.1. 

### `exists_compression_exponents`

 The rational exponents of §9.1 can be chosen for every fixed per-block
growth constant from Theorem 7.1. 

### `exists_compression_budgets`

 The same fixed pair of rationals gives the required history bound at
every positive input length. 

### `tendsto_blockCount`

 Every positive choice of the block exponent yields arbitrarily many blocks
at sufficiently large input lengths. 

### `laneBits_le_addressWidth`

 An address multiplier at least the rounded lane demand per binary
logarithm supplies all lane bits required by the compressor blocks. 

### `pow_five_le_processorCount`

 Choosing the multiplier of the address width at least five ensures the
processor count dominates the fifth power used in the counter budget. 
