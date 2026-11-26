---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Assembly/Matching.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Assembly/Matching.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Assembly/Matching.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Local movement of thin occurrences

The column contraction moves a whole occurrence to its matched
destination if any of its outgoing rows is selected. Select one
such row from the padded array and recover the destination from
the thick mate. The row contraction leaves all occurrences in place.


### `motion_spec`

 The read address is the neighbor slot and colony key of the
specific thick mate. Inactive rows need no dummy destination. 


# Short addresses for contracted sites

A moved station specifies a neighbor index and a colony label. From the
source of an original edge, both of its new endpoint addresses are at
most two local hops away. All six gadget parties use these same addresses.


### `step`

 After the motion query, only the local label and one decision bit
are needed to determine the destination of the occurrence. 

### `Path`

 The first hop is optional. It precedes the movement of the endpoint. 

 # Computing the local movement record without long addresses 

 # Recovering the physical replacement endpoints from local records 

### `Chart`

 The encoded site name stores a host position and a local interval key. 

 # Stub and colony numbering for grouped host positions 

### `nav`

 Follow a short neighbor index, defaulting to home for an empty seat. 

 # Extracting the outgoing records from local station patterns 

 # Counting selector seats by the local mask bits 


# Candidate wires for an entire subround

A fixed bank of slots accompanies each possible old row. The forward
and reciprocal mask bits distinguish the two members of a matched
pair from an untouched unit. Test for loops after reading the addresses.


### `extract_layout`

 This version allows the host index set itself to be padded. 

 # A subround matching determined by fixed-width arrays 
