---
{
  "module": "OAI/Computability/VPVNP/PairSelectedKernelReaders.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSelectedKernelReaders.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSelectedKernelReaders.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Identifying the actual local kernel reader at every recorded pass

The origin recorded by the online descriptor selects the very same shrink
or refresh term parser as the repeated monomial history, including its
kernel witnesses and all private choice words.


### `originReader`

 Recover the concrete local term parser indicated by the recorded
pass constructor, before any surrounding bind or repeat operation. 

### `ReaderOrigins`

 Agreement holds for all choices of the local profile, including the
next pass selected by each possible continuation. 

### `execute_originReaders`

 Matching the physical origin now rewrites the whole selected term parser
to the shrink or refresh implementation proved at that origin. 
