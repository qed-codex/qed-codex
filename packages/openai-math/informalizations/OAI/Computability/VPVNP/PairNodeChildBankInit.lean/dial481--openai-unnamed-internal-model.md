---
{
  "module": "OAI/Computability/VPVNP/PairNodeChildBankInit.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNodeChildBankInit.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNodeChildBankInit.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Initializing the register bank of child slot ordinals

The first slot receives zero. When a second slot exists it receives one.
Every subsequent instruction adds this stored unit to the preceding slot.
The fixed program uses one private instruction per slot at every word width.


### `next`

 Select the label for child slot `n` while it is in range and transfer to the return label
once the ordinal bank is full. 

### `instruction`

 The label of each slot contains its entire initialization instruction. 

### `Linked`

 Every supplied slot label contains the instruction that initializes its ordinal register
and continues to the next slot or the return label. 

### `native`

 Execute the initializer from arbitrary registers. The argument suffix and
external memory are passed directly to the continuation. 
