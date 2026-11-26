---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpComplementColumnBatch.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpComplementColumnBatch.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpComplementColumnBatch.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Complete complement-column batches

The input stores local-search records in forward color order. This fixed
program copies and reverses those records, reuses them for every runtime
block, and finally prepends the leftover coordinate descriptors.


### `command_eval`

 The reverse-order batch is built by execution. The caller supplies only
the forward local-search records and the two runtime count words. 

### `colorPrefix_reverse`

 Reversing the input batch and counting colors down produces the original
forward color order, with local complement indices in ascending order. 
