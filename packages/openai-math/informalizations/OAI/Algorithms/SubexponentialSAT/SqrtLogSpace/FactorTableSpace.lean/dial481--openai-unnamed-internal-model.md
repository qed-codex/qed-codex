---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/FactorTableSpace.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/FactorTableSpace.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/FactorTableSpace.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Space for one actual ambient-coordinate table construction. Its unary
traversal has only n iterations, so its polynomial local time bounds every
source prefix. No outer signature or finite-difference iteration count occurs
in this estimate. The concrete literal and staging traces are instantiated by
the factor-table producer, rather than supplied to a final counting endpoint. 

### `tableBudget`

 Includes the master's copy, all literal visits, output move and final halt. 

### `tableBudget_le`

 The entire native table construction costs a fixed quadratic polynomial
in the per-literal budget, ambient dimension and specialized payload width. 

### `literalLoop_resources`

 The unary ambient loop itself has one actual existential payload family
and an all-prefix bound linear in its paid number of native body calls. 

### `prepareFactor_resources`

 The actual run chooses each specialized payload after receiving its
register state. The same witness supplies exact table output, time and every
source-prefix bound; no register-uniform byte family is assumed. 

### `initialize_resources`

 Entry clearing is paid using the incoming word lengths, including garbage
in private scratch. Its bound includes the compiled return/halt instruction. 

### `original_stageCost_le`

 The eighteen physical copies have sources disjoint from every destination. 

### `initialized_stack_bound`

 Clearing private scratch cannot increase any incoming stack. 

### `initialized_base_external`

 Every actual external source master survives entry clearing, including
masters702/703 and710..728; no initial scratch-blank premise is used. 

### `stageCost_le`

 The relocated stage includes its compiled call instruction. 

### `stage_resources`

 All staging copies, the cutoff copy and both call and halt instructions
are counted on the same source run. 

### `original_exportCost_le`

 The output is copied into its freshly cleared destination before all340
private source stacks are reclaimed. 

### `exportCost_le`

 One additional instruction invokes the relocated exporter. 

### `export_resources`

 The exact exported table word and every caller stack share one trace. 

### `staged_output`

 Entry clearing and the paid staging leave the export destination empty. 

### `staged_temporary`

 The stage also returns the physical copy temporary empty. 

### `writtenPorts`

 Exactly the ports that may be changed by the table command: relocated
private worker, exported table, and physical copy temporaries. 

### `staged_frame`

 All caller masters outside the finite write set survive actual staging. 

### `exported_frame`

 Export and cleanup preserve every caller port outside the write set. 

### `command_output_frame`

 The exact output state used by the whole command preserves the node
ports, source masters and all other caller words outside its private writes. 

### `command_output_clean`

 Actual export clears the complete private worker and every initialized
backup, leaving only the full table on output62. 

### `command_output_stack_bound`

 Returning a table does not enlarge unrelated caller words. The final
bound is the maximum of the old boundary and the actual exported table word. 

### `caller_port_not_written`

 The protected caller regions include every low node port except the
export62, all eight layout masters, and high ports outside the private bank. 

### `staged_stack_bound`

 Staging ends within its paid local source-prefix bound. 

### `middleBound`

 The middle store retains the old caller data and one polynomial table. 

### `commandBudget`

 The fixed command pays entry clearing, relocated staging, its ambient
unary table loop, relocated export and final halt. 

### `commandBudget_le`

 All pre/postprocessing and the actual table loop fit a fixed quadratic
polynomial; the degree is independent of the input and every traversal count. 

### `command_resources`

 Exact table output, runtime and every source prefix of the same closed
command. The relational literal contract is instantiated by the concrete
producer; it is not an extra premise of the final counting theorem. 
