---
{
  "module": "OAI/Computability/VPVNP/PairSimulationRouteField.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationRouteField.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationRouteField.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Scanning a resident field for the cursor routing constraints

Each unused outgoing word must be zero. The mode determines the additional
test on the used outgoing field. It is skipped at an active launch, clamped
at an inactive successor, and compared with the selected incoming field at
a transit vertex. The scan accumulates differences into a mask and advances
all three cursors through the full field even after a mismatch.


### `instruction`

 Registers 0–2 are the unused outgoing, used outgoing and selected
incoming cursors. Registers 3–6 are the width, mode, sticky mask and one.
Registers 7–10 are the loop index, zero and two scratch words. 

### `resize_instruction`

 Resizing each instruction preserves its register operands and jump destinations. 

### `Linked`

 Each site in the machine contains its route-field instruction. 

### `PayloadOK`

 The mode word specifies the constraint on the selected outgoing field. 

### `payloadSteps`

 Cost of dispatch and comparison for the selected outgoing word. 

### `steps`

 Two setup instructions, a final exit test, and one pass through each word. 

### `Agrees`

 The bits of all three arrays relevant to the current routing mode. 

### `Preserved`

 The scan preserves the width, mode, constant one and all enclosing registers. 

### `run`

 The fixed jump table checks all resident words in the three routed slices.
The pointers may wrap or overlap. The only size restriction ensures that the
width fits in the loop counter. 
