---
{
  "module": "OAI/Computability/VPVNP/ChainAssignments.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ChainAssignments.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ChainAssignments.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Reindexing all shared bits of the live and primed chains

Groups and cuts are indexed consecutively. A bit on an even cut is an exterior
bit of the adjacent pairs. Bits on an odd cut and the send bits of its two
groups belong to just one pair. The bijection below makes the regrouping in
(9.2)–(9.5) independent of the bit values and the site computations.


### `group`

 Identify pair `i` and side `g` with group `2*i+g` in the chain of `2^(h+1)` groups. 

### `evenCut`

 Index `2*i` of exterior cut `i` after grouping the chain into adjacent pairs, including the
two end cuts. 

### `oddCut`

 Index `2*i+1` of the cut between the two groups of pair `i`. 

### `cut`

 Partition all cuts of the unpaired chain into the even cuts bounding pairs and the odd cuts
internal to individual pairs. 

### `AllCuts`

 An assignment of a bit string of the prescribed width to each of the `2^(h+1)+1` cuts of
the chain. 

### `Shared`

 A full assignment of chain cut strings together with a Boolean value for every shared RAM
bit of every group. 

### `split`

 Each physical assignment supplies exactly one exterior assignment and one
independent internal assignment per pair, and conversely. 

### `distributedBit`

 Read an index, advice, or cut field at the site address. Unused
endpoints and addresses beyond the field length are clamped to zero. 

### `physicalHeader`

 Form processor `v`'s header for group `j` from its distributed bits of the one-based group
number, advice, and left and right cut strings. 

### `physicalInput`

 An actual tape in the unpaired chain. Consecutive groups read the same
cut field, and a receive port reads the bit of its physical send endpoint. 

### `unpaired`

 The full contraction written with one variable for each physical shared bit,
one factor per group, and one factor per site in the group. 

### `unpaired_eq_original`

 Pairing consecutive factors preserves the integer contraction. 
