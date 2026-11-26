---
{
  "module": "OAI/Computability/VPVNP/CompressorBundleRankLayout.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBundleRankLayout.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBundleRankLayout.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Array layout for gathering keys and ranking every original arc

The rank pass shares the append pass's owner, stride, and count parameters.
It reads the classifier's key column and the new rectangular key rows. Static
interval bounds verify its memory frame even for probes in the padding at the
end of a short thick row.


### `rankPublic`

 Construct the six operands of the bundle ranking pass from the inherited parameters and the
supplied key, output and destination words. 

### `separated`

 Two disjoint half-open intervals, in either physical order. 

### `RankLayout`

 The materialized key rectangle must preserve the owner/count columns.
The rank destination column is separate from all four arrays read by ranking. 
