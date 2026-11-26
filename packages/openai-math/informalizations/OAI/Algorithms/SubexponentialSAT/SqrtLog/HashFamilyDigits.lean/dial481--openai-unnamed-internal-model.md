---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/HashFamilyDigits.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HashFamilyDigits.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HashFamilyDigits.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

### `digitEquiv`

 A combined alphabet digit is `coordinate + m * coefficient`. 

### `candidateDigitsEquiv`

 Coordinate/coefficient tuples are equivalent to strings in the combined
alphabet, keeping every occurrence separately even when coordinates repeat. 

### `enumerateDigits`

 Runtime-friendly base-`3*m` enumeration; position zero is least significant. 

### `listing_detection`

 Any bijective listing is valid, including a program's different tuple
order. This theorem imposes no choice operation on the supplied listing. 
