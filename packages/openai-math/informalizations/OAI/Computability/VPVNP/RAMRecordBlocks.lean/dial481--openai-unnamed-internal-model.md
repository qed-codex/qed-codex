---
{
  "module": "OAI/Computability/VPVNP/RAMRecordBlocks.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMRecordBlocks.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMRecordBlocks.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Padded record blocks for the RAM transcript

Each site in Lemma 10.1 contributes one initialization record, the probes of the
calls whose starting costs belong to that site, and enough empty slots to fill
a block of size `4H`. Filtering the physical array to its occupied slots gives
exactly the initialization and probe records, up to permutation.


### `siteRecordBlock`

 Fill the slots in a single site. The cost of its first call is supplied
by the predecessor, so probe timestamps are global across sites. 

### `recordBlocks`

 Encode consecutive sites starting at `site`, maintaining the actual
cumulative cost across the entire chain, including the sites after halt. 

### `getElem_recordBlocks`

 The cost supplied to a site's encoder is the sum of the charges at
all preceding sites. Empty buckets contribute no charge. 

### `recordBlocks_perm`

 Gather the initialization records in address order and the probes in time
order. Their interleaving within the physical array preserves their multiset. 

### `canonicalRecordBlocks`

 The input blocks for the global sort, obtained from the unique grouping
by starting costs. Even sites with no calls contribute their header record. 

### `getElem_canonicalRecordBlocks`

 Read the physical row at site `v` directly from its canonical bucket,
using the total cost of the preceding buckets as its start. 
