---
{
  "module": "OAI/Computability/VPVNP/RAMTapeWordComparison.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeWordComparison.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeWordComparison.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Conditional jumps on staged RAM words

The equality scan remembers whether all pairs of bits have agreed so far.
For an unsigned less-than test, the subtraction scan's final borrow gives
the answer. The machine clears the emitted word before returning, keeping
the branch bit in finite control. The two staged inputs may contain copies
of the same register.


### `Op`

 Equality and unsigned less-than operations used by word-RAM conditional branches. 

### `Op.initial`

 Initialize the equality flag to true or the subtraction borrow to false. 

### `Op.step`

 Update the equality flag and emit zero, or perform a subtraction bit step to update the
less-than borrow. 

### `Op.eval`

 Evaluate the selected equality or unsigned less-than test directly on two fixed-width
words. 

### `State`

 Control states for executing the comparison bit scan and returning its branch decision. 

### `code`

 Install the word scan, using its terminal flag while draining the output. 

### `word_run`

 From two operand copies, return the exact conditional-jump decision and
empty all four ports in a width-independent control. 
