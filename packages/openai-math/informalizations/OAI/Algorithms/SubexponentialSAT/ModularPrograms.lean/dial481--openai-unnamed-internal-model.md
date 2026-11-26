---
{
  "module": "OAI/Algorithms/SubexponentialSAT/ModularPrograms.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ModularPrograms.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ModularPrograms.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Finite Boolean-stack programs for modular arithmetic

The programs in this file use only a fixed finite collection of labels,
Boolean registers, and Boolean stacks. The operand width and modulus are data.


### `borrowBit_gate_form`

 A full subtractor using only the Boolean gates in BitProgram.
The two product terms are disjoint, so XOR implements their disjunction. 

### `subtractProgram`

 Three operand stacks, eight Boolean registers, and thirteen fixed labels.
Register 0 is the incoming/outgoing borrow. Stacks 0 and 1 are consumed;
stack 2 receives the reversed difference. 

### `roundRegs`

 Exact register transformation of one subtraction cell. 

### `subtract_round`

 An actual twelve-instruction trace of the fixed Boolean program. 

### `subtract_correct`

 Full measured subtraction on arbitrary equal-width operands. 

### `subtract_comparison`

 The final borrow is a comparison result produced by the measured program,
not by a natural-number comparison instruction. 

### `paddingProgram`

 Pad a modulus word to the width of a shape word. Both input stacks are
consumed; the padded word is pushed in reverse onto output stack 2. 

### `reverseOutput`

 Reorient the reversed result while preserving the borrow register. 

### `append_reverse_output`

 Sequentially link a proved arithmetic run to a proved transfer run.
Both runs execute inside the concrete linked finite instruction table. 

### `subtractLE_correct`

 A reusable subtraction program returning a little-endian result.
Its exact cost includes the result-reversal routine and both return jumps. 

 Preserve a candidate word while subtracting a modulus from its copy. 

### `selectDifferenceProgram`

 Select the saved candidate on borrow; otherwise reverse the difference.
The unused candidate and all work stacks are consumed in either branch. 
