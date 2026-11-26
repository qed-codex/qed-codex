---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpScopeProducer.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpScopeProducer.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpScopeProducer.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Construct a clause's local chunk scope from its encoded literals

This fixed program maps actual literal records to chunk records, restores the
record order, and invokes the checked stable deduplicator. Its output order is
the last-occurrence order used by the materializer and incidence-plan producer.


### `typedScope`

 Proof-carrying view of the same emitted numeric scope; its values and
order are unchanged. The machine does not execute the bound proof. 

### `budget`

 Every term counts instructions in a concrete pass over an actual encoding. 
