---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/ExecutionHashAlphabet.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/ExecutionHashAlphabet.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/ExecutionHashAlphabet.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 A paid, runtime-sized alphabet for the sparse-hash selector.  The existing
binary countdown emits all words below the supplied count; this wrapper also
clears its padded counter.  No instruction table depends on the count or word
width.  Only the six explicitly mapped stacks can change. 

### `generate_eval`

 The binary count on port0 is consumed and all work ports are cleaned.
The complete framed alphabet is produced on port5; every other caller stack
and register is preserved literally. 
