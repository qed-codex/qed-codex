---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryParameterBudgets.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryParameterBudgets.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryParameterBudgets.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Uniform input-polynomial numeric caps for every actually produced query.
These bounds quantify over every physical padding, while physical word-length
bounds are supplied separately by the concrete producers. 

### `eventually_scan_bounds_of_scope_resources`

 Actual raw scope resources imply the sharp scan bounds for every marked
or unmarked query, without an identity with the old selector history. 

### `eventually_small_inputs_of_scope_resources`

 The same raw structural bounds also supply the small scalar inputs;
all cutoffs are fixed before the query, mark, and candidate history. 

### `chosen_query_scalars_cutoff_of_scope_resources`

 The actual reciprocal sparsification choice satisfies the existing query
scalar estimates above one fixed cutoff. The three literal raw-scope bounds cover every attained history and trial;
no old selector provenance is required. 

### `chosen_serialized_values_cutoff_of_scope_resources`

 One fixed polynomial bounds every serialized numeric bank value of every
large query with the actual disjoint occurrence choice. Padding lengths remain
arbitrary; this is a bound on values, not on the padded words. 

### `chosen_scalar_input_cap_of_scope_resources`

 Numeric source dimensions and all produced bank entries share a fixed
polynomial in the original input length. The actual native scan identifies
incidences, so the full raw row count is included without using rank. 

### `raw_query_serialized_values_polynomial`

 A coarse polynomial bounds every serialized numeric value from literal
history and trial sizes, without guard success or a large-input cutoff. 

### `scalar_storage_polynomial`

 Simultaneous dense source rows, full multiplication and inverse caches,
raw specialized records and the complete n-entry factor table are polynomial
in the actual scalar cap. The truncation parameter is the actual precision t. 

### `finite_caps_polynomial`

 Every polynomial physical producer cap can share one retained input cap;
no transient service bound is recursively fed into the next loop iteration. 

### `chosen_guarded_input_cap_of_scope_resources`

 The actual chosen disjoint occurrence schedule bounds every pre-serialization
numeric model port by one original-input polynomial, uniformly over padding.
The narrow model bridge then supplies all concrete packing and ring dimensions. 
