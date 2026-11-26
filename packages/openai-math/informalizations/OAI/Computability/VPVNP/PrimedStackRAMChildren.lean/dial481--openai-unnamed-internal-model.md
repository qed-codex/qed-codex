---
{
  "module": "OAI/Computability/VPVNP/PrimedStackRAMChildren.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedStackRAMChildren.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedStackRAMChildren.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Pushing two pending subtrees

The word code validates a chosen split and both child states, then pushes the
right child followed by the left child. The next pop therefore visits the left
subtree. Both pushes use the same external depth word and two frame planes.


### `rightFrame`

 Check the chosen split and state words, then form the right child in registers 0 and 1. 

### `leftFrame`

 Form the left child from the retained split and left-state words. 

### `pushChildren`

 Check the split and child states, then push the right frame followed by the left frame so
that preorder traversal pops the left child first. 

### `pushChildren_rep`

 The abstract stack after the genuine two pushes, including the eight external probes. 

### `child_degrees`

 For a legal split the two computed degree words are precisely the
integer left and right degrees. In particular subtraction does not wrap. 
