---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/HornerProgramServices.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HornerProgramServices.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HornerProgramServices.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Fully discharged native binary services for arbitrary coefficient-vector
length. Shared by Horner, local CRT and dense polynomial services. 

### `NativeReady`

 Persistent native arithmetic metadata and a clean private workspace. 

### `NativeReady.frame_except_low_caches`

 Updating the caller's two polynomial caches does not affect scalar service
readiness; all remaining low ports are retained. 

### `NativeReady.frame`

 Readiness transports across the standard persistent low-frame relation. 

### `NativeReady.update_polynomial_caches`

 The prepared polynomial zero and unary length caches are caller-owned. 
