---
{
  "module": "OAI/Computability/VPVNP/LiveHeaderBootstrap.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderBootstrap.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderBootstrap.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native recovery of the distributed index and advice

The first two stages start on the actual processor memory. Their two tag
writes are carried into the next dispatch. The resulting memory contains
the original packed headers, the index summaries and copied bits, and all
advice words. Every address outside the written regions keeps its value.


### `BootstrapState`

 The bootstrap's recovered group index, summary, advice words, and packed headers, with a
frame for memory outside its writes. 
