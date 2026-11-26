---
{
  "module": "OAI/Computability/VPVNP/PrimedStackRAM.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedStackRAM.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedStackRAM.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Constant-probe instructions for the primed parser

Registers 0 and 1 hold the current degree minus one and nonterminal state.
Register 2 holds a chosen location or split. Registers 3 and 4 hold child
states, 5 is the offset of the input row, 6 is the selected bit, and 7 is the
dense production index. The remaining registers are private temporaries.

Public words 0 through 4 are the degree-plane, state-plane, mark, histogram and
depth addresses. Words 5, 6, 7 are the stack capacity, number of positions and
number of states. Words 8, 9, 10 are the input base, terminal-label count and
total label count. These are public parameters of a fixed instruction table.


### `Line`

 One straight-line instruction for the primed parser, with sixteen registers and eleven
public words. 

### `push`

 Push the frame in registers 0 and 1. The pointer records the next free slot. 

### `pop`

 Pop the most recently pushed frame into registers 0 and 1. 

### `mark`

 Reject a repeated leaf and mark its position otherwise. 

### `clearMark`

 Clear the indicated mark while preparing a fresh site. 

### `leafBit`

 Fetch one bit of the assembled input row. 

### `increment`

 Increment the word for a production. Reject an out-of-range label or a wrapped count. 

### `terminalIndex`

 Private arithmetic for the terminal production (state, position, bit). 

### `binaryIndex`

 Private arithmetic for the ordered binary production. Degree is positive
on entry, so its triangular prefix is degree times (degree minus one) divided by two. 

### `push_spec`

 The written degree, state and depth are exactly the three payloads of a push. 

### `pop_spec`

 Popping reads the words at the previous top and decreases the depth. 

### `mark_spec`

 The distinct-position test succeeds exactly on an unused position in range. 
