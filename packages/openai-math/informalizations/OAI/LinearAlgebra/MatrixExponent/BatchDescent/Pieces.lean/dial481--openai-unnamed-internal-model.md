---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/BatchDescent/Pieces.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/BatchDescent/Pieces.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/BatchDescent/Pieces.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Packing port and table rows

Keep a tuple of size at most `u` intact by assigning it to the row of
its first slot and allowing `2*u` slots per row. Both coordinates use
prefix sums. The same construction packs whole positions into bins.


### `row`

 The last row is always available, even for an empty trailing tuple. 

### `Lengths`

 Occurrences are indexed first, incident ports second. 

### `counts`

 Row reservations for each position include a spare row. 


# Common bins for the two endpoint orders

The table rows, port rows and spare row of one position all occupy
the same bin. Slots in each order are injectively placed, so a bit
assignment can be transferred between orders without duplication.


### `rank`

 The ordinal in the list at one port, independent of its row address. 

 # The anchor of a position and its consecutive port headers 

### `anchor`

 A header for the entire position fits in the first half of its bin. 

### `portAnchor`

 The port headers use distinct consecutive slots in the same bin. 


# Reassembling port rows into table rows

Each bin holds rows indexed by `R`, with slots indexed by `S`. Split
each slot into `R` pieces with bit positions `P`. A slice takes one
piece from every slot of every row, so it has the width of one row.
The same list of sources determines the rearrangement in each slice.


### `Bins`

 A common routing dictionary and a common table dictionary. Taps
may read any exterior or private position of a larger transcript. 

### `reassemble`

 All slices are checked in one batch. The second batch multiplies the
entries for the resulting rows, with no restriction on the entries. 


# Descriptions of packed table rows

A bin stores a one-hot map from table sockets to port sockets. A row
stores the presence bit, label and argument positions of each occurrence
there. These descriptions contain no payload bits. An unused argument
is read as zero, and an arity-zero occurrence still contributes its entry.


### `padded`

 Reindex a tuple of active slot payloads; fill the other entries with zero. 


# Ordered spans as bundles

All spans at an occurrence split into pieces of a common width. A
numbering of those pieces depends only on the short pattern label.
It is independent of the rest of the host and of the row allocation.


### `value`

 One label describes all stations at an occurrence. 

 # Local description of a bin, independent of host and bin identifiers 

### `binFunction`

 The query only inspects descriptors with their validity flag set. 

 # Generating the two socket orders and the local controls from bin keys 

### `binTransform`

 One dictionary handles every physical bin. No host or bin number
is included in its key. 
