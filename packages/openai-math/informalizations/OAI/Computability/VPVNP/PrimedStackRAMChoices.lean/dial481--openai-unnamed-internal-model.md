---
{
  "module": "OAI/Computability/VPVNP/PrimedStackRAMChoices.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedStackRAMChoices.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedStackRAMChoices.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Complete word choices at a parser node

The private RAM consumes one word at a terminal and three at an internal node.
A call cannot accept with unused choices. Separating this exact-length check
from the range checks identifies the same choice streams as the mathematical
token decoder, including truncated and overlong streams.


### `RawChoice`

 Words guessed at one parser node before checking their bounds. A leaf carries a position,
and a binary node carries a split and two child states. 

### `exactChoice`

 Decode the entire branch tape as one width-`w` position word for a leaf or three width-`w`
words for a binary node. Return `none` for a truncated tape or leftover bits. 

### `RawChoice.token`

 Convert a raw choice to a grammar token by checking the leaf position against `m` or the
binary split against `d` and both child states against `H`. 

### `RawChoice.isLeaf`

 Test whether the raw node choice consists of a single leaf-position word. 

### `completeNode`

 The outgoing call state, requiring the branch tape to be consumed exactly. 

### `setGuess`

 Store the guessed word in the first register of the supplied embedding and clear the other
two registers used by the word reader. 

### `choiceRegs`

 Register file after the node guesses. Register 2 holds the leaf position or split, and
binary nodes also place the left and right states in registers 3 and 4. 

### `RawChoice.lines`

 Select the leaf or binary instruction block that processes the guessed words after the
stack pop. 

### `RawChoice.events`

 Private word-reader trace for the leaf position or, at a binary node, the concatenated
traces for the split, left state, and right state. 

### `completeNode_pop`

 After the initial pop, the complete native node accepts exactly the decoded
raw choice and then executes the corresponding leaf or internal block. 
