---
{
  "module": "OAI/Computability/VPVNP/PairSelectedRowChecks.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSelectedRowChecks.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSelectedRowChecks.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Joining the native shrink and refresh row checks along a selected branch

Each local implementation sees the two actual compressor states on either
side of its own pass, in their numerical slot order. Transport across the
output-network equality and recursion through the selected passes provide
both the decoder and emission contracts for the final term chain.


### `uncastPointers`

 Return a row-pointer family for the original term chain by undoing the transport of its
input network. 

### `pushAddress`

 Transport a numerical site-address function from the term's output network to the equal
network of the following state. 

### `PassChecks`

 Both local obligations at a state pass, with the actual half-wire
packets in its source and successor states. 

### `ExecutionChecks`

 A sequence of checks for the individually selected native shrinking
and degree-refresh rows. 

### `execution_checks`

 A local proof over the actual state records of each pass supplies the
complete selected-branch hypotheses used by the terminal vertex worker. 
