---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/InterpolationCacheProgramBasic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/InterpolationCacheProgramBasic.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/InterpolationCacheProgramBasic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Fixed local cache-producer instructions and framed native service calls.
The lower256 ports are the existing arithmetic ABI; controller streams and
copy scratch occupy disjoint higher ports. 

### `lowCall_run`

 The service is a real compiled finite subprogram. Its one changed low
port is installed back into the larger controller store; all higher streams
and every other low port are preserved. 
