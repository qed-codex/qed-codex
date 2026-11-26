---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/NativeLeafInput.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/NativeLeafInput.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/NativeLeafInput.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Physical leaf input facts after the actual terminal dispatcher. The
number of clauses is bounded using the disjoint selector's occurrence
estimate; no OR-cover leaf multiplicity is used. 

### `length_eq_card`

 Valid raw syntax has one record per semantic clause. 

### `empty_not_mem`

 The terminal empty-clause test agrees with the semantic set input. 

### `card_le_occurrences`

 Incidence counting for nonempty clauses. This is the source's elementary
clause bound, independent of the overlapping sparsification controller. 

### `clauses_le_physical_occurrence`

 The occurrence word on physical stack264 bounds the actual record count.
Both the selector and the input remain over the declared ambient Fin n. 

### `records_input`

 The exact serialized records consumed by startup retain the physical
body and the actual number of clauses. 

### `nonterminal_positive`

 Nonterminal startup has a positive clause count and a positive supplied
occurrence bound; the latter is an actual decoded word, possibly padded. 
