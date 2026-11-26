---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HighQueryLocalBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HighQueryLocalBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HighQueryLocalBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Source-only local costs for the physical high-count controller. Retained
caller words, including the outer marked accumulator322, do not enter them. 

### `seed_eval`

 This is the actual current-mask initialization, with no supplied zero
counter and no bound on unrelated retained stacks. 

### `copy_cost_le`

 The durable high-counter refresh pays only for its source and destination
words; arbitrarily large retained collector words are irrelevant to time. 

### `canonicalize_eval`

 Canonical unsigned readback runs on the actual accumulator and its two
scratch words. This is a source-only time statement, separate from prefix space. 

### `canonicalized_discarded`

 Canonicalization preserves the active source cap while leaving arbitrary
retained caller words outside the time argument. 

### `markedReturn_eval`

 Complete marked readback and cleanup has source-only time on the actual
run. In particular neither the clause tail320 nor accumulator322 is scanned. 

### `acceptedReturn_eval`

 The final accepted query uses the same cleanup and a real copy back788.
The single canonical count word is the only extra word read by this suffix. 

### `seed_resources`

 Source-only seed time and all-prefix caller space are properties of the
same fixed actual run, identified by deterministic execution. 

### `markedReturn_resources`

 The actual marked return carries both independent bounds: active-source
time and a maximum prefix cap covering every retained caller word. 

### `acceptedReturn_resources`

 The accepted output has the same actual source-time/all-prefix guarantee;
its entire canonical binary word remains on788. 
