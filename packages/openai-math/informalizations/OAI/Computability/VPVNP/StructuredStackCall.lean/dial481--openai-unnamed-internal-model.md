---
{
  "module": "OAI/Computability/VPVNP/StructuredStackCall.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/StructuredStackCall.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/StructuredStackCall.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Using an existing finite stack program as a returning routine

The distinguished halt of a legacy program becomes a normal return to the caller.
A deterministic execution ending at that halt has exactly the same length after
installation, provided it starts outside the return state.


### `ofCode`

 Redirect transitions entering the normal completion state to the caller. 
