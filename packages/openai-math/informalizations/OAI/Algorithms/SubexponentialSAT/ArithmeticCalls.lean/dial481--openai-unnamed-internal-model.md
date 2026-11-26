---
{
  "module": "OAI/Algorithms/SubexponentialSAT/ArithmeticCalls.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ArithmeticCalls.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ArithmeticCalls.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Source-preserving arithmetic calls on fixed Boolean-stack ports

Operands are copied into distinct work ports before the actual finite adder or
multiplier runs. The source ports may coincide. The only final stack change is
the output word; every work port is restored to its incoming empty state.


### `multiplyAt_eval`

 Source-preserving binary multiplication by an actual finite program.
All five work stacks are empty in the returned state, because only out changes. 

### `addAt_eval`

 Source-preserving binary addition, with an explicit carry reset before
the verified little-endian adder. 
