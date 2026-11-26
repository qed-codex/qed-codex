---
{
  "module": "OAI/Computability/VPVNP/PairRefreshDiagonal.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairRefreshDiagonal.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairRefreshDiagonal.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Testing the two diagonal ties in a refresh kernel

At a port the outgoing old half is compared to its outgoing external
segment, and the incoming external segment to the incoming old half. The
widths of these two comparisons can differ. Both use the same discrepancy
mask, so success means every bit of both ties agrees.


### `loopRegs`

 Embed the seven bit-comparison loop registers into the ten registers of the two-sided
diagonal test. 

### `control`

 Registers 0,1,2 give the first left cursor, exclusive left end and
right cursor. Registers 7,8,9 give the second triple. 

### `Linked`

 The installed control code links the two comparison scans to their return labels before
branching on the accumulated mismatch flag. 

### `Pointers`

 Private starts of the two old halves and their corresponding external
segments. The lengths belong to the original, independent half-wires. 

### `Pointers.oldOut`

 Private start address of the old outgoing half-word. 

### `Pointers.externalOut`

 Private start address of the outgoing segment against which the old outgoing half is
  checked. 

### `Pointers.oldIn`

 Private start address of the old incoming half-word. 

### `Pointers.externalIn`

 Private start address of the incoming segment against which the old incoming half is
  checked. 

### `Pointers.Ready`

 Register layout at entry to the two diagonal scans. 

### `Tie`

 A pair of equally long bit fields in private memory. 

### `Tie.left`

 Private read cursor for the original half-word in this diagonal tie. 

### `Tie.right`

 Private read cursor for the segment paired with that half-word. 

### `Tie.oldBits`

 The independent bits of the original half-word that the comparison must read. 

### `Tie.segmentBits`

 Bits of the selected segment that are compared with the corresponding old half-word. 

### `Tie.resident`

 Both private ranges contain the encoded bits specified for this tie, in increasing bit
order. 

### `compare`

 Execute both comparisons, even if the first one fails. The input may
contain any independent old and new halves, including empty fields. 

### `label`

 The concrete instruction layout. The first two labels are the accepting
and rejecting exits. The three seven-instruction blocks are control and the
two private array comparisons. 

### `table`

 Resizable 23-instruction diagonal test with two seven-instruction bit scans and distinct
accept and reject exits. 

### `compare_portDiagonal`

 Specialize the physical comparison to the two actual diagonal demand
coordinates of the refresh kernel. The ordinary port map is entered exactly
when the integer diagonal multiplier is one. 
