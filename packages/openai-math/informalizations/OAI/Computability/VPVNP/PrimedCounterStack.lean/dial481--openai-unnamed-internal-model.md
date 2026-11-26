---
{
  "module": "OAI/Computability/VPVNP/PrimedCounterStack.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterStack.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterStack.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Stack execution of the primed parser

At each visit the machine pops the pending frame, produces one histogram label,
and pushes zero or two frames. The left child is visited first. The executable
scan below agrees with recursive tree decoding for every continuation stack.


### `Frame`

 One pending grammar node represented by its bounded degree index and nonterminal state. 

### `Label`

 A production histogram key for either a terminal position and bit or a binary split with
its parent and child states. 

### `step`

 Pop one frame. The emitted label identifies the counter to increment, and
the replacement frames are prepended to the remaining stack. 

### `scan`

 Execute the flat stream of node choices. Completion requires exhausting
both the input stream and the pending stack at the same visit. 

### `labels`

 The production labels of a tree in visit order. 

### `tally`

 The integer counter vector formed by adding one for each visit. 

### `scan_cons`

 Unrolling one root in a continuation stack consumes exactly one encoded
tree. This also handles malformed or truncated inputs and unused trailing choices. 

### `scan_nil`

 An empty continuation stack cannot accept trailing choices. 

### `scan_root`

 Complete traversal from the prescribed root emits exactly the labels of
the unique parse recovered from this list of choices. 

### `scan_marked`

 Linear mark checks and the stack traversal have the same acceptance
predicate as the recursive reader; every accepted tree supplies its histogram. 
