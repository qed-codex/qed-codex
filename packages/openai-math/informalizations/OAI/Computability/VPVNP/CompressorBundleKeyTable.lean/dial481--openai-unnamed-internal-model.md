---
{
  "module": "OAI/Computability/VPVNP/CompressorBundleKeyTable.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBundleKeyTable.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBundleKeyTable.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Materializing keys for every thick-wire and motif bundle

The preimage table has two consecutive sets of bundle rows. Each set has
a fixed number of live entries per row. The key table uses the same stride
as the ID table, so the rank scan reads its row and offset directly.
Successive runs of the three-probe worker share their external memory.


### `KeyTable`

 The four external arrays and the shape of the two sets of bundle rows. 

### `KeyTable.idsBase`

 Base of the strided bundle rows containing the arc identifiers to look up. 

### `KeyTable.keyBase`

 Base of the key array addressed by arc identifier. 

### `KeyTable.outputBase`

 Base of the strided output rows receiving the gathered keys. 

### `KeyTable.widthBase`

 Base of the width array associated with the bundle key table. 

### `KeyTable.bundles`

 Number of bundles represented in each of the thick-wire and motif row banks. 

### `KeyTable.stride`

 Number of words reserved per physical bundle row. 

### `KeyTable.thickCount`

 Number of occupied thick-wire entries in each bundle. 

### `KeyTable.motifCount`

 Number of occupied motif entries in each bundle. 

### `KeyTable.arcCount`

 Size of the arc-identifier domain used to look up keys. 

### `bundle_row_lengths_add`

 In each bundle, the thick-wire row and the motif row account for every
color-mask and slot-label combination exactly once. 

### `bundle_rows_total`

 Both gather scans together read exactly the old physical arc count. 

### `rowSize`

 Thick-wire rows precede the motif rows. 

### `idStart`

 Natural address of the first identifier in physical row `b`. 

### `outStart`

 Natural address at which gathered keys for physical row `b` begin. 

### `lookup`

 Read the identifier at row `b`, offset `i`, then read its key from the lookup array. 

### `rowPublic`

 The row gather receives the base addresses of the identifier row, the key lookup, and the
output row. 

### `Layout`

 Both row tables occupy whole rectangles. The destination rectangle is
disjoint from the ID table and from both absolute-arc columns. 

### `outAddress_eq`

 The word address used by the rank worker agrees with the rectangular
natural address for every slot, including the padding. 

### `Runs`

 Each row scan uses the memory left by all preceding rows. Its exact
cost, persistent cursor, readback, and external frame are recorded. 

### `Completed`

 Exactly the live prefixes of the completed rows have been written. The
frame also covers every unused padding cell inside a completed row. 

### `Completed.inputs`

 Throughout a prefix of the scan all cells of the ID, classifier-key,
and old-width inputs retain their original values. 

### `entries`

 Number of actual ID entries in the first `k` rows. 

### `runPrefix`

 Materialize any prefix of the two rectangular tables in ordinal bucket
order, accounting for the shorter real prefixes of thick-wire rows. 

### `run`

 The whole pair of tables in ordinal order, with exactly four charged
operations per real entry across both kinds of bundles. 

### `dyadic`

 Instantiate the row counts for the dyadic packing with `n` base sites,
degree `2^a`, and `g` residual lane bits. 

### `dyadic_run`

 For the packing's actual two row counts the full materialization costs
exactly four charged operations per original arc. 
