---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/NativeOuterBudgets.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/NativeOuterBudgets.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/NativeOuterBudgets.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The exact large-entry arithmetic join: paid canonical frontend, fixed
cutoff test, actual setup, disjoint DFS, full-word positivity and factor-seven
primitive compilation. These numerical bounds introduce no run contract. 

### `entrySpace`

 Each actual source phase is lifted to one bound, once. 

### `entryTime`

 The exact upper bound obtained by composing the measured source phases
and then applying the actual guarded compiler's factor seven. 

### `entrySpace_polynomial`

 Space is polynomial in the original input word, independently of all
visit and leaf-runtime counts. The canonical entry is included. 

### `primitiveSpace_polynomial`

 The exact compiler envelope counts every primitive tape and every
visited prefix, including blank crossings and its fixed control overhead. 

### `entryTime_le`

 The startup body can be shorter than formulaBound. Every visit still
uses the genuine formulaBound budget, including losing selector scans. 

### `entryTime_polynomial`

 Constants and degree depend only on fixed width and the ordinary source
cap, before any formula, visited node, leaf or primitive run is selected. 

### `runtime_of_tree_and_leaf`

 The actual reciprocal-sparsification visits multiply the actual leaf
budget. Their exponents add; the ETH square-root-log scale stays unchanged. 

### `globalBound_polynomial`

 One fixed cap simultaneously satisfies actual startup, visits, the local
leaf, classification and power setup. It is chosen before any input or run. 

### `leafTime_runtimeBound`

 The actual leaf wrapper's linear global-cap work and rounded local time
preserve the same exponential scale. The chosen cap depends only on input
length, and the rounding is confined to this proof-side time bound. 

### `runtime_with_fallback`

 One positive triple of constants covers both the actual large-run time
and the fixed finite fallback, uniformly including ambient n=0. 

### `space_with_fallback`

 The same fixed positive polynomial covers all large primitive visited
space and the actual finite fallback. No runtime or visit count is used. 
