---
{
  "module": "OAI/Computability/VPVNP/LiveHeaderScanProtected.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderScanProtected.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderScanProtected.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Processor-site preservation during arbitrary scheduled scans

Even a malformed count or offset cannot redirect a write into the processor
sites. The public cursor guard bounds the destination within its allocated
buffer on every successful copy call.


### `call_preserves_below`

 Any successful scheduled scan preserves every address below the scratch base,
even with arbitrary descriptor words, branch input and initial cursor. 
