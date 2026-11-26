---
{
  "module": "OAI/Computability/VPVNP/LiveHeaderPhases.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderPhases.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderPhases.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Live group flags computed from the scanned header

The live program tests whether it is at the first group, at the midpoint,
in the first half, or at the last group. Each test uses the scanned high
bit position and population count. The tests also apply when the first
group is the midpoint.


### `Flag`

 The first-group, midpoint, first-half, and last-group predicates computed from the
one-based index. 

### `Flag.holds`

 Evaluate a phase flag against a one-based group index and the chain's height. 

### `allOnes`

 The complete scanned prefix is the finite set of binary positions. 

### `firstTail_iff`

 In the nondegenerate case, the first tail index has precisely bits
zero and `h` set. The low bit distinguishes it from other tail indices
of population two. 

### `setup`

 The public parameters locate the two index-scan words and the destination. 

### `dispatch`

 Select the native comparison and Boolean store that implement the requested phase flag. 

### `block`

 Load the scanned index summary and execute the test for the requested group flag. 

### `Writes`

 A successful flag write after at most three conditional instructions. 

### `block_exec`

 A deterministic native flag computation on the output of the index scan.
Its two reads and one write take at most thirteen instructions including tests. 

### `lowLoad`

 The first tail group needs the low bit as well as the high position and
population. Its low bit is at the base of the copied index array. 

### `firstTailBlock`

 Load the index summary and low digit to test whether this is the first group after the
midpoint. 

### `firstTail_exec`

 The group after the midpoint alone is designated for initialization.
This test covers the two-group chain and reads a total of three scratch
words before writing its decision. 

### `scanned_width_exec`

 Direct composition with the two summary words of the header scan. 
