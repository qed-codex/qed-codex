---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpMainDecode.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpMainDecode.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpMainDecode.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The concrete flat-coefficient decoder installed in the main caller ABI. 

### `scratch`

 Decoder scratch is in the low workspace. Its polynomial/answer, modulus,
and width occupy the agreed persistent ports. 

### `installed_head`

 The exposed bit is produced by the actual remainder/positivity decoder. 

### `execution`

 The caller supplies the concrete encoded flat polynomial, modulus, width,
and empty local work ports. The theorem supplies the exact lifted execution;
it has no premise postulating a decoder algorithm or its cost. 
