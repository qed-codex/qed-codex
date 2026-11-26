---
{
  "module": "OAI/Computability/VPVNP/EvaluatorOutput.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorOutput.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorOutput.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reading the unit coordinate and branching on the final residue

The basis list of Lemma 8.2 starts at the unit, with ordinal zero. A path
ending elsewhere rejects. At ordinal zero the machine reads only the first
limb of the accumulated field product. The width stack supplies the number
of bits to read, so higher polynomial-basis coefficients never enter the
residue comparison.


### `Port`

 The basis ordinal, limb-width tally and accumulated field product read by the terminal
residue test. 

### `Phase`

 Control for testing the unit ordinal and comparing successive guessed bits with the low
limb of the accumulated product. 

### `routine`

 The bound comparison runs from low to high bits. On exhaustion the two
possible branch targets already encode the comparison of the whole word. 

### `bank`

 The named stacks used by the terminal reader. All other stacks of the
whole evaluator can be framed around this routine. 

### `count_output`

 With a correct endpoint the continuation is never entered: every accepted
guess halts directly. The result is the ordinary natural value of the low limb. 

### `count_output_limb`

 Applied to the field representation, the terminal machine counts the
low prime-field coefficient if and only if the final ordinal is zero. 

### `allStops_output`

 Every terminal branch halts within its linear clock. The endpoint and low
limb tests only consume their inputs, including on a rejecting branch. 
