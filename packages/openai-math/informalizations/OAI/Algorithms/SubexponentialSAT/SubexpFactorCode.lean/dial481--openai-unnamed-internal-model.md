---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpFactorCode.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpFactorCode.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpFactorCode.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Computing the factor records consumed by the separated program builder

The source stores finite row expressions rather than Taylor coefficients.
Every incidence is compiled and shifted once, and the resulting arrays are
captured by the generated `FactorData.taylor` function. Preprocessing counters
sum the actual expression-compilation, shift, and coefficient-lookup counters.


### `FactorSource`

 Input data before Taylor preprocessing at a chosen node. 

### `buildFactor`

 Build all incidence caches eagerly before exposing coefficient lookup. 

### `compilationBudget`

 Computable syntax-only bound for all dense expression compilation. 

### `shiftBudget`

 Computable syntax-only bound for all shifted dense rows. 

### `buildFactors`

 Traverse the factor list once, sharing every computed record and its
preprocessing counters. The output data feed `SubexpProgramBuilder` directly. 

### `buildFactor_taylor`

 The local Taylor identity required by program correctness is a theorem
of the constructor, not a certificate supplied with the input. 

### `buildFactor_taylor_of_denote`

 Scope-reindexed interface matching the local premise of
`SubexpProgramCorrectness.groupExpr_eq_rowGroup`. Only the denotation of the
input row syntax must be connected to the desired mathematical row. 
