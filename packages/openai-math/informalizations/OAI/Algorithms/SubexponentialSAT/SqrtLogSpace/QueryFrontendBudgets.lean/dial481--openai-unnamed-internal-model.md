---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryFrontendBudgets.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryFrontendBudgets.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryFrontendBudgets.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Fixed polynomial bounds from the actual six frontend source words. 

### `query_capacity_of_sources`

 Physical query words, including arbitrary padding and the actual raw trial
rows, bound the capacity used by the native frontend. This is the same six
port calculation as the original query-width lemma, without its final-resource
constructor import. 

### `query_capacity_of_words`

 Uniform physical word bounds imply the six source bounds. 

### `query_frontend_sources_polynomial`

 The complete native frontend has a fixed polynomial in the actual query
word cap and ambient size. Numeric correctness alone is not used to bound
padding, raw rows, or any other retained word. 

### `query_frontend_physical_polynomial`

 The all-word version remains available to source-space callers. 

### `query_frontend_cubic_sources_polynomial`

 The concrete cubic source cap supplied by the staged hash query remains a
fixed polynomial through the complete physical frontend. The constants precede
all actual queries, marks, source padding and caller states. 
