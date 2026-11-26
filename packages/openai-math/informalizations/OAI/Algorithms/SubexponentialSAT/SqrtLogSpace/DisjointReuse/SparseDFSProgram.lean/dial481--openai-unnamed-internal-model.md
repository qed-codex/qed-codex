---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/SparseDFSProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/SparseDFSProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/SparseDFSProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Fixed finite control for the outer disjoint counting traversal.

The leaf command is an explicit piece of finite code chosen with `k`. Its
layout, reconstruction, input loading and output export are still
separate obligations until the concrete leaf implementation is substituted.
There is no oracle instruction or endpoint theorem in this module.


### `splitterView`

 The splitter keeps the threshold outside its entire local footprint. 

### `clearPorts`

 The finite list is part of the instruction table, never a stored work list. 

### `lowPorts`

 The fixed low-workspace ports, kept opaque to avoid reducing the entire
256-element instruction table during routine typeclass and theorem checking. 

### `testPending`

 Every iteration re-reads the physical pending tag after all callbacks. 

### `startTotal`

 The total stack is empty on entry and becomes canonical binary zero. 

### `finishVisit`

 Explicitly discard the current body and every low workspace port before
retesting the frontier. No callback cleanup or register persistence is implicit. 

### `body`

 `leaf` includes the actual charged leaf loaders, computation, result
export to stack263, and cleanup. It must preserve the persistent outer frame. 

### `exportCount`

 Physically clear the external word and copy scratch before preserving bit
order in the final canonical output. Retained raw input is charged here. 

### `command`

 This command starts from an already normalized current body, saved original
header and chosen threshold. Preprocessing is charged in the caller. 

### `exportCount_prefix_space`

 Output cleanup and copying use only their own linear work, never the
exponentially long traversal time; every one of the 1220 stacks is counted. 

### `body_branch_eval`

 Once concrete phase executions are proved, this is the exact branch trace
of the already defined body; the found flag is consumed immediately. 

### `raw_branch_count_reverse`

 The physical selector filter accumulates its records in reverse order.
Only the selected finite family matters, and the variable type stays `Fin n`. 
