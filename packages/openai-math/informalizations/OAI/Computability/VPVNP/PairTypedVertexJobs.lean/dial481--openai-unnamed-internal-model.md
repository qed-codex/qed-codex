---
{
  "module": "OAI/Computability/VPVNP/PairTypedVertexJobs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTypedVertexJobs.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTypedVertexJobs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Half-wire packets in the selected vertex traversal

At a visit the input packet names the current row and contains its actual
outgoing and incoming half-wire bits. Its children receive the old halves
chosen by this occurrence, in placement-fiber order. Running the resulting
jobs in preorder consumes the root and preserves every pending suffix.


### `TypedVertexJob`

 A visit guesses all child half-wires before reading the local kernel bits.
At a cursor leaf, the local bits are the original validator's private choices. 

### `TypedVertexJob.input`

 The pending input packet consumed by this typed vertex job. 

### `TypedVertexJob.children`

 Child argument packets produced by the job in the order expected by the DFS traversal. 

### `TypedVertexJob.localBits`

 Additional choice bits consumed locally by this job after its children's argument fields. 

### `TypedVertexJob.increment`

 Histogram increment per parameter label contributed by this typed vertex job. 

### `TypedVertexJob.erase`

 Erase the packet types to a plain vertex job while preserving the input node, concatenated
child and local bits, and label increments. 

### `PacketVisits`

 Consume the packet at the head of the frontier and prepend that visit's
child packets. Equality of packets includes every bit of the old half-wires. 

### `PacketVisits.pending_sublist`

 Every currently pending packet occurs in order among the unvisited jobs
and the untouched final suffix. 

### `StoredVisits`

 Readiness of the typed inputs before the corresponding native updates. 

### `PacketVisits.WritesAgree`

 A hook may change any other private cells. Its updates agree with the
child writes precisely on the intervals that are live after each visit. 

### `PacketVisits.preparedAlong`

 The native update reads the exact input at every job and preserves the
stored values of all pending siblings, including the final suffix. 

### `TermParsers.halfBits`

 Encode one old vertex's half-wires in the term parser's slot order. 

### `TermParsers.childPackets`

 A packet for each old site in this particular placement fiber. The halves
in the packet are those selected by this visit's placed assignment. 

### `TermParsers.childPackets_state`

 For a state-indexed term parser this is the private arena's outgoing-then-
incoming bit layout, with each incoming width taken at its matched source. 

### `TypedJobsFor`

 The supplied bits at the root of a subtree come from the parent or from the
shared final wires. All internal packets are constructed from the selected halves. 

### `lastRowAddresses`

 Addresses of the last selected rows, including the zero-step case. 

### `typedVertexJobs`

 Construct the selected branch's typed vertex jobs by composing the cursor leaf jobs with
all scheduled term layers and their row pointers. 

### `selectedTypedJobs_prepared`

 With the actual stage-row addresses the native readiness theorem needs
only disjointness from the externally supplied suffix. Within the selected
tree all row addresses are distinct by the placement partition. 

### `selectedCursor_typedJobs`

 The final network supplies one common payload per edge. Each final
site starts with its actual packed halves, and thereafter each child uses
exactly the old halves its own parent guessed. 
