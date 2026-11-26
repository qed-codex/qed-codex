---
{
  "module": "OAI/Computability/VPVNP/RAMTapeInputParametersMultiply.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeInputParametersMultiply.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeInputParametersMultiply.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fixed unary multiplication for the live input parameters

Transfer the left factor to the outer scratch stack. For each of its tally marks,
restore one mark to the left input and add a copy of the right input to the accumulator.
The two inputs and both scratch stacks are restored at the normal return.


### `mulAdd`

 Add the product of the two input tallies to `dst`. 

### `mulFrame`

 Frame for the three stacks that change during the outer loop. 
