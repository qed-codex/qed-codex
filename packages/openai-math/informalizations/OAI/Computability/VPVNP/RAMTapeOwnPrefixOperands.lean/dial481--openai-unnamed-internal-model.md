---
{
  "module": "OAI/Computability/VPVNP/RAMTapeOwnPrefixOperands.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeOwnPrefixOperands.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeOwnPrefixOperands.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Computing the live operand vector with the processor's own code as data

Compose the six-word physical startup with the finite arithmetic expression
loader. The primed assembler's length and packed-prefix slots agree with its
specification for the actual program, although the loader is fixed before
this program is chosen.


### `operandStartup`

 Parse the physical site and its prefix into six public words, then run the operand program
on that bank. 

### `operandCoefficient`

 Clock coefficient for parsing the physical inputs, packing the actual prefix, evaluating
geometry, and filling the operand slots. 

### `eventually_prefix_fits`

 Every fixed program's literal prefix eventually fits in one live word. 
