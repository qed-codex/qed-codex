---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/DensePolynomialProgramAdd.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/DensePolynomialProgramAdd.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/DensePolynomialProgramAdd.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Native addition of dense polynomial arrays whose coefficients have an
arbitrary runtime extension degree. The fixed scanner visits base words;
there is no quartet assumption and no generated instruction table. 

### `addCmd`

 This code is the same fixed scalar-word scanner for every extension degree,
polynomial length, modulus, and coefficient width. 
