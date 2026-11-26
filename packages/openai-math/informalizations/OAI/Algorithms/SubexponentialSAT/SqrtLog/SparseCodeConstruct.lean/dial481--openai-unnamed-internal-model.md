---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/SparseCodeConstruct.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/SparseCodeConstruct.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/SparseCodeConstruct.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Explicit sparse parity-check constructor

Every choice below is executable: two finite searches, arithmetic index
equivalences, and restriction to the first input columns. The hypotheses of
the local-code and Walsh existence lemmas are discharged by the parameter
bounds. No code or expander is supplied as an assumption to the final rows.


### `constructedMatrix`

 Total matrix constructor; zero columns and invalid B use the explicit
zero matrix. The final correctness theorem assumes B is positive. 

### `rows_kernel_bound`

 Unconditional small-weight detection, stated in the integer form needed
by the tuple-sampler interface. 
