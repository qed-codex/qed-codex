---
{
  "module": "OAI/Computability/VPVNP/LiveHeaderScalarStages.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderScalarStages.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderScalarStages.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Executions of the scalar stages of the live header program

These stages run once and end with an accepting exit to the next stage. They
read the summary words produced by the index scan and write only their own
specified outputs. Every local operand is the one wired in the complete table.


### `SingleRun`

 A single accepted call to the relocated stage, with its real memory effect. 

### `scalarPub`

 The first sixteen words of the selected header stage's public row, used by its scalar
worker. 

### `Summary`

 The four scratch words consumed after index scanning. 

### `ScalarFit`

 The public and scratch words used by the width and phase stages. 

### `width_run`

 Every width stage has a successful source call. All requested widths
have their exact clamped value, including both incident cuts in the tail. 

### `descriptor_run`

 Each descriptor stage publishes the exact interval to its immediately
following scan. The scratch words are reused between successive fields. 
