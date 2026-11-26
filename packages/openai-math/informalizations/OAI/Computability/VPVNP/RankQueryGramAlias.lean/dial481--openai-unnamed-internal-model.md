---
{
  "module": "OAI/Computability/VPVNP/RankQueryGramAlias.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryGramAlias.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryGramAlias.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Installing Gram reads at the Schur engine's actual ports

Three input registers read the Schur output descriptor directly. The Gram
multiplier's accumulator is the engine's return-value port. Both banks keep
their input widths, advice and private-register invariants across calls.


### `Aux`

 Auxiliary ports of the descriptor adapter, combining the Schur dispatch word bank with the
signed Gram coefficient and entry-reader ports. 

### `leftBank`

 Embed the Schur dispatch word bank in the left summand of the adapter's auxiliary ports. 

### `outputSlot`

 The Schur dispatch register that holds output word `i` of the six-word descriptor. 

### `wires`

 Place the six descriptor wires in dispatch output registers and take the coefficient,
scratch and extra wires from the Gram bank. 

### `slot`

 Identify the aliased Gram inputs by mapping word registers zero through two to descriptor
outputs one through three. Other ports yield `none`. 

### `gramPorts`

 Connect the first three Gram input registers to the Schur descriptor, the product
accumulator to the engine result, and the remaining ports to Gram auxiliary storage. 

### `FixedParams`

 Gram input register three holds the column count `m`, and input registers four through
seven hold zero. 

### `RightReady`

 The Gram bank has the fixed inputs for `m`, a clean multiplier with packed field advice and
empty operands, and an entry-reader bank satisfying `ready`. 

### `Ready`

 The Schur dispatch bank is prepared for row count `n` and the Gram bank for column count
`m`, field advice `c` and a ready entry reader. 

### `valueRoutine`

 Install the coefficient callback selected by `neg` on the engine's Gram ports so it reads
the descriptor and writes to the result stack. 

### `gram`

 Use the supplied matrix-entry reader to evaluate a weighted Gram coefficient directly into
the engine result, negating it when `neg` is true. 

### `prepareRegs`

 Reuse the three Schur output words as the row, column and degree of a
Gram input. The inactive Gram copies of these words stay in the caller. 

### `CallRuns`

 A signed scalar-entry call uses two row indices and a coefficient degree.
Its fixed program and mathematical entry map may come from the weighted
Gram matrix or a constant-polynomial Cramer matrix. 
