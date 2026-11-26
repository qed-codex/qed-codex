---
{
  "module": "OAI/Computability/VPVNP/RAMTapeDivisionRestore.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeDivisionRestore.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeDivisionRestore.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Restore scan for binary division

Each iteration restores one divisor bit and consumes the corresponding bits
of both possible remainders. The borrow from the forward scan determines
which bit is written. Reversing the three scratch stacks in this way puts
the resulting words back in least-significant-bit-first order.


### `restoreRun`

 Restore the divisor and select the low word of the old or trial
remainder. The final empty pop transfers control to the quotient digit. 
