---
{
  "module": "OAI/Computability/VPVNP/PairSimulationMapHandlerOperand.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapHandlerOperand.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapHandlerOperand.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Calling a grouped matrix on its prepared physical operands

The selected role's data are one entry input and the associated resident wire
and descriptor addresses. The native writer reads its six real operands and
publishes the descriptor at the evaluated base. This interface retains every
register and memory frame needed to continue at the next resident row.


### `index`

 The demand-grid point and party selecting the handler for this entry. 

### `layout`

 The selected handler's map call table layout. 

### `Workspace`

 Memory locations and size bounds for running the selected map on this entry's bits. 

### `names`

 Parameter ordinals reported by the entry evaluator, or `none` on rejection. 

### `pub`

 Value of the selected handler's `j`-th public operand at entry. 

### `state`

 Value of the sixth operand, used as the state word in descriptor expressions. 

### `addr`

 Descriptor base address evaluated from the handler's six operands and external memory. 

### `Prepared`

 Numerical and semantic facts established by the selected physical shrink
or refresh operand materializer, at the handler's actual entry configuration. 

### `native`

 This is the physical step consumed by the resident loop. The bound is the
selected handler's clock; its exact external count is the operand expression loads. 
