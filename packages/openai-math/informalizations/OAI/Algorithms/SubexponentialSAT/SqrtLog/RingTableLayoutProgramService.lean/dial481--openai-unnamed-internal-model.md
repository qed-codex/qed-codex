---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/RingTableLayoutProgramService.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/RingTableLayoutProgramService.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/RingTableLayoutProgramService.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


Integration ABI: two Boolean registers and eighteen stacks. Inputs are the
power-major bit stream on stack 0, a list of length d on stack 1, and a list
of length B on stack 2. Stack 3 receives the forward table. Stacks 4 through
17 are empty on entry and exit. The three inputs are preserved; the registers
are scratch. Neither d nor B occurs in the command's finite control.

Offsets are maintained as unary lists. Each scalar at (i+j)*d+k is fetched by
the native preserving array reader; its bits are transferred to a reverse
accumulator. A final native transfer restores the required forward order.


### `power_table_command_eval`

 Embeddable command contract for the power-generation/table-layout service. 

### `power_table_native_polynomial`

 A dimension-independent finite program with a polynomial native trace bound. 
