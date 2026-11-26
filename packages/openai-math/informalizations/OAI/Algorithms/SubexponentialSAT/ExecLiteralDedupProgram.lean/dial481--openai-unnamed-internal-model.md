---
{
  "module": "OAI/Algorithms/SubexponentialSAT/ExecLiteralDedupProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ExecLiteralDedupProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ExecLiteralDedupProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Actual stable literal deduplication

The fixed program tests each record against the remaining records, retains its
last occurrence, and restores record order. All membership, copy, emission,
and reversal calls are concrete finite programs with measured executions.


### `budget`

 The suffix-dependent cost counts the actual complete callback at each
record; the parser and loop-control costs are included separately. 

### `dedup`

 The complete routine uses its input stack again for the final ordered
output. Its reversed accumulator and every work stack finish empty. 

### `literal_runsIn`

 On actual unary literal fields, the result is precisely the executable
CNF normalizer's stable, last-occurrence literal deduplication. 
