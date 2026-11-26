---
{
  "module": "OAI/Computability/VPVNP/DegreeRefreshStep.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/DegreeRefreshStep.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/DegreeRefreshStep.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The degree refresh as a placed wire-kernel step

In Section 7.3, each old position becomes a port of its block. Its vertex
factor stays whole at that port. The local map reads the outgoing external
word, the incoming word in source-segment order, and the selected supply
half-wires. All padding wires have their unique zero-bit payload.


### `oldWireGraph`

 The old wire network in block, slot, and old source-port coordinates. 

### `OutputEdge`

 External slots, one copy of the supply edges per block, and cyclic padding slots. 

### `refreshOutput`

 The selected output has one external slot per port. Each copy of the
supply graph lies within one block, as do all cyclic padding arcs. 

### `outputAssignments`

 Concatenated external words and internal assignments together specify
one assignment to the output wires, with every padding slot uniquely filled. 

### `supplyHalf`

 The two half-wire lists of the supply motif are read from the internal
arcs of this block, retaining their independent source and target values. 

### `refreshTerm`

 The port-local term of (7.1) for one joint selection of the block motif maps. 

### `refreshTerm_value`

 For a selected term the shared output-edge sum equals the sum over the
external strings and the independent internal assignments in every block. 

### `refreshStep`

 An ordinary motif identity in each block produces the degree-refresh
step of (7.1), with identity placement in the grouped port coordinates. 
