---
{
  "module": "OAI/Algorithms/SubexponentialSAT/PackedSAT.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/PackedSAT.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/PackedSAT.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Concrete packed CNF systems and the counting pipeline

This module records the actual variable partition and bounded factor pattern.
The final counting composition makes no running-time claim.


### `variableScope`

 The original variable scope of an actual CNF clause. 

### `degree_variableScope`

 Clause-subtype indexing does not change the number of occurrences. 

### `card_chunkFiber`

 Each chunk fiber contains exactly its declared number of Boolean bits. 

### `degree_factorScope`

 `FactorReduction` puts unary indices on the left of the sum; the generic
incidence library puts them on the right. This proves the bound for the actual
constructed system without silently identifying those two index types. 

### `packedSystem`

 Pack the original `Fin n` coordinates by quotient and remainder. 

### `fixedConstruction`

 The finite layout construction is selected before the input size and CNF. 

### `smallThreshold`

 Include dimension zero in the fixed finite fallback range. 

### `packedLayout`

 The supplied pattern is proved bounded, and the previously fixed universal
construction supplies its actual layout. No layout property is postulated. 

### `largeCount`

 The large-input branch is the defined separated-moment/CRT count, using
the actual prime-power ring and its natural-number decoder. 

### `smallCount`

 Explicit finite enumeration, used only below the fixed dimension cutoff. 

### `boundedCount`

 A bounded-occurrence CNF pipeline. Empty clauses return zero immediately;
the fixed finite dimension range is enumerated; all remaining inputs use the
actual constructed layout, separated jets, CRT, and prime-power decoder. 

### `exists_fixed_counting_pipeline`

 One set of finite construction constants works for every input size and
every CNF satisfying the fixed width and occurrence bounds. This is a
mathematical correctness assertion, not a machine-running-time assertion. 

### `occurrenceBound`

 The occurrence bound is chosen from the width before the input varies. 

### `sparseLeaves`

 The actual deterministic sparsifier's output, carrying its proved bounds.
Attaching these proofs does not alter any leaf formula or duplicate a leaf. 

### `sparseScan`

 Short-circuit OR of the genuinely computed leaf decisions. Overlapping
leaves are intentionally never summed as counts of the original formula. 

### `sparseScan_calls_le`

 A bound on calls to the leaf test; this is not a bit-runtime bound. 

### `fixedDecision`

 All parameters and the universal layout construction are fixed from
`p,k,ell` before the input's variable count and clauses are supplied. 

### `fixedDecision_correct`

 Mathematical correctness of the specified sparsify/pack/layout/count/OR
pipeline. No time bound or machine implementation is asserted. 
