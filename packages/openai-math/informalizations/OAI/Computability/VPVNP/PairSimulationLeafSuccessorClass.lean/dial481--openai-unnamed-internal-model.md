---
{
  "module": "OAI/Computability/VPVNP/PairSimulationLeafSuccessorClass.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafSuccessorClass.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafSuccessorClass.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native successor-class selection

A nonwrapping successor flips a nonempty low-bit prefix. The six native
rows compute its XOR mask and count the halvings needed to reach one.
The sender and unit registers are preserved, including at mask one.


### `instruction`

 Sender, unit, mask and class occupy registers 0, 1, 2 and 3 respectively. 

### `Linked`

 The host contains the six rows that compute a nonwrapping successor's XOR mask and its
class by repeated halving. 

### `Result`

 Exact observable state at the continuation. Only the two output
registers may have changed, and the final mask is one. 

### `native`

 Compute the class of the actual successor edge using an arbitrary
embedding into a native RAM table. Each successful loop iteration costs
three instructions, in addition to initialization and the last test. 
