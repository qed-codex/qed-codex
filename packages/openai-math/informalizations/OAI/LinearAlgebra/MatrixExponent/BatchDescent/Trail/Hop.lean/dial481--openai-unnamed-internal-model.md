---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/BatchDescent/Trail/Hop.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/BatchDescent/Trail/Hop.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/BatchDescent/Trail/Hop.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Following original exterior stacks

A span carries a local channel and the original stack key. The
long global name of the channel is shared by every block at its host.
This record contains no values of the exterior input bits.



# Tracking the incoming exterior spans at a new host

A host receives a bounded bank of old names. Each occupied exterior
span points into that bank and selects one old span. Pointwise
preservation of offsets and widths implies preservation of entire
stacks, by injectivity of the two boundary maps.



# Candidate origin marks

An incoming channel consists of a local hop and a channel at the
corresponding previous host. Only channels used by an actual span
contribute to the bound on the number of distinct source names.


### `mark`

 Translate a short lane number to a pair of hop and lane number. 

### `Tracks.incoming`

 One original stack becomes one entire span with exactly one incoming
mark. The name may occur through different hops for other stacks. 

 # A short return hop and predecessor-span address 

 # Padding short predecessor pointers to batch-read addresses 

 # Long and short fields of an exterior-tracking step 


# Looking up a batch of incoming markers

Each bit of a translated marker is either constant or an old marker
bit. Read the resulting columns at the predecessor pointers, then
append the long names, which require no indirect reads.


 # Cost of updating long names and short marks separately 

 # Relabeling incoming spans by a compact table of distinct names 

### `Tracks.update`

 The name width is paid once per channel, independently of how
many exterior spans and blocks use it. 

 # Routing channel flags without repeating the long names per block 

 # Cost of updating long channel names and short span tags 

 # Executing a trail update simultaneously at all hosts 
