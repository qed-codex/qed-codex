---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/HashInputProgramLift.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HashInputProgramLift.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HashInputProgramLift.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Native integer-representative coefficient lifting. The only arithmetic
performed by the machine is the audited dynamic padding/clearing routine. 

### `lift_runs`

 A single fixed program produces the whole flat extension-ring constant.
The runtime shape contains one bit per output bit, and is consumed. Long padded
input representations are cleared with their actual lengths charged. 
