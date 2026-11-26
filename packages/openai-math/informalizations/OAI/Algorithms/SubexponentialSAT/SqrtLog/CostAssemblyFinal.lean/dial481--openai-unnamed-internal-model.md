---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/CostAssemblyFinal.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/CostAssemblyFinal.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/CostAssemblyFinal.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 One closed cost expression with actual jet order, hash candidate count,
high-incidence branch count, and joint-signature/head enumeration. The two
remaining algorithmic interfaces are setup work and ordinary primitive work. 

### `Resources.labelRows`

 Rank used only to bound the number of attained signatures.  It need
  not be the number of rows stored or processed by the native program. 

### `Resources.bits`

 Primitive coefficient/key costs; these use the actual retained rows. 

### `Resources.ordinary`

 Includes actual matrix rows and payload dimensions, even when they
  exceed the rank parameter `labelRows`. 

### `exponentConstant`

 All fixed-k numerical losses are displayed in this coefficient. 

### `assembledWork_target`

 A sequence-specific global estimate: its constant may depend on `p`.
The uniform solver interface is `assembledWork_uniform_cutoff` in
`CostAssemblyUniform`, which handles every resource record above one cutoff. 
