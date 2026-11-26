---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/SquarefreeProgramLookup.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/SquarefreeProgramLookup.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/SquarefreeProgramLookup.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 A fixed primitive dictionary lookup. Dictionary normalization guarantees
unique keys. All key and coefficient bits are scanned by the existing finite
record program; key width, coefficient width and dictionary length are runtime
data and do not affect the instruction table. 

### `fetch_eq_lookup`

 On a normalized dictionary, mathematical additive fetch is first-match lookup. 

### `dictionaryLookup_encoded`

 Fully encoded lookup, with the semantic option returned on the output stack. 

### `lookupBudget_bound`

 All scan costs, including failed key comparisons, are linear in serialized
key/payload lengths times the number of entries, with explicit query scans. 
