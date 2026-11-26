---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkWidthFootprints.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkWidthFootprints.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkWidthFootprints.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Probes of dense shrinking width, prefix, AB and absolute-ID workers

All bounds concern the chronological source events. For both scattered
payloads the rank and owner cells keep their original values throughout
the scan, so indirect writes stay in the two reserved rectangles.


### `Checked`

 A scan covers cursor ordinals from zero to the bound and confines all its external reads
and writes to their respective allowed regions. 

### `coordinates`

 The same quotient and remainder index the sorted prefixes and AB pieces. 

### `prefixReads`

 Addresses the prefix worker may read in the per-bundle width rectangle and the column of
running bundle totals. 

### `prefixWrites`

 Addresses the prefix worker may write in the per-bundle start-offset rectangle and the
totals column. 

### `abReads`

 The bundle-total column from which the AB worker reads its balancing inputs. 

### `abWrites`

 Allowed write addresses for the AB worker. The two rectangles reserve a full row stride per
bundle for piece widths and starting offsets. 

### `scatterReads`

 Addresses in the owner, rank and old-width columns consulted by the width scatter. 

### `scatterWrites`

 The two consecutive sorted-width rectangles, one for thick entries and one for CD entries,
that receive the scatter writes. 
