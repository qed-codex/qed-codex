---
{
  "module": "OAI/Computability/VPVNP/RAMValidatorBucket.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMValidatorBucket.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMValidatorBucket.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Bounded machine simulation in a transcript bucket

The range test precedes the private calls. Each call checks all three probe
allowances before consuming a read guess. Once simulation stops, the processor
validates its unused choice suffix and its outgoing cut or terminal halt.


### `Machine.runBucket`

 Execute the calls and check their successor information. This includes
work spent before an eventual failure on arbitrary input. 
