---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSiteLiteral.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSiteLiteral.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSiteLiteral.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Loading the validator's fixed initial word

The word scan used by the private instruction set also loads a fixed natural
literal into an arbitrary bank. Its template gives the word width, and the
two reverse stacks are empty again when the subroutine returns.


### `routine`

 Load a fixed natural literal into a word using the operand scanner on the specified ports. 
