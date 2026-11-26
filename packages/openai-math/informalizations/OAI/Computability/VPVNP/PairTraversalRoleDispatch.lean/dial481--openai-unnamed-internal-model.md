---
{
  "module": "OAI/Computability/VPVNP/PairTraversalRoleDispatch.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalRoleDispatch.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalRoleDispatch.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The native dispatch opcode reads the selected pass's role

The DFS uses a word-valued node address. The table uses the same absolute
address plus a fixed public offset. The full tag-region bound proves there
is no wraparound for any selected node.


### `Role.dispatch`

 Case labels used in the native router. 

### `Reads.dispatch`

 At any selected layer and site, the machine's one external read dispatches
to precisely the handler corresponding to the retained pass origin. 
