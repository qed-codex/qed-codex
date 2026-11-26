---
{
  "module": "OAI/Computability/VPVNP/SliceArithmeticHornerPrepare.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticHornerPrepare.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticHornerPrepare.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Preparing the bit stacks for a Horner digit

Each digit reuses the stored modulus and multiplier. The machine restores the
row count, loads the next high-degree-first digit, clears the predecessor and
negates the accumulator's top coefficient left in register six by the last
round. A single whole-stack reversal installs the output for the next round.


### `Extra`

 Ports holding the saved modulus coefficients, multiplier and row count, together with the
live row, digit, and round streams. 

### `Ports`

 Register and stream ports of the complete Horner multiplication controller. 

### `extra`

 State of the saved polynomial and multiplier streams, unary row counts, pending digit bits,
and remaining rounds. 

### `streams`

 Install the old accumulator, reduction coefficients, multiplier coefficients, and output
bits alongside the caller's streams. 

### `prepare`

 Stage the row inputs, load the next Horner digit, clear the predecessor, and negate the top
accumulator limb for reduction. 

### `prepared`

 The register changes at the start of a Horner round. 

### `restore`

 Replace the consumed accumulator by the coefficient scan's bit-reversed output. 
