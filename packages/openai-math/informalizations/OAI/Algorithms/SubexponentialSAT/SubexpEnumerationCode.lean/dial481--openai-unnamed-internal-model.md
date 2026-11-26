---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpEnumerationCode.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpEnumerationCode.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpEnumerationCode.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Finite-list adapter for supplied multicolor enumeration data

The input is `EnumerationData`, whose vector arrays and bijections must be
constructed separately. This module creates actual lists using `List.ofFn`
and `List.finRange`, proves their coverage and lengths, and supplies the
coordinate-support lists used by the executable separated evaluator.
No basis, complement, or enumeration is selected by classical choice here.


### `outerBases`

 Explicit outer basepoint list, in the supplied array order. 

### `innerIncrements`

 Each color's explicit increment list. No product of these lists is formed. 

### `supportLists`

 Support coordinates in increasing ambient-index order. 

### `outsideList`

 Complement coordinates, obtained by a finite filter over the ambient indices. 

### `assignments_covered`

 Coverage by the supplied basepoints and individual increment lists,
without constructing their Cartesian product as a list. 

### `compiled_beta_eq`

 The executable dot product at the one-color input is exactly the beta of
the full reconstructed assignment. Coordinate and residue lifts stay distinct. 

### `groupCode`

 Build each group expression at the basepoint plus its own color increment.
The residue-field lift and coordinate-weight lift are deliberately separate. 

### `programBlocks`

 The actual list program, built directly from the supplied vector arrays. 

### `programBlocks_eq_computedBlocks`

 Mapping the finite vector arrays produces exactly the index-based program
whose weight and finite-sum correctness were already proved. 

### `programBlocks_innerCalls`

 Every actual list block has the expected number of independently scanned
inner terms, and the total equals the derived enumeration count. 

### `programBlocks_size_le`

 The builder's expression-size estimate specialized to the exact supplied
array lengths. This bounds expression nodes, not Turing-machine steps. 

### `executeProgram_eq_separatedJet`

 The remaining program premises are local group-expression semantics and
their independently provable own-color invariance. All list enumeration and
computed-weight premises are discharged by this adapter. 
