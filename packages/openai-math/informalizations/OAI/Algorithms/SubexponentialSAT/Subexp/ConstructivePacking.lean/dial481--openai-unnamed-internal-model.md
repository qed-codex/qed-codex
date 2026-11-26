---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/ConstructivePacking.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/ConstructivePacking.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/ConstructivePacking.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Executable complete-block packing

All execution definitions use supplied finite lists, filtering, minimum scans,
indexed list access, and index lookup. No execution definition uses classical
choice or an abstract inverse. Mathematical cardinalities occur only in proofs.


### `FiniteEnumeration`

 A supplied, duplicate-free enumeration of the whole finite type. 

### `equivFin`

 Executable enumeration and inverse, implemented by `get` and `idxOf`. 

### `listSubtypeEquiv`

 A concrete list enumerating a predicate gives a computable subtype equivalence.
The predicate itself need not have a decision procedure: the list is supplied. 

### `PackingData`

 All operational packing inputs are explicit finite data. 

### `bucket`

 One scan of the vertex list extracts a type fiber in the original order. 

### `bucketEquiv`

 Explicit fiber enumeration, without `Fintype.equivFin`. 

### `minCount`

 The minimum scan uses the vertex-list length as its initial cap. 

### `selected`

 The selected portion of each bucket is the first `blockCount` coordinates. 

### `vertexAt`

 Indexed placement of a type in a block. 

### `lookup`

 Find the coordinate's position in its own bucket and check if it was selected. 

### `completeBlocks`

 The old mathematical interface, now filled by the computed placement. 

### `lookup_some_iff`

 Exact correctness specification for the executable inverse lookup. 

### `leftovers`

 The original vertex order, filtered by executable lookup failure. 

### `leftoverEquiv`

 Explicit leftover enumeration, with an `idxOf` inverse. 

### `bucketCounted`

 A filter implementation that also counts its label-equality tests. 

### `minCountCounted`

 The minimum scan with counters for label tests and minimum comparisons.
This does not charge the cost of evaluating the supplied label function. 

### `blockCountCounted`

 Exactly one vertex scan and one minimum comparison per supplied type. 

### `coverage_of_count_lower`

 The computed minimum and embedding have the same loss guarantee as the
abstract packing theorem. 

### `leftovers_toFinset`

 The computed leftover list is exactly the earlier mathematical leftover set. 
