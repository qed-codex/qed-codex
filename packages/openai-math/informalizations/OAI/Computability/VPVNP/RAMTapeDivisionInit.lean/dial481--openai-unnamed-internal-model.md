---
{
  "module": "OAI/Computability/VPVNP/RAMTapeDivisionInit.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeDivisionInit.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeDivisionInit.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Initialization and division by zero on bit stacks

Reversing the input exposes the dividend in most-significant-bit order.
While saving the divisor the machine records whether any bit is set and
allocates a zero remainder cell for each divisor bit. Restoring the saved
divisor then branches on the computed nonzero flag.


### `initRun`

 The initial scans detect a zero divisor at every width, including zero.
They consume the dividend stack, restore the divisor, and prepare a zero
remainder of exactly the divisor's width. 

### `zeroRun`

 After zero-divisor detection the machine returns an all-zero quotient
and the original dividend as remainder, both at the dividend's width. 
