---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/RingNodeSetup.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/RingNodeSetup.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/RingNodeSetup.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Paid traversal of the actual framed node table. The remaining cursor and
unary index are physical stacks, and the decoded node is transferred to the
original factor port. No list of semantic nodes is manufactured by the machine. 

### `storeOf`

 Project every named field without changing any other caller stack. 

### `initNodes`

 Initial cursor setup includes clearing stale parser buffers and index. 

### `readNode`

 Consume one outer list tag, read its frame, and put the whole node at78. 

### `advance_eval`

 The supplied native index advance is two real instructions. 

### `nodeRead_frame`

 The node reader has no hidden persistent writes. 

### `nodeRead_boundary`

 A fixed entry bound is restored at the reader boundary. Its temporary
prefix bound must not be fed back as the next node's entry bound. 

### `eval_resources`

 Each local loader trace bounds all stacks and includes the compiled halt.
The caller must restore a fixed boundary between nodes; this lemma does not
charge all completed node invocations as live storage. 
