---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSortLayerRows.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortLayerRows.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortLayerRows.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Physical execution of a complete sorting layer

The fixed row traversal implements the local and cross-site comparators on
arbitrary five-word inputs. It preserves the input block, consumes exactly
the two exchange fields when the stride crosses sites, and accumulates the
selected records and every canonicality and outgoing-copy check.


### `runs`

 Complete row traversal at the word width of the five-word record format. 
