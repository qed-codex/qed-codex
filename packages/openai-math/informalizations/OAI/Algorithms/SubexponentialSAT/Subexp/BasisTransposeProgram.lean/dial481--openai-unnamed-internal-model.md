---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/BasisTransposeProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/BasisTransposeProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/BasisTransposeProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Gathering a searched basis table into vector-major order

The local search stores ambient coordinates as rows and basis vectors as
columns. Its scalar frames have fixed width, so the checked gather program
can transpose those frames without decoding or changing a field element.
The result is exactly the kernel/complement table consumed by block copying.

This adapter's runtime inputs are the searched table, its unary frame width,
and the explicit transpose read plan. It proves the physical reordering and
the plan's polynomial size; producing the read-plan bytes is a separate stage.


### `input_tableBits`

 The actual table bytes retained by the encoded basis search are exactly
the physical source array of this gather call. 
