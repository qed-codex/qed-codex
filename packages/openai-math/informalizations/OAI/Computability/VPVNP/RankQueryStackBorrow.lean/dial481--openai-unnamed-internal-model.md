---
{
  "module": "OAI/Computability/VPVNP/RankQueryStackBorrow.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackBorrow.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackBorrow.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The product-loop counter test in the Schur controller

A zero counter is consumed and yields a true completion flag. A positive
counter loses one, keeps its width, and yields a false completion flag.
The control scans the low zero bits only and reuses one empty scratch stack.


### `Port`

 Counter, borrow scratch stack and completion flag used by the binary decrement routine. 

### `Phase`

 Control phases for scanning low bits, resolving a borrow and reporting whether the counter
was exhausted. 

### `body`

 Decrement a positive little-endian counter by borrowing through its low zero bits, or
signal completion when the counter is zero. 

### `bank`

 Assign the counter bits, scratch contents and flag bits to their three respective ports. 
