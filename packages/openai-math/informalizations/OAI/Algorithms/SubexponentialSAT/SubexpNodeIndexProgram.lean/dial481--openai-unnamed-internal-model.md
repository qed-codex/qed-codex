---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpNodeIndexProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpNodeIndexProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpNodeIndexProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Physical lookup of the current field node

The fixed program copies the framed node table, parses its records in order,
compares their actual bits with the current node, and counts rejected records.
Its only visible stack change is the unary first matching index at port 116.
The source table at 125 and query at 78 are preserved.


### `Clean`

 The five writable ports comprise four scratch words and the result. 

### `command`

 A finite command with only seven assigned ports. 

### `command_eval`

 The result is read from the actual serialized table. No node index is an input. 

### `budget_polynomial`

 The measured program bound is polynomial in actual input word lengths. 

### `index_mem`

 Membership gives a valid matching position in the actual ordered table. 

### `index_of_getElem`

 Distinct encoded nodes identify any canonical position uniquely. 

### `command_eval_getElem`

 The canonical-index corollary still executes the physical search. 
