---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpLayoutConstruction.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpLayoutConstruction.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpLayoutConstruction.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Concrete raw factor construction for the layout phase

The fixed program constructs the unary-factor prefix, its shape masters, and
all clause factors in encounter order. The paired family mapper performs the
actual concatenation. The same resulting scope stream feeds assignment and
the same table stream feeds the later source builder.


### `program_runs`

 Both streams arise from the actual fixed programs, and the retained raw
input and scalar words survive the complete construction. 
