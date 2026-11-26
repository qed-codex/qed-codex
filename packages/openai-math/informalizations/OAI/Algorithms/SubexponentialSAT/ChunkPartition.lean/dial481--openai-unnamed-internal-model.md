---
{
  "module": "OAI/Algorithms/SubexponentialSAT/ChunkPartition.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ChunkPartition.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ChunkPartition.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# An explicit ceiling-based partition into Boolean chunks

For positive `ell`, the number of chunks is `(n + ell - 1) / ell`.
The `i`th chunk contains the consecutive indices starting at `i * ell` and
has size `min ell (n - i * ell)`. Quotient and remainder give an actual
equivalence between the original indices and chunk/offset pairs.


### `count`

 The natural-number ceiling of `n / ell` for positive `ell`. 

### `size`

 Size of each consecutive chunk, allowing a shorter final chunk. 

### `Index`

 Chunk index together with a valid within-chunk offset. 

### `size_eq_ell_of_not_last`

 Every chunk before the last has the full prescribed size. 

### `lastIndex`

 The actual final chunk exists precisely when the input has a variable. 

### `last_size_eq_remainder`

 A divisible input has a full last chunk; otherwise the last chunk has
exactly the positive remainder. No empty trailing chunk is introduced. 

### `splitIndex`

 Split an original index into quotient and remainder. 

### `joinIndex`

 Reassemble a chunk/offset pair as an original index. 

### `indexEquiv`

 The concrete partition equivalence required by Boolean packing. 

### `sum_size`

 The chunk sizes sum to exactly the original number of variables. 
