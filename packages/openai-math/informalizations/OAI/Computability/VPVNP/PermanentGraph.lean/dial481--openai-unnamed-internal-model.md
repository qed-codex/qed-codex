---
{
  "module": "OAI/Computability/VPVNP/PermanentGraph.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PermanentGraph.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PermanentGraph.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The cycle-cover graph for exact-one clauses

For each occurrence `g` there are three internal vertices. Its first port meets the
arc of the variable ring corresponding to the satisfying literal. Its second port
meets the loop of its clause. Separate occurrence gadgets distinguish all parallel
clause loops. One unmarked row on each ring carries the weight of a true assignment.


### `Exterior`

 Vertices outside the equality gadgets, consisting of variable-ring rows and clause
vertices. 

### `Interior`

 The three internal vertices of each literal occurrence's equality gadget. 

### `Vertex`

 The full index set of the permanent matrix, including the equality gadgets, rings, and
clauses. 

### `markedPosition`

 The ring row assigned to an occurrence, on the ring of that occurrence's variable. 

### `markedPort`

 The marked arc exists only on the ring of the occurrence's variable and only in
its satisfying direction. 

### `ringEntry`

 Destination of a ring arc, before the gadget's internal rows are expanded. 

### `ringExit`

 The exterior ring vertex reached when an occurrence gadget takes the satisfying ring
direction. 

### `clauseExit`

 The clause vertex connected to the outgoing clause port of this occurrence. 

### `ringLabel`

 A true ring direction uses a variable label only on the dedicated row `m`. 

### `ringWeight`

 Evaluate a ring arc at the supplied weights. Only the true direction on the dedicated row
`m` contributes the variable weight. 

### `ringEntry_ne`

 The two ring arcs have distinct endpoints, including at a marked occurrence. 

### `graphLabels`

 Every adjacency entry is a single variable or a single scalar. 

### `graphMatrix`

 The matrix obtained by evaluating all arc labels of the permanent gadget at the specified
weights and equality-gadget parameter. 
