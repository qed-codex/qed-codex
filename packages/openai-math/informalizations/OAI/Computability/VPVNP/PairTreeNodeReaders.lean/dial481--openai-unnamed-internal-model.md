---
{
  "module": "OAI/Computability/VPVNP/PairTreeNodeReaders.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTreeNodeReaders.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTreeNodeReaders.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Local role-reader contracts for exact traversal of a selected term tree 

### `nodeReader`

 This is the local part of the term's reader: first the independent
child half-wires, then that term's own checked kernel choices. 

### `nodeStep_of_suffix`

 Suffix equality and the effect of the native writes suffice for both
directions of the term-row contract. The write effect is required only for
the exact placed assignment and local kernel occurrence read by that row. 

### `children_childPackets`

 With the state parser's actual half-wire order the child packet list is
literally the one built by the selected term's native argument pass. 

### `leaf_subtrees`

 The physical leaf's suffix equality with its cursor reader and its
preservation of the pending packets give the initial subtree induction. 

### `ExactBlock.unique`

 The selected occurrence is unique for any exact native suffix, including
the empty suffix used by the actual burst return. 
