---
{
  "module": "OAI/Computability/VPVNP/RAMProcessorGlobalCredit.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorGlobalCredit.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorGlobalCredit.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Initializing the processor's remaining global allowance

The input cap and incoming cumulative cost occupy binary words. The processor
copies both words, subtracts the cost from the cap, and rejects on a final
borrow. The cap, the cumulative cost, and the other call counters survive this
operation. The running time is linear in the word width and the old output.


### `State`

 Control states for staging the cap and cost, clearing the destination and subtracting to
compute the remaining global credit. 

### `body`

 The no-borrow exit returns to the caller. A borrow stops the entire path. 

### `routine`

 Compute the remaining global credit by subtracting cumulative cost from the cap, rejecting
if subtraction borrows past the word. 

### `run`

 Every valid pair of input words has a deterministic path of the same
length. The final control is the rejecting halt exactly when the cost
exceeds the cap. All ports except the global allowance are restored. 

### `remaining_val`

 The arithmetic word represents ordinary natural subtraction whenever
initialization returns, including at exact exhaustion of the global allowance. 
