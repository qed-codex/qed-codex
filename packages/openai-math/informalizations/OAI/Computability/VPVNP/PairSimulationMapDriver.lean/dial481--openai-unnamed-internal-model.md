---
{
  "module": "OAI/Computability/VPVNP/PairSimulationMapDriver.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapDriver.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapDriver.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native dispatch and repetition of the selected map rows

Each pass reads the next private selector ordinal and compares it with the
fixed selector ports. A match jumps directly to the corresponding row's
first instruction. All row subroutines return to the same label store.
After the last copy the driver transfers control to the full-width test.


### `Program`

 Registers hold the selector cursor and end, label cursor, one, loaded
ordinal, comparison temporary, and the label returned by the selected row. 

### `Program.selectors`

 Selectors in the order the driver tests when dispatching a decoded ordinal. 

### `Program.port`

 Public-word position holding the dispatch ordinal for each selector. 

### `Program.reg`

 Place the selector cursor and end, label cursor, increment, loaded ordinal, comparison
  temporary, and returned label in seven distinct registers. 

### `Program.pc`

 Program counters for the five outer-loop instructions that test for completion, load a
  selector, store a label, and advance both cursors. 

### `Program.comparePC`

 Instruction addresses for one selector's dispatch pair. The false branch loads its public
  ordinal and the true branch compares that ordinal with the private one. 

### `Program.rowPC`

 Entry address of the row evaluator chosen by a successful selector comparison. 

### `Program.checkWidths`

 Continuation that checks final widths after the driver consumes the selector array. 

### `Program.bad`

 Rejecting continuation taken when the comparison chain exhausts all selectors. 

### `first`

 An exhausted comparison chain jumps to the rejecting exit. 

### `instruction`

 The five outer-loop instructions for checking the selector cursor, loading the next
ordinal, storing the row's returned label, and incrementing the two cursors. 

### `dispatch`

 Two actual opcodes per fixed selector, with an independent hit target. 

### `Linked`

 The machine implements both the five outer driver instructions and the ordered
load-and-compare dispatch for every selector in the table. 

### `dispatchSteps`

 Two instructions per candidate through the first match, in table order. 

### `dispatch_hit_exact`

 Successful dispatch consumes at most two instructions per selector.
The selected row receives the loaded ordinal and the same private memory. 

### `dispatch_hit`

 Successful dispatch consumes at most two instructions per selector.
The selected row receives the loaded ordinal and the same private memory. 

### `Stable`

 Controller instructions change four registers and may store in the
label array. A row invariant stable under these changes can include all
resident input bits, base addresses, and current demand and supply offsets. 

### `RowRuns`

 One row contract is discharged by the selected row's own native prefix.
It advances the local offsets and leaves the driver cursor words intact. 

### `RowRunsWith`

 A row prefix carrying a further predicate on its actual instruction count. 

### `Ready`

 A ready loop boundary includes all completed labels and all resident
selectors. Unused cells of the output array may hold arbitrary values. 

### `visitCap`

 Budget for one loop test, ordinal load, fixed dispatch, selected row,
label store and two cursor increments. 

### `visitWith`

 The same path returns the label and charges exactly the row's own ticks plus
the comparison-chain ticks and five loop instructions. 

### `visits`

 Repeat actual selected row calls in input order. Every written label is
already available at the next copy boundary, and the next row receives the
updated offset invariant. 

### `native`

 At the final-width checker the label slice is in copy order and the
row invariant has reached its final offsets. This includes the zero-copy
case, which executes exactly the loop's final test. 
