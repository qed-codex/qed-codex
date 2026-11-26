---
{
  "module": "OAI/Computability/VPVNP/CompressorChoiceGridStage.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorChoiceGridStage.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorChoiceGridStage.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Executing rounded-grid selection and outer term choice on demand records

The demand scanner and the fixed grid tests share a register file in one
compiled call. The call returns the first covering grid row. The term reader
computes its repetition count from the same demand records and chooses the
outer supply vector. The code uses the ordered grid fixed by Theorem 6.1.


### `join`

 The two fixed tables share a register file and occupy disjoint parts of
the public constants. Their normal control edge is the sequence instruction
link, so no dynamic memory entry is supplied for the energy. 

### `code`

 Instruction sequence that prepares the demand energy before scanning the candidate grid
rows. 

### `machine`

 Instantiate the demand-grid program with the chosen demand order, energy weights and
candidate-row coefficients. 

### `native`

 This call begins at the ordinary machine entry point. Its return word
indexes the same first covering point as the mathematical grid search. 

### `fixedRows`

 Rows are ordered exactly as in the fixed rounded demand grid. 

### `chooseTerm`

 Run the grid call followed by the demand-to-payload calls. The first
returned field identifies the fixed template used for the local maps. 

### `chooseTerm_spec`

 All dynamic motif data come from actual demand records. The three reset
calls choose the original fixed grid point and admit exactly the binary
streams of Theorem 6.1's outer indices, including its zero-width unit case. 

### `eventually_live_word_fits`

 The fixed motif's word requirement is eventually met by the Section 9.1
machine uniformly over every polynomial bound on intermediate demand widths. 
