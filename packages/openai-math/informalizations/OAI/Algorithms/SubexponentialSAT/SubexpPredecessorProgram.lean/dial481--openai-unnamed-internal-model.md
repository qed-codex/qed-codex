---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpPredecessorProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpPredecessorProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpPredecessorProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 A nine-label bit program for fixed-width binary decrement. 

### `predecessorProgram`

 Register 0 is the borrow. The initializer sets it to one, after which
each bit uses XOR and AND to propagate that borrow through the runtime word. 

### `predecessor_trace`

 Exact execution count, with a direct connection to the verified subtractor. 
