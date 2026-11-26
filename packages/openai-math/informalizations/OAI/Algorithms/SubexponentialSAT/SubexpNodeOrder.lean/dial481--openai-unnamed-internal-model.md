---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpNodeOrder.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpNodeOrder.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpNodeOrder.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Interpreting the actual generated node order

A proved permutation of the explicit encoded node table determines an exact
node equivalence in that order. Reindexing searches the concrete finite lists;
it uses neither an abstract finite-field enumeration nor a chosen layout.


### `nodeIndex`

 Executable reindexing from an actually produced permutation of the words
to the previously verified coefficient-list order. 

### `nodeEquiv`

 The semantic field nodes in the actual generated word order. 
