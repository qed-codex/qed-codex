---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/ReconstructionProgramRing.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/ReconstructionProgramRing.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/ReconstructionProgramRing.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Source-preserving CRT adapters for the native arbitrary-degree ring
programs. The adapter is a fixed finite table. Its cost includes three input
copies, the actual native trace, output copying and cleanup. 

### `ports`

 Native arithmetic uses its own bank; the four retained caches are shared
with the local polynomial services. 

### `NativeSpec`

 This contract refers to the actual native program trace. 
