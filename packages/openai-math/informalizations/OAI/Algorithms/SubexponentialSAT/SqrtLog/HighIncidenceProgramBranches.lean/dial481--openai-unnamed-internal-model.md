---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/HighIncidenceProgramBranches.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HighIncidenceProgramBranches.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HighIncidenceProgramBranches.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Runtime Boolean branch initialization and exhaustive odometer traces.
The only parameter in the enumeration command is its fixed real callback.
The high dimension is data, not finite control. 

### `enumerate_high`

 The initialized one-bit records enumerate exactly all assignments to the
selected coordinates. Every callback is an actual trace; rejected branches
remain in the cost and in the visit log. 

### `covers_high_assignment`

 Every h-bit high assignment has its own actual callback invocation. 
