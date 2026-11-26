---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/CodeSearchProgramEnumeration.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/CodeSearchProgramEnumeration.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/CodeSearchProgramEnumeration.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fixed-control enumeration of the code-construction search spaces

The very same 83-label bit program enumerates all dimensions. Dimension is a
unary input stack, not the size of a generated instruction table. The output
is the actual framed list in the order produced by that program. Theorems
below charge the complete list, including candidates subsequently rejected.
Preparing the input dimension and fixed alphabet, and checking candidates,
are separate stages: this module does not pretend they are free.


### `enumerationProgram`

 The instruction table is fixed, independent of all numerical parameters. 

### `enumerationInput`

 All input arrays are explicit. The scalar alphabet is the fixed two- or
three-element array at the applications; the unary dimension is input data. 
