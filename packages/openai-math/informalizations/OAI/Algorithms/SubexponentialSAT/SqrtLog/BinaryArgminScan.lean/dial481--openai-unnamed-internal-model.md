---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/BinaryArgminScan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/BinaryArgminScan.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/BinaryArgminScan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A measured binary argmin scan with a paid loader

`LoaderSpec` is a refinement obligation on a fixed, executable command. It
requires an actual `StructuredCalls.Eval` for every callback, including the
final empty callback; it is not an oracle or an instruction for evaluating a
mathematical score. A caller may satisfy it by parsing prepared records or by
enumerating candidates and executing a score program. The incumbent score is
cached. Its first evaluation and the preparation of the initial incumbent are
outside this scan and must be charged by the caller.


### `LoaderSpec`

 This supplies both the callback implementation and its paid trace. The
single queue stack can encode arbitrary loader context. All other ports are
explicitly framed. The callback must work with every incumbent and register
contents satisfying the bit bounds. 

### `scanCommand`

 The command is fixed independently of score widths and candidate counts. 

### `scan_eval`

 Exact semantic refinement of the numerical argmin of `HashSelect`. The
cost includes all losing candidates, all score copies, and the terminal load. 

### `program`

 One fixed finite instruction table for each supplied loader command. 

### `program_trace`

 The refinement above gives a genuine halted `BitProgram` trace. 

### `selected_spec`

 The returned payload belongs to the supplied list, and its binary numeric
score is at most the score of every supplied candidate. 
