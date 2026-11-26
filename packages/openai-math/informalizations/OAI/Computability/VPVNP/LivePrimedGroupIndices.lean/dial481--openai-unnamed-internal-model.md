---
{
  "module": "OAI/Computability/VPVNP/LivePrimedGroupIndices.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LivePrimedGroupIndices.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LivePrimedGroupIndices.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Preparing the two primed group indices

In Section 14.1, a first-half live group numbered `i` supplies the auxiliary
machine with two little-endian indices. Their low bits are one and zero. The
remaining bits represent `i - 1` and `i`. Each digit call propagates a
single borrow through external scratch, even when the index exceeds a RAM word.


### `borrow`

 The borrow entering digit `j` in the subtraction `i - 1`. 

### `borrow_endpoint`

 In the last group the scanned low digits are all zero and subtraction
still carries its borrow. In every earlier group the borrow has cleared. 

### `setup`

 Public words give the input base, left and right output bases, and the
borrow address. The initialization sets both low bits and starts the borrow. 

### `initialized`

 Set the low bits of the left and right primed indices to one and zero and initialize the
borrow for subtracting one from the live group index. 

### `digit`

 Both reads precede the three writes. Register 9 receives the new
borrow, register 10 the bit of the predecessor, and register 11 the next cursor. 

### `updated`

 Store the next digits of the two primed indices, using the incoming borrow for the left
digit, and propagate the new borrow. 

### `initialize_native`

 A native initialization call takes three probes and returns cursor zero. 

### `digit_native`

 Executing the same fixed table at every digit takes five probes. 

### `outside`

 Addresses outside both output arrays and the scalar borrow cell. 

### `Layout`

 All array addresses fit and writable regions are disjoint. Bases can
occur in any physical order, and unrelated scratch may surround them. 

### `stores`

 Each address holds one unpacked bit of a little-endian integer. 

### `storedBits`

 Read an unpacked array as a little-endian bit string. 

### `stores_value`

 The decoded value uses arbitrary natural-number precision, independently of
the width of a single RAM word. 

### `pair_values`

 Both output integers fit even when doubling sets a new high bit. 

### `Invariant`

 After processing `j` digits, the two output prefixes store the low `j + 1` bits of `2*i -
1` and `2*i`, the borrow cell is current, and memory outside the workspace agrees with its
initial contents. 

### `native`

 One setup call followed by `h` deterministic digit calls gives the exact
`h+1` output bits, clears the borrow, and preserves every other memory cell.
For the middle live group the right array includes the high bit of `L`. 
