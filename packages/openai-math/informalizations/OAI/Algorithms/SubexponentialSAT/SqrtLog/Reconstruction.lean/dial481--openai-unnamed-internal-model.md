---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/Reconstruction.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/Reconstruction.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/Reconstruction.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Explicit reconstruction for independently chosen node and jet counts

This interface reuses the audited dense-list Hermite program. Its inverse
table is computed by finite powers and geometric sums. No interpolation
choice, scalar-inverse oracle, or field assumption on the coefficient ring
occurs in `run`. The represented arithmetic callbacks carry their own costs.


### `run`

 Execute the complete dense reconstruction, including inverse preparation. 

### `HasJets`

 The node evaluator can supply either this identity or coefficient identities. 

### `run_correct`

 Full reconstruction from finite-ring jets; the residue field is used only
to certify the inverses computed inside the executable program. 

### `run_head_eq_eval_zero`

 The first returned coefficient is the value needed for exact counting. 

### `run_length`

 Only a linear number of output coefficients is retained. 
