---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryJetSelected.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryJetSelected.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryJetSelected.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Exact dense semantics of the native selected-factor run after immediate
Boolean specialization. The common lifting marker remains through products. 

### `indicatorJet_eval_congr`

 The indicator only uses its scalar coefficients, shared marker, and input.
Thus two coefficient-ring maps agreeing on those data give the same value. 

### `selectedValue_eval_congr`

 Naturality of the actual selected expression, including marked violations
and neutral IDs, under maps that retain the common lifting marker. 

### `selectedValue_specialized_dense`

 The actual source expression computed from already-specialized incidence
jets has exactly the bounded dense value of the unspecialized expression. 

### `selectedFactor_step_specialized_dense`

 One actual selected-factor multiplication extends an arbitrary valid
empty-support accumulator. Both the resulting validity and its dense value
refer to the same native product output. 

### `selectedRun_specialized_dense`

 The SAME native selected-run output over empty-support incidence dictionaries
has the specialized dense product value. The incidence denotation premises are
literal-scoped and supplied by the actual specialized producer. 

### `grouped_dense_query_rescan`

 The exact dense query in the form tested by the native full-head rescan:
the complete attained key and correction condition guard each contribution.
The shared-marker readout is applied after every group multiplication. 
