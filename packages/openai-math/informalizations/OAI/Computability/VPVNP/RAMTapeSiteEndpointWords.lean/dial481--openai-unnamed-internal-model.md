---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSiteEndpointWords.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSiteEndpointWords.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSiteEndpointWords.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Exact endpoint words for a processor's cost interval

A site numbered `v` with bucket capacity `2^e` checks the two endpoints
`v * 2^e` and `(v+1) * 2^e`. Padding the site address before incrementing it
retains the carry of the final site, whose end word equals the global cap.


### `startWord`

 Word encoding the start of the site’s cost interval, its address multiplied by the
power-of-two bucket capacity. 

### `endWord`

 Word encoding the end of the site’s cost interval, `(v.val + 1) * 2^e` for site address
`v`. 

### `padded`

 Leave room for a carry out of the original address before shifting. 
