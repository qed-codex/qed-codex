---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Transcript/Route/Restore.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Transcript/Route/Restore.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Transcript/Route/Restore.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Numbering within capacity buckets

The decoder at a bucket first range-checks the index, then reads
the entry at that rank in the ordered list for the bucket.


### `ranked`

 A deterministic ordinal per bucket. 


# Named chains of equalities

Each free bit has a distinguished root. All positions must be connected
to their named source and no equality may connect different names.
Redundant checks and changes of edge orientation are harmless.


### `contract`

 Internal summation over physical tape bits is exactly summation
over the independent roots. 

 # Transporting diagram ports on a fixed private tape 

### `Route`

 Taps name physical bit positions. The origin of each must be the
specified exterior bit or internal edge of the diagram. 


# A single dictionary for a whole family of station tables

Use the left-to-right order of the named bit positions. The
argument length is exactly the label length plus the station arity.


### `Dictionary`

 Valid labels need only distinguish different station tables. 


# Ordered bundles at a station

Positions use the left-to-right order of the incoming and then
outgoing ports. An internal bundle occupies a contiguous interval
at each end. Exterior positions may have arbitrary global names.


### `portPeer`

 Side of the local port and, for an internal edge, the remote
station and the offset on the opposite side of that station. 

 # Source offsets in ordered runs of parallel wires 

### `wireAt_next`

 On adjacent ports within an ordered block, the side stays fixed
and the source offset of an internal wire advances by one. 

### `endAt`

 All indexed positions, including both ends of a loop, are distinct. 

 # Exterior names in station port order 

 # Reading a table from local labels and its two exterior strings 

### `restore`

 A tagged position reads an internal bit. An untagged position
consumes the next exterior bit on its side. 
