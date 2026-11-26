---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryVisitorCorrect.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryVisitorCorrect.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryVisitorCorrect.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Correctness of the fixed concrete two-pass visitor. 

### `visitor_empty`

 With no emitted heads the fixed visitor still constructs and contributes
the ring unit. Both real replay paths and the real normalization tail execute;
there is no empty-formula Boolean shortcut. 

### `multiply_masterFrame`

 Concrete multiplication preserves the retained query snapshot. Its
changing head/tuple dictionaries are separate from the pair accumulator. 

### `multiply_run`

 The fixed native multiply consumes the actual head sum and retains its
full dense product. Readout is deferred until the completed tuple is added. 

### `readHead_state_bound`

 Parsing a retained representative frame restores the same word bound.
The decoded word and the remaining address are portions of actual stored
words, so their numerical values never become a storage charge. 

### `install_run`

 The first-pass native overlay updates only the ambient representative
baseline. All ring inputs, the tuple product and the pair accumulator retain
their actual words and denotations. 

### `prepare_run`

 The actual full-key and correction-gate setup preserves the three
semantic invariants needed by the subsequent head sum and multiplication. 
