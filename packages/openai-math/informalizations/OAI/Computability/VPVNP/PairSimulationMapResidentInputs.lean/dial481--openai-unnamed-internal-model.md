---
{
  "module": "OAI/Computability/VPVNP/PairSimulationMapResidentInputs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapResidentInputs.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapResidentInputs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reading the map list and term pointers of a shrinking site

Four consecutive level words give the map-count head, dense-ID table head,
term head, and term stride. Every packed site's count is its row capacity
(6dQ), so the count already read supplies the row stride. The next
fragment splits one ID into its motif and party and reads the first word
of the motif's term record, the demand-grid ordinal.


### `headerCode`

 Registers zero and one hold the old level header and packed site ordinal.
Registers two and three receive the half-open map-ID range, and four and
five the term-table base and stride. Registers eight to ten are scratch. 

### `HeaderLinked`

 The header scan is linked to the first map-list guard. 

### `count`

 The count word at this packed site. 

### `rowStart`

 First cell of this site's packed map-ID row. 

### `headerEvents`

 The header trace includes the indirect count read and the four pointer
or stride words. All reads come from the supplied external memory. 

### `HeaderFrame`

 The entry scan preserves all registers outside its seven destinations. 

### `HeaderResult`

 Cursor bounds and term lookup data actually read for the enclosing loop. 

### `header_native`

 The header fragment has fixed instruction and probe counts on all
external words, including an empty row. 

### `itemCode`

 Fetch the current map ID, divide it by six to obtain motif and party,
and read the first word of that motif's selected term. The row cursor
is advanced by the enclosing loop. 

### `ItemLinked`

 The item reader returns directly to the native motif/party dispatch. 

### `termAddr`

 The address calculated by the native division, multiply and add. 

### `itemEvents`

 The item probe sequence is independent of the entered control table. 

### `ItemResult`

 Outputs for one map, including the term-row base needed by the field reader. 

### `item_native`

 Both item probes and the complete continuation state on arbitrary memory. 

### `Published`

 The four published level fields in ordinary external-memory coordinates. 

### `Published.of_head_frames`

 The term publisher and the later data-head publisher retain the two
previously written map heads. The data-head publisher also retains both
words written by the term publisher. 

### `Published.retain`

 Later updates elsewhere in memory preserve the directory descriptor. 

### `HeaderResult.readback`

 Readback at a fitted header and count cell. Row cursor arithmetic is
word arithmetic, so the exclusive row end may coincide with the modulus. 

### `ItemResult.readback`

 On a genuine resident occurrence, native division and remainder recover
the motif ordinal and the six-valued party without truncation. The grid word
is read at the ordinary, fitted address in the selected term table. 

### `Address`

 Fixed slots occupied by both readers in the pair worker. 

### `text`

 The readers share the surrounding eleven public words and have no
private public-parameter bank of their own. Their exits link to the map
guard and selected map evaluator. 

### `linked`

 Placing the fixed instruction slots supplies both native reader links. 
