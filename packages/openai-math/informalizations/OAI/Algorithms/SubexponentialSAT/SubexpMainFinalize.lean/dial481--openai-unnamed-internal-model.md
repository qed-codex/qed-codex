---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpMainFinalize.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpMainFinalize.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpMainFinalize.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Actual decoding followed by reusable-workspace cleanup

The ordinary workspace is cleared by a real fixed program after the decoded
answer has been written to persistent storage. Threshold words and other
persistent data survive. The time bound follows from actual stack-bit growth,
so restoration of the next leaf's workspace is not a free logical operation.


### `withCleanup_bound`

 Every bit in the cleanup region was present on entry or was allocated by
an actual source instruction. Cleanup therefore has linear additional cost. 

### `withCleanup_selected_bound`

 Only the selected workspace is charged. In particular the bound is
independent of the arbitrary unread leaf stream on a persistent stack. 

### `decoder_workspace_frame`

 The decoder uses only low scratch ports below eight and its three
persistent ports. In particular it cannot touch a protected threshold bank. 

### `execution`

 The finalizer preserves the real answer while physically restoring every
selected work stack. Count and all port locations are fixed before input. 

### `execution_selected`

 The per-leaf form excludes persistent unread data from the cleanup cost. 
