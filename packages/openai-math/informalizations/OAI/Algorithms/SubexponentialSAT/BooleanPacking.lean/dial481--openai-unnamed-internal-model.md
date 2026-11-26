---
{
  "module": "OAI/Algorithms/SubexponentialSAT/BooleanPacking.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/BooleanPacking.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/BooleanPacking.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Boolean chunks and valid finite-field labels

This file implements the encoding in Section 3 of the candidate exposition.
The encoding is an actual recursively defined equivalence, not just an equality
of cardinalities. Primality is unnecessary for this combinatorial part.


### `capacity_of_le_log`

 The manuscript's logarithmic chunk-size choice supplies enough labels. 

### `capacity_of_le_log2`

 The equivalent `Nat.log2` formulation of the chunk-size bound. 

### `Chunk`

 A chunk of `b` Boolean coordinates. Empty chunks are allowed by the API. 

### `splitChunk`

 Splitting a nonempty chunk into its first bit and remaining bits. 

### `chunkEquiv`

 A computable encoding of a Boolean chunk by exactly `2^b` labels. 

### `ValidLabel`

 The allowed labels for a `b`-bit chunk inside `Fin p`. 

### `finValidLabelEquiv`

 Including the initial segment of length `2^b` into a larger label space. 

### `validLabelEquiv`

 Encoding and decoding a chunk using precisely the valid labels. 

### `chunkEmbedding`

 The chunk encoding into the complete label space, including invalid labels. 

### `decode`

 Decoding is defined on valid labels. 

### `PackedAssignment`

 All chunk-label assignments accepted by the unary validity tests. 

### `packingEquiv`

 Coordinatewise chunk encoding, with validity built into the codomain. 

### `BitIndex`

 An index for each original bit, recording both its chunk and position. 

### `regroupEquiv`

 Regrouping Boolean coordinates requires no assignments to be discarded. 

### `flatPackingEquiv`

 Encoding a flat Boolean assignment into accepted chunk labels. 

### `assignmentPackingEquiv`

 A concrete partition of the original variable indices transports packing
to the original assignment type. 

### `satisfyingEquiv`

 The satisfying assignments for any predicate correspond under encoding. 

### `count_preserved`

 Exact finite model-count preservation, not just satisfiability preservation. 

### `assignment_count_preserved`

 The exact model-count theorem also applies to any partition of original
Boolean variable indices into chunks. 

### `finEquiv_val`

 The finite label equivalence preserves the usual representatives in `ZMod`. 

### `ValidZModLabel`

 Valid representatives inside `ZMod p`. For prime `p`, these are field labels. 

### `validZModEquiv`

 The same explicit encoding in the residue ring, hence in the prime field. 

### `chunkZModEmbedding`

 Encoding a Boolean chunk as a residue-ring element. 
