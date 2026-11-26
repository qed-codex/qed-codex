---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordRefreshNewSlots.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordRefreshNewSlots.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordRefreshNewSlots.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native writes of the refreshed endpoint and width tables

Each visit takes a bundle (new site) number as its persistent cursor. The bundle
order is old base vertex, port, residual lane. At a fixed local slot, one call
writes the translated incoming identifier, the inverse link and the actual
width. The expander's two fixed columns are indexed by port and expander slot.
The selected supply widths are indexed by the full site and expander slot.


### `W`

 The fixed-width machine word used for refreshed slot addresses and widths. 

### `Public`

 The thirteen public words supplying dimensions, a local slot index, and the input and
output column heads. 

### `Kind`

 The local index is zero for the external slot, an expander-edge number
for an internal slot, and a padding-copy number for a padding slot. 

### `Row`

 Columns 10 and 11 map an outgoing identifier to its incoming identifier
and vice versa. Column 12 stores the width at the outgoing identifier. 

### `Row.src`

 Packed outgoing slot identifier for this incidence row. 

### `Row.dst`

 Packed incoming slot identifier at the opposite end of this incidence row. 

### `Row.width`

 The word encoding the number of bits carried by the arc. 

### `Row.update`

 Write the two directed mate links and the outgoing width for the row. 

### `row`

 Read the dimensions, target/total arrays, fixed expander and selected supply
tables. Arithmetic is word arithmetic, including the cyclic padding rotation. 

### `decode`

 Load the base vertex (register 4), port (5), and lane (6) from the site cursor. 

### `restore`

 Register 5 now carries the target port. Restore the target site (register 2)
while preserving the lane. 

### `code`

 Fixed tables of instructions. Public words 0–4 give the port count,
expander degree, new degree, residual lane count and the local copy index.
Words 5–9 give bases of the external target, external total, expander target
port, expander reverse slot and selected supply width arrays. Words 10–12
locate the forward link, inverse link and width arrays. 

### `events`

 The native read and write events for one external, expander, or padding slot at the current
site. 

### `native`

 One native call from fresh private memory, including its full event sequence. 

### `written`

 Read back the two endpoint links and the width after this native call.
The inequalities separate the three actual output cells, including at loops
of the numerical permutation. 

### `sites`

 The external directory enumerates the base arc before the residual lane. 

### `arcs`

 The endpoint identifiers range bijectively over the refreshed half-slots. 

### `word`

 Embed a numerical array index into a word. 

### `bundleOrder_sites`

 With product-order base slots, the binary directory and new slots have
identical site numbers. 

### `Dimensions`

 Public constants common to the three scans. The whole interval of output
half-slot identifiers fits in the address word. 

### `Represents`

 Equality with the numbered graph record before writing the three cells. 

### `external_record`

 The translated target directory and the computed prefix total are the two
input words of the external-slot visit. 

### `expander_record`

 A RAM visit reads the matching reverse port and reverse slot from the fixed
expander, and the selected width from the current term's supply table. 

### `padding_record`

 Padding preserves the local copy number, advances the port modulo the old
degree at the same vertex and lane, and emits the zero-width row. 

### `actual_record`

 The identifiers stored by any of the three verified visits give precisely
the actual matching and width, including the incoming slot number. 

### `chosen_expander_record`

 The expander visit applies also to the explicit supply lengths of a
term admitted by the block reader, including its selector fields. 

### `external_terminal_record`

 The two input words of the external-slot writer come directly from the
terminal memory of the external segment pass. 

### `Column`

 The three output words of a visit. 

### `Row.address`

 Select a row's write address, indexing the incoming column by destination and the other two
by source. 

### `Row.value`

 Select the row value to store in the outgoing-mate, incoming-mate, or width column. 

### `inputs`

 All read addresses are determined by the cursor and the public words. 

### `expected`

 Expected record at a source site, calculated in the input memory. 

### `PassLayout`

 Output words of different rows and columns have distinct addresses. They
are disjoint from all inputs of the pass. 

### `Prefix`

 Every visited row is complete. Every memory word outside the visited
output cells has its original value, including words beyond the RAM range. 

### `probeCount`

 Probe count of a native visit, before adding its call boundary. 

### `kindOf`

 Choose the native table for each slot class. 

### `slot_cost`

 Summing the full-pass costs over the numbered local slots counts each
expander and each padding copy separately. 

### `scan_run`

 All calls for one fixed local slot, starting at any already completed prefix. 

### `full_pass`

 From arbitrary initial memory, one complete native pass produces all
forward and inverse links and widths for its slot and preserves every other
cell. This costs six, seven or four per site, according to the slot class. 

### `PassLayout.ofActual`

 For a fixed local slot, injectivity within each physical column follows
from the permutation of actual lifted half-slots. This also covers parallel
expander edges. Only the separation of input and output arrays and of distinct
output columns needs to be supplied by the address layout. 
