---
{
  "module": "OAI/Computability/VPVNP/FixedProgramModelData.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/FixedProgramModelData.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/FixedProgramModelData.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The shared advice and paths of the fixed diagonal program

The program distributes one advice string across the groups. It contains
the raw evaluator advice followed, after padding, by the permutation from
dense physical labels to the joint formal label order. Every midpoint
configuration starts on that very raw advice and the same truncated exponent
words. The weighted pair paths and the native single-group counts must
refer to this common distribution.


### `noncomputable local instance (p : Nat.Primes) (t d : ℕ) : Fintype (Ground p t d)`

 Enumerate the finite ground field of the selected slice. 

### `noncomputable local instance (p : Nat.Primes) (t d : ℕ) : Algebra (Ground p t d) (Ambient p)`

 View the ambient field as an algebra over the ground field through the slice embedding. 

### `chainHeight`

 Height `h` for which each half of the diagonal chain has `2^h` groups. 

### `counterWidth`

 Bit width reserved for each accumulated label exponent. 

### `orderWord`

 Formal label index at a physical counter position, encoded as an advice word. 

### `distributedAdvice`

 Pack the raw evaluator advice and the physical-to-formal label permutation into the shared tape. 

### `exponentWords`

 Encode each exponent modulo the word size used by the evaluator. 

### `initial`

 Start the evaluator on its raw advice followed by the serialized exponent vector. 

### `ScalarData`

 The scalar program at this model has exactly the raw input assembled
by the midpoint stages. The range statement covers all branch histories,
so it also covers the initial configuration in the absence of an accepting path. 

### `ScalarData.raw`

 Raw binary reader advice for this finite model. 

### `ScalarData.advice`

 Shared chain advice obtained by packing the scalar reader advice and label order. 

### `ScalarData.init`

 Encode the midpoint evaluator configuration after reindexing the physical counters. 

### `PairData`

 Finite weighted paths for each pair whose sum recovers its nominated grammar multiplicity. 

### `PairData.Path`

 Path choices for this exterior, pair index and production nomination. 

### `PairData.ν`

 Compressor label exponents contributed by one pair path. 
