---
{
  "module": "OAI/Computability/VPVNP/PrimedStackRAMNodeTable.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedStackRAMNodeTable.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedStackRAMNodeTable.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fixed word-RAM table for a node of the primed counter

After popping the top frame, the degree determines whether the next choice is
one word or three. The zero register for this test is initialized by the pop.
Each chooser uses registers 8 and 12 temporarily. On entry register 5 gives
the offset of the assembled input row. A standalone call can initialize it
from the persistent word.


### `straight`

 Turn a nonempty straight-line segment into structured code with exactly the
same number of instructions. 

### `contains_straight`

 Every compiled occurrence of a nonempty straight-line sequence contains the
genuine opcode block used in its trace specification. 

### `lines`

 A nonempty literal instruction list. 

### `guessRegs`

 Choices have distinct result, weight and zero registers. The scratch
registers are shared by the three successive invocations. 

### `leafLines`

 Check and mark the chosen terminal position, read its input bit, compute the terminal
production index, and increment its count. 

### `binaryChecks`

 Check that the chosen split is below the popped degree and both child states are below the
public state count. 

### `binaryLines`

 Validate the binary choice, increment its production count, and push the right child
followed by the left for preorder traversal. 

### `leafFlow`

 Structured RAM code that guesses one terminal position and executes the leaf instruction
list. 

### `binaryFlow`

 Structured RAM code that guesses a degree split and two child states before executing the
binary instruction list. 

### `nodeFlow`

 Structured code for one preorder visit. Pop a frame and branch on whether its degree is
zero. 

### `nodeTemplate`

 Standalone instruction table for one node, initialized by copying the persistent state word
into register 5 as the input-row offset. 

### `leafWork`

 Exact number of elementary word instructions when a leaf succeeds, including
the one-word guess and the branch on the popped degree. 

### `binaryWork`

 The three fixed-width choices of an internal node. 
