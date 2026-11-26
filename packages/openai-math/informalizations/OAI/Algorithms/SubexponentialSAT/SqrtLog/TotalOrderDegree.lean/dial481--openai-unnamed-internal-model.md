---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/TotalOrderDegree.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/TotalOrderDegree.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/TotalOrderDegree.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Additive precision degree for a shared total-order truncation. 

### `DegreeBound`

 The U^j coefficient has degree at most a+b*j in the input variables. 

### `output_totalDegree_le`

 Only the shared total U-order contributes to the precision degree. 

### `output_totalDegree_prime_bound`

 Uniform e_s degree p-1 and H degree p yield the desired additive bound. 

### `output_totalDegree_hash_bound`

 After substituting degree-k hashes, both contributions scale by k. 
