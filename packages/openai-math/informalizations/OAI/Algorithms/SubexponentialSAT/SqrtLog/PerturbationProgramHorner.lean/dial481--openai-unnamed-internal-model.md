---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/PerturbationProgramHorner.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/PerturbationProgramHorner.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/PerturbationProgramHorner.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Semantic invariant for the actual fixed-width polynomial Horner fold.
Truncation at every multiplication is valid for the final shifted polynomial. 

### `shifted_horner_denote`

 Instantiate with the native fixed-length dense polynomial services. The
premises state decoded arithmetic laws, rather than providing a shift oracle. 
