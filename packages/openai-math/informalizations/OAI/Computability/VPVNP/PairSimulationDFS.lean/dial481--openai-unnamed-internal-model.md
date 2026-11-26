---
{
  "module": "OAI/Computability/VPVNP/PairSimulationDFS.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationDFS.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationDFS.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Traversing stored child lists inside a final-vertex burst

The private stack grows downward. After a vertex has been popped, a contiguous
private interval immediately before the pending suffix receives its child
descriptor addresses in increasing list order. This uses one external read per
child and leaves the pending suffix and the rest of private memory untouched.
The next pop therefore visits the first child.


### `Represents`

 The live stack, from the first pending visit through the last. 

### `Row`

 The stored count and row pointer of a descriptor. 

### `instruction`

 Registers 0–4 are shared with the contiguous copy loop. Registers 5–8
hold the stack top, stack end, popped descriptor, and child count. 

### `Linked`

 Require the nine dispatcher instructions at the specified program counters and registers.
They pop a node, transfer control to `visit`, prepare its child interval for `copy`, and
jump to `done` on an empty stack. 

### `execute_empty`

 The empty stack enters the continuation with one deterministic test. 

### `execute_pop`

 One pop selects the descriptor at the top and passes the remaining stack
to the vertex code. This step consumes no binary choice or external probe. 

### `execute_children`

 The descriptor header costs two probes, and the loop fetches each child
address once. The returned stack begins with the complete ordered child
list, followed by the original pending vertices. 

### `Visits`

 A terminating descent through the actual rows in external memory.
The list index retains the order of every visit, including multiple visits
to equal descriptor addresses if the input rows contain duplicates. 

### `execute_visits`

 All visits of a finite traversal are realized by the fixed RAM
dispatcher when the entry hook immediately returns to the child-row scan.
The continuation may use all remaining fuel and arbitrary branch bits. 
