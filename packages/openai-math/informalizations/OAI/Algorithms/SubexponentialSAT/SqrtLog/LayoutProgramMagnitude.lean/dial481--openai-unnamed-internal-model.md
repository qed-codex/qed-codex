---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutProgramMagnitude.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutProgramMagnitude.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutProgramMagnitude.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Unsigned component-total budgets for the signed-pair implementation.
These bounds do not infer component size from the absolute signed difference.
The physical arithmetic refinement must prove its total obeys this recurrence. 

### `scalarMass`

 The nonnegative recurrence for one scalar numerator. Sign swaps leave this
quantity unchanged, and pair addition/multiplication have no cancellation. 

### `scalar_components_le`

 A consumer needs a bound on each component, not just on their difference. 

### `constraintMassBound`

 Safe full cleared-constraint budget, including the diagonal denominator. 

### `fiberMass_le`

 Summing an incidence fiber grows unsigned total at most linearly in the
number of copies. Repetitions are counted; no cancellation is used. 
