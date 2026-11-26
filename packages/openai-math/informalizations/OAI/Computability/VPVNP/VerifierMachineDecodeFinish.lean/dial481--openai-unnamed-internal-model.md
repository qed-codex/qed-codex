---
{
  "module": "OAI/Computability/VPVNP/VerifierMachineDecodeFinish.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/VerifierMachineDecodeFinish.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/VerifierMachineDecodeFinish.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Correctness of the completed row scan

The final endpoint has to agree with both the number of bits actually scanned and the outer
unary length. Together these checks identify exactly the canonical prefix of a valid machine.


### `finished_iff`

 Finishing at the end of the announced table length is equivalent to successful decoding
of a program satisfying the requested wire. 
