---
{
  "module": "OAI/Computability/VPVNP/LiveCompressedPairStartupInputs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveCompressedPairStartupInputs.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveCompressedPairStartupInputs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Cursor startup inputs in the live pair ABI

The pair gets its workspace, input length and address width from public slots
two, six and seven. Its dispatch tag is the first old-state word, below the
auxiliary shadow and the cursor workspace. For a polynomially bounded bucket
size all four addresses or values fit the paper's word width eventually.


### `tag_before_workspace`

 The old-state tag precedes the entire cursor workspace, for every layout. 

### `startup_inputs`

 Read the three startup words and the address computed by the actual tag prologue.
Their values are independent of the literal-prefix operands in slots zero and one. 

### `startup_workspace_polynomial`

 The workspace addresses form a polynomially bounded sequence even though
their offset includes every site of the virtual auxiliary RAM. 

### `eventually_startup_inputs`

 One length threshold works for every literal program prefix. 
