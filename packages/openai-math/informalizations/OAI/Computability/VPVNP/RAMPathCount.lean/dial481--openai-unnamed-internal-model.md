---
{
  "module": "OAI/Computability/VPVNP/RAMPathCount.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMPathCount.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMPathCount.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Counting RAM paths as a contraction of local validators

For every shared-bit assignment, the factor at a site is the number of its
successful local branch histories. All these sets are finite, even for
malformed messages. Summing their product gives the genuine capped RAM
path count in Lemma 10.1.


### `SitePaths`

 Lists of call reports accepted by a single site's validator for the given shared-bit
assignment. 

### `parsimoniousRAMTranscripts`

 Lemma 10.1. The sites use the exact bit layout of (10.1), with the
first and last successor fields clamped. 
