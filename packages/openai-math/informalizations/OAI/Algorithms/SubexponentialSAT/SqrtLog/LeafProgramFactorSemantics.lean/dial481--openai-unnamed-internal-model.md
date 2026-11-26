---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramFactorSemantics.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramFactorSemantics.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramFactorSemantics.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 One executed factor step, specialized to the actual source ring, its
computed multiplication table, and the three physical assignment masters. 

### `product_step`

 Multiplication clips at the existing shared-U and jet cutoffs. The seed
need not be supplied with an artificial untruncated representative. 

### `hash_step`

 Exact expanded raw hash followed by its indicator and seed multiplication. 

### `marked_step`

 The marked row uses its clause fold directly; it has no hash idempotent. 
