---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpNodeFilter.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpNodeFilter.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpNodeFilter.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A fixed-control nonzero-record filter for field nodes

The parser supplies each reversed payload. The callback copies it, executes
the verified positivity scanner on the copy, and emits the preserved original
exactly when it is nonzero. Retained records are prepended, so their final order
is the reverse of the input's filtered order.


### `ports`

 Parser registers 0,1,2; scan registers 3,4; register 5 is framed.
Stacks: unread records 0, original payload 1, scan copy 2, copy scratch 3,
retained output records 4. 

### `cmd_eval`

 Complete measured execution of the fixed filter command, including
preservation of previously accumulated output records. 

### `program`

 One fixed finite instruction table for every field size and word width. 
