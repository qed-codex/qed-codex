---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/BlockSearch.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/BlockSearch.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/BlockSearch.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Explicit exhaustive linear-algebra search on a finite universal block

The execution functions use lists of field elements and explicitly enumerate
vectors and scalar coefficient tuples. No decision procedure for the proposition
`LinearIndependent` or for an abstract span is executed.


### `Candidate`

 A tuple of at most `N` explicitly represented vectors. 

### `candidates`

 Enumerate dimensions, then all vector tuples of that dimension. 

### `basisTest`

 All independence, membership, and spanning checks are finite loops. 

### `subspaceCandidate`

 This witness is used only to prove that the executable enumeration succeeds. 

### `searchBasis`

 Executable search; no abstract linear-algebra predicate occurs in its code. 

### `findBasis`

 A total executable basis finder. The existence proof is erased by execution. 

### `GoodPair`

 A kernel basis together with a complementary basis, certified by scalar tests. 

### `searchPair`

 Search pairs of bounded-length tuples, still only on the universal block. 

### `decomposePair`

 The inverse coordinate map is a finite local search, not a chosen existential witness. 

### `pairEquiv`

 An executable local coordinate equivalence, with a direct linear-combination inverse. 

### `kernelCoeffsEquiv`

 Kernel coordinates, obtained from the executable local decomposition search. 

### `length_flatMap_le`

 A general finite-list enumeration bound, independent of any mathematical oracle. 

### `checkedAll`

 Instrumented full traversal: the second component counts scheduled primitive checks. 

### `checkedFind`

 Instrumented search counts the checks performed up to the first successful candidate. 
