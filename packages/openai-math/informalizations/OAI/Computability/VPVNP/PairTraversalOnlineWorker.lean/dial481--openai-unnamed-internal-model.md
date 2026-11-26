---
{
  "module": "OAI/Computability/VPVNP/PairTraversalOnlineWorker.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalOnlineWorker.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalOnlineWorker.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Running traversal workers with the selected layer's directory words

A leaf, a placement fiber and a role tag are written by fixed programs. At
their online entry the current site ordinal and the layout words are in
registers. Each former parameter or state load becomes a single private copy.
The emitted events, memory image and branch bits agree with the original
worker, including every iteration of the fiber scan.


### `code`

 Replace the component's public inputs and persistent input with register reads. 

### `liftExec`

 Lift a worker derivation to a call with runtime directory words. The
outer machine retains its persistent state and every register outside the scratch bank. 

### `restrictExec`

 Conversely, every successful enclosing execution restricts to a genuine
execution of the original program. Both directions include the exact event log. 

### `Allocation`

 The three workers share at most seven scratch registers, six directory
words and the site cursor. The enclosing machine can reserve more registers. 

### `Allocation.scratch`

 Embed the seven registers available for a traversal worker's scratch calculations. 

### `Allocation.bank`

 Assign each of the worker's six runtime bank words to its enclosing register. 

### `Allocation.site`

 Register holding the current site ordinal for the installed worker. 

### `«prefix»`

 Scratch registers occupy positions 0 through 6. The six layout words
occupy positions 7 through 12 and the site cursor occupies position 13. 

### `regs`

 Restrict the seven-register scratch embedding to the smaller bank required by a particular
worker. 

### `words`

 Select a prefix of the six runtime bank words for a worker with fewer parameters. 

### `leaf`

 Install the leaf-row writer with its allocated scratch registers, directory words, and site
ordinal. 

### `fiber`

 Install the preimage-fiber row writer using the full scratch and public parameter banks. 

### `role`

 Install the role-tag writer for a single selected site using the corresponding smaller
register banks. 

### `leafEvents`

 The two header writes in chronological order, with their private ticks. 

### `leaf_exec`

 The linked leaf body accepts arbitrary scratch contents and uses the
runtime base and stride. Its successor is in scratch register zero. 

### `role_exec`

 The tag worker writes the computed role address and advances scratch
register zero. The preloaded tag can vary between sites. 

### `fiber_exec`

 Translate the complete current placement fiber. The node headers cost
three probes and every child contributes one read and one write. 

### `execute_then`

 Compile the worker followed by the caller's continuation in one instruction
table. The continuation receives exactly the worker's final registers, external
memory, unused fuel and unused choice bits. 
