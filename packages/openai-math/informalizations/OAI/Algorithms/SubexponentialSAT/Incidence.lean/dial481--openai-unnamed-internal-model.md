---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Incidence.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Incidence.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Incidence.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Finite factor incidence bounds

Scopes are finite sets: a coordinate occurs at most once in any single factor,
while distinct factors may have equal scopes.  The results below count actual
incidences, bound the neighbors sharing a factor, and account for packing
Boolean variables into chunks followed by one unary validity factor per chunk.


### `incident`

 The factors whose scope contains a given coordinate. 

### `degree`

 Number of distinct factors containing a coordinate. 

### `sum_degrees`

 Counting incidences by coordinates or by factors gives the same result. 

### `card_factors_le`

 Nonempty scopes and maximum coordinate degree imply `m ≤ ΔD`. 

### `dependencyNeighbors`

 Other coordinates sharing at least one factor with `v`. 

### `card_dependencyNeighbors_le_degree_mul`

 Each incident factor contributes at most `k-1` other coordinates. 

### `card_dependencyNeighbors_le`

 Arity at most `k` and degree at most `Δ` imply at most `Δ(k-1)` neighbors. 

### `chunkFiber`

 The original variables assigned to one chunk. 

### `packedScope`

 A packed factor reads each distinct chunk touched by its original scope. 

### `card_packedScope_le`

 Packing cannot increase the arity of a factor. 

### `degree_packedScope_le`

 At most `ell` variables of degree at most `B` give chunk degree at most `ell B`. 

### `withUnaryScope`

 Add exactly one unary factor for every coordinate. 

### `degree_withUnaryScope`

 The unary factors increase every coordinate degree by exactly one. 

### `degree_packedScope_withUnary_le`

 Chunk packing plus unary validity factors gives `Δ = 1 + ell B`. 

### `bounded_card_factors_le`

 The factor-count consequence of the common bounded-pattern interface. 

### `bounded_card_dependencyNeighbors_le`

 The dependency-neighbor consequence of the common bounded-pattern interface. 

### `packedUnaryPattern`

 Pack a pattern and add a distinct unary factor for each chunk. 

### `packedUnaryPattern_bounded`

 The full bounded-pattern interface survives chunking and unary validity factors. 
