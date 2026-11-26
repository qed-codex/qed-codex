---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/ScoreBuilderRefinement.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/ScoreBuilderRefinement.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/ScoreBuilderRefinement.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Exact refinement of the fixed score builder

The execution theorem below starts from the actual controller memory and
encoded read-only tables. Its output is the natural conditional objective in
the exact order consumed by the first-minimum routine.


### `refines_of_cost_bound`

 The remaining premise is a uniform numerical bound on an already proved
instruction count, not an assumed execution of a score oracle. 

### `assignmentProgram`

 One fixed controller, independent of all mathematical parameters. 
