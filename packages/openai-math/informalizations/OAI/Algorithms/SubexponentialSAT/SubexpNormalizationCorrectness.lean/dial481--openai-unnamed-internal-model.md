---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpNormalizationCorrectness.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpNormalizationCorrectness.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpNormalizationCorrectness.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

+# Canonical-input correctness of the encoded normalizer

The program consumes the body left by the separate header parser. The output
is exactly the typed sparsifier's ordered normalized input. The declared
variable universe is retained, so unused coordinates require no renaming.


### `canonical_body_runsIn`

 The output is the exact ordered list that initializes the typed worklist. 

### `canonical_body_inputLength_runsIn`

 The bound may use the complete input length although the header is parsed
by a separate program. This theorem does not charge that separate parsing. 
