---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/PackingLoaderProgramCore.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/PackingLoaderProgramCore.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/PackingLoaderProgramCore.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Native alphabet/seed construction followed by actual assignment copying.
The old producer is used at delta=0 so the seed count is exactly ambient+factors;
the new scorer's four-word depth is installed separately. 

### `core_eval`

 Actual generation from numeric parameters and the installed raw pair
bytes. No alphabet, seed list, or initialized assignment is an input. 
