---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HighQueryRankCount.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HighQueryRankCount.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HighQueryRankCount.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The actual produced factor constructor and physical high odometer use
one source predicate and one descending rank order. Arithmetic witnesses and
interpolation nodes introduce no additional acceptance condition. 

### `query_high`

 The freshly computed physical high mask is the addressed packing high
set, including the empty high set. The ambient dimension is unchanged. 

### `native_source_hashes`

 These are the literal original clauses and row coefficients of the
actual constructor, with only the proved finite-index transport. 

### `native_rank_count`

 The actual native fixed-high answer is precisely the integer summand
used by the high-assignment accumulator; no coefficient or bit is tested. 

### `native_physical_count`

 The literal reversed zero-merge vector read by the machine gives the
same summand, including the unique rank when there are no high coordinates. 

### `native_decoded_count`

 The actual decoder's ascending ambient vector determines exactly the
same descending high-coordinate rank. Low coordinates are not counted twice. 

### `native_rank_sum`

 Summing exactly the attained rank interval gives the full ambient source
count. This is a proof-side sum; the executable loop retains a binary word. 
