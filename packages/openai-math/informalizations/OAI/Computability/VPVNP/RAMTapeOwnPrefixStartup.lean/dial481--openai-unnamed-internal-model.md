---
{
  "module": "OAI/Computability/VPVNP/RAMTapeOwnPrefixStartup.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeOwnPrefixStartup.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeOwnPrefixStartup.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The six live public inputs from the original site tape

The physical processor first parses its own tape and computes the four
geometry words. It retains the literal self-delimiting prefix on a stack.
A fixed routine copies that stack into the fifth and sixth public fields
as its length and packed value. The startup code has no program-text operand.


### `Port`

 Combined physical processor ports and arithmetic bank with six public inputs, including the
two parsed prefix words. 

### `savedPrefix`

 Processor stack retaining the complete parsed self-delimiting prefix. 

### `geometryBank`

 Intermediate arithmetic bank containing the four geometry words, empty prefix-word slots,
and zero-valued registers and persistent word. 

### `startup`

 Parse and load the physical operand bank. Its fixed code depends only
on the register count and the cost parameters of the processor. 
