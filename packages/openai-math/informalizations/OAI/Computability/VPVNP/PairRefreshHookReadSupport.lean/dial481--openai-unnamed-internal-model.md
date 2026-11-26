---
{
  "module": "OAI/Computability/VPVNP/PairRefreshHookReadSupport.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairRefreshHookReadSupport.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairRefreshHookReadSupport.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# External reads of an accepted refresh hook

The locator may read the terminal scalars at offsets 1, 15, 16 and 17.
All other reads precede the terminal header. The concrete old and new
incidence regions and refresh scratch allocation supply their address bounds.


### `read_worker_layout`

 A successful parse only probes the allowed words of the enclosing terminal
worker. Both packed column sizes come from the selected old position count. 
