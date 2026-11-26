---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryTupleReadoutSemantics.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryTupleReadoutSemantics.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryTupleReadoutSemantics.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Exact readout of the emitted first-occurrence tuples. The equivalences
below preserve the numeric representative at every head. They are proof-level
reindexings of the native traversal, not stored families or evaluator services. 

### `tupleLabelEquiv`

 Actual full-key equality and source-label equality identify the same
first occurrence. The underlying bounded candidate is unchanged. 

### `labelRepresentatives`

 The attained-label grouping chooses the same assignments that the actual
first-occurrence traversal emitted; no correction restriction is added. 

### `sum_emitted`

 Multiplicity one is inherited from the proved first-occurrence
equivalence, with the actual representative assignment in every summand. 

### `emitted_readout`

 The exact native tuple value: full-head key and correction tests remain
inside each head sum, and additive readout remains outside the full product. 

### `grouped_dense_query_emitted`

 Reindex the existing finite-difference/grouping theorem by exactly the
tuples emitted by the native traversal. No coefficient identity is reproved. 

### `zero_head_readout`

 For zero levels the actual traversal emits the unique empty tuple and
the empty product contributes the unit exactly once. This needs no head map. 
