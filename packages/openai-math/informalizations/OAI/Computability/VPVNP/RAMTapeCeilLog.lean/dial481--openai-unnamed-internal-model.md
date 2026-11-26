---
{
  "module": "OAI/Computability/VPVNP/RAMTapeCeilLog.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeCeilLog.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeCeilLog.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A finite stack control for the physical site address width

The source stack holds the input length in unary. A round consumes pairs
of marks, returning one mark per pair, including a final singleton. Every
round with at least two source marks prepends a fixed number of output
marks. The last round consumes zero or one source mark and returns.


### `Port`

 Stack labels for the unary length, its rounded half, and accumulated address-width marks. 

### `Phase`

 Control of the repeated ceiling-halving rounds, with a finite counter for the fixed output
marks per nontrivial round. 

### `code`

 Each nontrivial round emits the fixed `B` bits. The changing count is
stored in unary on the stacks. 

### `store`

 Place the supplied bit lists on the length, intermediate, and width-output stacks. 

### `runs`

 The output stack receives exactly the site's address width
`B * Nat.clog 2 n` in unary. The source and temporary stacks finish empty.
The exact instruction count is `cost B n`, bounded by `cost_le`. 
