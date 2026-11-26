---
{
  "module": "OAI/Computability/VPVNP/RAMTapeDivisionForward.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeDivisionForward.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeDivisionForward.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Forward scan of a restoring division step

The control holds the next shifted candidate bit in `prev`. For each low
position it saves the divisor, candidate and difference bits. At the high
position it subtracts the zero extension of the divisor to obtain the final
borrow. Only the low positions occupy the three scratch stacks.


### `forwardRun`

 A full forward pass saves the three reversed low words and branches on
the same final borrow as subtraction of the zero-extended divisor. 
