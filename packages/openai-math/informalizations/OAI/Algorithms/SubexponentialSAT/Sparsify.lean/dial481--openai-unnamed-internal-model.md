---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Sparsify.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Sparsify.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Sparsify.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Deterministic sunflower sparsification

The selector enumerates fixed-cardinality subfamilies of the input and subclauses
of input clauses.  It uses the concrete syntax ordering from `Encoding`, rather
than a semantic choice oracle.  Recursive calls decrease total literal mass.


### `coreCandidates`

 Candidate cores are subclauses of existing clauses, not arbitrary subsets of
the entire variable universe. 

### `candidates_length_le`

 The finite selector searches polynomially many candidates for fixed width
and fixed sunflower thresholds. This is an enumeration-size bound, not a claim
about unimplemented Turing-machine bit costs. 

### `pick`

 A finite deterministic search, returning a proof of the tested predicate. 

### `Choice`

 A chosen branch includes all of its independently checked local facts. 

### `leastChoice`

 Turn the first successful width search into all the branching data. 

### `select`

 Select the least available width, then the first syntactic candidate. 

### `Decomposition`

 An actual finite binary decomposition tree. Leaf terminality is established
by the failed finite search, not assumed by the caller. 

### `sideAt`

 Read a path as a total sequence of branch choices, false beyond its end. 

### `PathData`

 Concrete histories extracted from a root-to-node path. All insertion
conditions are local branch facts; no cumulative bound is included here. 

### `pathData`

 Follow an actual path in the constructed tree and retain its local
sunflower transitions for the independent charging theorem. 

### `treeFor`

 Normalize once, then carry out the actual terminating branching algorithm. 

### `sparsifyTree`

 All threshold parameters are selected from k before the input is examined. 

### `sparsify`

 The explicit finite list returned by deterministic sunflower sparsification. 
