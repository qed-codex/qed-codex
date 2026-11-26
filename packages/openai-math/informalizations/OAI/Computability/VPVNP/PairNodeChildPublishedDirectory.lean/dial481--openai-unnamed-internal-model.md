---
{
  "module": "OAI/Computability/VPVNP/PairNodeChildPublishedDirectory.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNodeChildPublishedDirectory.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNodeChildPublishedDirectory.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The child decoder's directory in the published DFS level

The retained row base occupies scalar 14. The metadata writer publishes the
row stride, old degree, argument arena and stride, inverse-incidence pointer
and width pointer in scalars 15 through 20. These seven consecutive words
are the operand bank read by the native child header.


### `directory_of_payload`

 The first six metadata operands after the retained row pointer are the
six remaining words consumed by the child decoder. 

### `directory_retain`

 Later planner and traversal reports may change memory anywhere outside
these seven words while preserving the decoder's operand bank. 

### `directory_at_locator`

 The child handoff's old-level pointer names the retained seven fields in
the actual traversal memory. The bootstrap supplies the first header and the
level pitch, and the traversal frame preserves every cell before its rows. 

### `Published.shrink_child_directory`

 The actual three selected metadata publications give the child directory
in their post-memory. Scalar 14 is inherited from the preceding publication. 

### `Published.refresh_child_directory`

 At a refresh the same seven words describe the unique older child. The
degree comes from the selected refresh scalar, and the two incidence bases
come from its packed old-level head bank. 
