---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/NativeLeafSemantics.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/NativeLeafSemantics.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/NativeLeafSemantics.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The leaf's serialized raw clauses and the selector's indexed clauses
have exactly the same ambient models. Repeated clauses or literals are not
assigned extra model multiplicity. 

### `indexed`

 Index the actual list of clauses without renaming any ambient variable. 

### `recordIndex`

 Literal codes for each actual serialized clause, without sorting or
removing raw occurrences. The dependent index cast changes only its proof. 

### `indexed_image`

 Indexing the original list gives its semantic clause set, including when
that list contains repeated clauses or repeated literals. 

### `rawCount_sum`

 The sum ranges over all assignments on the declared Fin n, including
coordinates unused by every clause. 

### `history_accepts`

 The exact greedily selected history accepts precisely the original raw
formula, using the good code matrices produced by native preparation. 

### `history_count`

 This is the full unmarked accepted count, not the violation mass or a
single marked query's count. 

### `native_history_count`

 Read the actual selected-history boundary supplied by the native rounds.
The last count query must still execute on this history to produce the word. 
