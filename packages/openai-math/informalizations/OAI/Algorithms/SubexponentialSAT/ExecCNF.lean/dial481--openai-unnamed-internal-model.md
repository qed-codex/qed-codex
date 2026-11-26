---
{
  "module": "OAI/Algorithms/SubexponentialSAT/ExecCNF.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ExecCNF.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ExecCNF.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Executable list operations for CNF formulas

These definitions use explicit finite lists and decidable literal comparisons.
The structural bounds count list elements or comparison invocations; they make
no assumption that an arbitrary `DecidableEq` comparison has unit bit cost.


### `contains`

 A left-to-right linear literal-membership scan. 

### `subset`

 Every literal of the first list is searched for in the second. 

### `dedupLiterals`

 Keep the last occurrence of each literal, preserving that order. 

### `dedupClauses`

 Remove duplicate clauses using set equality, including permutations. 

### `tautology`

 Test whether a clause contains a literal together with its designated opposite. 

### `absorb`

 Strict-superset deletion; semantic duplicate clauses are removed first. 

### `cleanLiterals`

 Literal deduplication is separate from clause deduplication. 

### `eraseClauses`

 Remove every clause equal as a set to a selected clause. 

### `clauses`

 Raw selected clauses formed by attaching the common core. 

### `containsComparisons`

 The number of literal equality tests executed by `contains`. 

### `subsetComparisons`

 Literal equality tests in the short-circuit subset scan. 

### `mass`

 Executable total literal count after removing both kinds of duplicates.
This is a list computation, not a call to the finite-set specification. 
