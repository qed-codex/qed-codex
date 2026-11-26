---
{
  "module": "OAI/Computability/VPVNP/LiveProgramPaperParameters.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramPaperParameters.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramPaperParameters.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Joint parameter choices for the live evaluator and the diagonal budget

Choose the chain power, raw-prefix and advice exponents, tape radius and cut
width before choosing the address multiplier. The bound on that multiplier
depends on these fixed exponents. Only then take the eventual threshold in
the input length.


### `paper_parameters`

 One choice of the constants gives simultaneous clock, cut, advice and
outside-budget bounds, as well as sufficient physical word space. 
