---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/MomentsProgramDictionaryBase.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/MomentsProgramDictionaryBase.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/MomentsProgramDictionaryBase.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Fixed physical dictionary-insertion program. All dictionary/key/vector
lengths are input data. The complete semantic composition is proved separately;
this file defines the finite table and its paid stack primitives. 

### `parseRegisters`

 The parser's destination is reversed; transferring it to native stack9
restores the old coefficient vector to forward order before addition. 

### `insert`

 Dictionary15, query.reverse16, new coefficient17, modulus5, coefficient
width12, extension dimension24 are inputs. Result dictionary15 replaces the
old value by new+old, once the local semantic composition is discharged. 
