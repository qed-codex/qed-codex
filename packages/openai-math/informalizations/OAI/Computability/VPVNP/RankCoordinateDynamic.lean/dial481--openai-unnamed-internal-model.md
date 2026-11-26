---
{
  "module": "OAI/Computability/VPVNP/RankCoordinateDynamic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateDynamic.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateDynamic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Preparing the query-dependent Cramer row and target

The rank and length of the equation block are fixed advice. Adding its rank to
the current basis ordinal gives a greedy row query whose returned original
index locates the source basis monomial. Adding the same rank to the next
ordinal gives the row to replace in the square numerator.


### `Host`

 The eight-register ISA stack bank, including its persistent, scratch and private-log ports,
together with the ordinal selector’s auxiliary ports. 

### `regs`

 Registers contain current, next, equation rank, equation-row count, the
two combined ordinals, original selected row, and selected monomial ordinal. 

### `bank`

 Combine the live coordinate registers with the auxiliary stacks of the ordinal selector. 

### `indexPorts`

 Wire the selector's input and output to registers four and six while leaving its auxiliary
ports in their own bank. 

### `machine`

 The greedy selector reads the current combined ordinal from register four.
The two outputs for the Cramer caller are registers five and seven. 

### `overhead`

 Tick allowance for computing the two rank offsets, clearing the selector’s result register
and subtracting the equation-row count after selection. 

### `machine_bounded`

 Actual register and greedy-index execution. The result includes all offsets,
the requested basis monomial, and the selector's reusable workspace. 
