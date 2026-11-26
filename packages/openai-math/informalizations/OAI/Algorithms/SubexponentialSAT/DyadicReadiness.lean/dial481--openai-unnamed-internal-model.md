---
{
  "module": "OAI/Algorithms/SubexponentialSAT/DyadicReadiness.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/DyadicReadiness.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/DyadicReadiness.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Readiness and layout inequalities for the implemented dyadic selector

All numerical schedules in this file are `DyadicSchedule` definitions.  The
fixed parameter `T` remains visible.  Readiness uses the proved polynomial
incidence bound for every fixed `k,T`; the separate `Control k T` certificate
is needed for the sparsification budget, not for these layout inequalities.


### `degree_budget`

 The floor defining R always respects the degree budget. 

### `parameters`

 The genuine multicolor parameter record for the dyadic schedule. 

### `eventually_ready`

 Both growing arithmetic checks hold eventually for every fixed k,T.
No tail or block-threshold assumption is supplied by the caller. 

### `exists_fallback_cutoff`

 Failed checks occur below one fixed input-size cutoff. 

### `parameter_threshold`

 The exact universal-type threshold needed by the layout constructor. 

### `weighted_tail`

 The integer readiness guard implies the degree-cleared tensor tail bound
used by the actual multicolor layout constructor. 

### `fallback_machine`

 A single finite fallback machine handles every failed dyadic guard.
This does not claim that the guard or the large-input solver is compiled. 
