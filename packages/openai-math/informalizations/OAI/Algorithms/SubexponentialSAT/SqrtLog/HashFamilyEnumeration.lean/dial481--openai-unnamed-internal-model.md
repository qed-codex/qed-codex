---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/HashFamilyEnumeration.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HashFamilyEnumeration.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HashFamilyEnumeration.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

### `candidateEquivFin`

 Explicit mixed-radix indexing: the coordinate tuple is encoded in base
`m`, and the coefficient tuple in base three. No choice is used by the map. 

### `enumerate`

 The finite hash family, in a computable order suitable for `List.ofFn`. 

### `enumerate_detection`

 The indexed family detects every heavy vector on at least a third of its
indices, with repetitions in coordinate tuples and even repeated rows kept. 
