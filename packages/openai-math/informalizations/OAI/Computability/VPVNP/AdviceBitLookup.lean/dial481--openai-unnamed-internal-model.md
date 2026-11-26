---
{
  "module": "OAI/Computability/VPVNP/AdviceBitLookup.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/AdviceBitLookup.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/AdviceBitLookup.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Reading a bit at a unary address in circuit advice

The instruction stream starts with one `true` per skipped value and a terminating
`false`. The routine saves the skipped prefix, copies the addressed bit to the
result stack, and restores the valuation stack in its original order.


### `Port`

 The four stacks used to consume a unary address, inspect the valuation, save its skipped
prefix, and return the selected bit. 

### `State`

 Finite control for skipping valuation bits, reading the addressed bit, and restoring the
skipped prefix in its original order. 

### `code`

 Fixed finite control. A missing delimiter or an out-of-bounds address rejects. 

### `store`

 Assign the supplied instruction stream, valuation, saved prefix, and output to their
respective lookup stacks. 

### `lookup_runs`

 A lookup takes exactly five instructions per skipped bit and five fixed
instructions. Both the remaining advice and the old result tail are preserved. 

### `routine`

 A normal lookup returns to its caller. The malformed-input halt still rejects. 
