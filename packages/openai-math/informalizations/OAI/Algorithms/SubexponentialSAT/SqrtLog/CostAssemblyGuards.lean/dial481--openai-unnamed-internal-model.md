---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/CostAssemblyGuards.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/CostAssemblyGuards.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/CostAssemblyGuards.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Uniform large-input success of the actual integer parameter guards.
The cutoff is selected before the produced input.  The nonempty-formula and
neutral-coverage premises are explicit semantic obligations of the caller. 

### `parameter_guards_uniform_cutoff`

 One cutoff handles every branch-dependent produced parameter record.
The numerical factor count and width are unrestricted here: they affect the
jet order but do not occur in the executable feasibility guard. 

### `eventually_parameter_guards_ambient`

 Fixed ambient polylogarithmic scope bounds suffice for every retained-half
branch.  No choice of a branch or formula precedes the cutoff. 
