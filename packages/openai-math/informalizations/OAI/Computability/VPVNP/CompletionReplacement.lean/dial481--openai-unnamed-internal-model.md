---
{
  "module": "OAI/Computability/VPVNP/CompletionReplacement.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompletionReplacement.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompletionReplacement.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Replacing a column of a completion

When a fresh column extends an independent frame, it can take the place of
any of the completion columns. The original and the modified completions
together span exactly the completion with the fresh column adjoined.


### `independent_completion_init`

 Discard the last column of an independent completed frame. 

### `independent_completion_replacement`

 Replace one completion column by the last column of an independent extension. 

### `span_completion_sup_replacement`

 The two completions jointly span all the old columns and the new one. 
