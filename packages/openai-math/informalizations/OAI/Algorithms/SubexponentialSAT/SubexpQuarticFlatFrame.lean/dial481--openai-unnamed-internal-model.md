---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpQuarticFlatFrame.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpQuarticFlatFrame.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpQuarticFlatFrame.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Store frames and fixed caller ports for the flat quartic service. 

### `finalStore_updates`

 Relative to a valid input store, only the consumed operands and product
output change. This form supports an arbitrary surrounding caller frame. 

### `resultStacks`

 The only three stacks changed at the end of the multiplication call. 

### `resultRegs`

 Registers outside the assigned eight registers retain their caller values. 

### `denseRegisters`

 The dense-polynomial caller reserves registers 0--7 for this subroutine. 

### `densePort`

 The 61 bank words occupy 30--90; the modulus is the caller's stack 5.
Inputs/output occupy 11/12/13, with reduction cache 91 and unary width 10. 
