---
{
  "module": "OAI/Algorithms/SubexponentialSAT/ExecSunflowerSearch.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ExecSunflowerSearch.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ExecSunflowerSearch.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Explicit finite sunflower search, with counted list scans. 

### `scan`

 First successful Boolean test, together with the actual number of tests run. 

### `scanWidths`

 Scan consecutive widths, counting all candidate tests executed. 

### `FixedEnumeration`

 An explicit fixed-size generator records recursive calls and outer-list cells
visited by its append/map operations. 

### `enumerateFixed_calls_le`

 Failed branches are included: this bound is on actual recursive calls, even
when the requested size exceeds the input length and the output is empty. 

### `enumerateFixed_cells_le`

 Every map/append cell traversal is charged, independently of output size. 

### `enumerateCores`

 Enumerate all sublists of one clause, recording the recursion and map/append loops. 

### `enumerateCoreFamily`

 Enumerate clause cores for a whole input, counting the outer concatenations too. 

### `intersection`

 Literal intersection is implemented by a filter and linear membership scans. 

### `petals`

 Petals as executable literal-list differences. 

### `check`

 All conditions are checked by finite list scans. Distinctness is enforced by
counting the extensional clause deduplication, not raw repeated occurrences. 

### `Good`

 Mathematical specification of a candidate; execution uses `check`. 

### `coreCandidates`

 Cores are sublists of individual clauses; no formula powerset is generated. 

### `pairLists`

 Form the Cartesian product by explicit map/append loops. The count charges
one recursive call and each map/append list-cell visit. 

### `buildCandidates`

 Structural generation work: recursive calls and map/append cell visits.
The extensional clause-deduplication comparisons are counted separately by the
measured CNF primitives; candidate predicate tests are also separate. 

### `candidates`

 Direct fixed-cardinality subfamily generation followed by core candidates. 

### `searchAt`

 Search one width and count actual calls to the complete Boolean predicate. 

### `select`

 Widths are visited in the fixed order 2, 3, ..., k. 

### `subfamilyList`

 Restrict the extensionally deduplicated list to a specified finite family. 

### `exists_coreList`

 A finite literal subset of a clause has a concrete sublist representative. 

### `candidate_complete`

 Every set-theoretic sunflower is represented by an enumerated list candidate. 

### `FreeAt`

 The terminality criterion at a single width. 

### `petals_set`

 Executable petals match the finite-set petals used by the branching proof. 

### `RawWidthAtMost`

 Raw list-width assumption used in the enumeration bounds. 

### `candidates_length_le`

 Candidate count, without treating list generation or literal comparison as free. 

### `searchAt_count_le`

 Actual predicate-test count is at most the generated candidate-list length. 

### `select_count_le`

 Across all visited widths, count every complete Boolean candidate test. 

### `generationBudget`

 Polynomial structural-generation budget for fixed requested sunflower size. 

### `candidate_bounds`

 Every generated candidate has the bounded raw dimensions required by the
measured checker, whether or not it is a valid sunflower. 
