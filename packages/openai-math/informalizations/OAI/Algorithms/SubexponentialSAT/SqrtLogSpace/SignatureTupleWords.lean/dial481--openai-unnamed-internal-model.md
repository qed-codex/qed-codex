---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/SignatureTupleWords.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/SignatureTupleWords.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/SignatureTupleWords.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Exact physical words for the emitted numeric head representatives. These
are proof-level coordinate maps; the executable cursor retains only its bounded
binary word and uses the existing native selected-coordinate scan. 

### `representative_selected_word`

 The numeric representative word is exactly the selected ambient bits of
its source head assignment, in the physical loader's ascending coordinate
order. This includes an empty head and does not select a key representative
in a second, potentially different order. 

### `ambientAssignment`

 An ambient extension used only to identify the physical selected bits. 

### `emitted_word`

 The actual numeric candidate supplies a concrete ambient extension whose
selected word is exactly the saved representative payload. 
