---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramLift.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramLift.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramLift.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Integer representative lifting of the ternary selector coefficients.
Only reduction is a ring homomorphism. The lift itself is a finite choice of
0, 1, or 2, and no ring homomorphism from `ZMod 3` into the thickened ring is
assumed. All statements use the supplied irreducible polynomial. 

### `coefficient`

 The actual coefficient value used by the hash circuit. 

### `reduction_hash`

 This is the origin equality needed by the selector: evaluate the integer
lift in the actual thickened ring, then reduce to the embedded ternary hash. 

### `reduction_sparseRow`

 Sparse-list version of the same bridge, matching the executable evaluator's
input representation and preserving empty rows and empty clauses. 
