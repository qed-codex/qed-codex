---
{
  "module": "OAI/Computability/VPVNP/PairSimulationMapCallSetup.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapCallSetup.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapCallSetup.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Computing initial map registers from the private call descriptor

The caller supplies the live widths, one base per endpoint, the copy count, and
the directory, selector-array, label-array and histogram bases. The fixed register
recipes compute all derived bounds from these words. Reads access private memory.


### `arg`

 Expression that loads a map-call operand from the private descriptor at the offset assigned
by `args`. 

### `recipe`

 Expression for each register, including unused scratch registers initialized to zero. 

### `recipes`

 Index the initial register expressions by the compiler's numerical output slots, using
`slots.symm` to recover each logical map register. 

### `eval_arg`

 One private load in a compiled expression reads the designated descriptor word. 

### `values`

 The natural data supplied by the caller, converted to machine words. 

### `load`

 Exact native setup prefix before directory construction. Its outputs are the
map's allocated registers, and its fixed length is independent of all live widths. 

### `ready_of_registers`

 Combine the computed register formulas with the actual incident bit cells and
the newly installed directory. All remaining assumptions refer to the call operands. 

### `Input`

 Raw caller data for initializing the map, independent of the selector sequence. 

### `native`

 The descriptor reader and directory writer leave the actual map program ready at
its first instruction, preserving every private cell outside the fixed port directory. 
