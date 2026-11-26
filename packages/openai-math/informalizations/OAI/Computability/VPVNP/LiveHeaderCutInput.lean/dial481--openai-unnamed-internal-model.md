---
{
  "module": "OAI/Computability/VPVNP/LiveHeaderCutInput.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderCutInput.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderCutInput.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native readback of the two incident live cuts

The incoming cut at a group is its preceding cut and the outgoing cut is
its following cut. A copy interval reads the corresponding slot of the
original physical processor header and writes one encoded bit per word.
The same physical readback identifies the native padding guard with the
canonical zero padding of each typed layout.


### `cutSlot`

 The two incident cut slots in the four-bit processor word. 

### `incidentCut`

 Index of the physical cut shared by consecutive groups. 

### `SiteHeaders`

 The processor sites still contain the original packed headers at this
point in the computation. Scratch memory is allowed to contain live data. 

### `CopiedSlice`

 The exact original cut bits at consecutive scratch addresses. 

### `FieldCopy.physical`

 Interpret a completed copy, including one performed by a fixed-capacity
runner, in terms of the group cut supplied to the contraction. 

### `physical_copy_native`

 Execute the native bit-copy table with the descriptor installed in
memory. The same reports give the typed readback and preserve every site. 

### `SiteHeaders.zeroSlice`

 Exact interpretation of the padding reads. An interval with no sites
imposes the empty conjunction. 

### `physical_padding_native_iff`

 Native success on arbitrary physical cut input is equivalent to the
mathematical zero-slice condition. 

### `physical_padding_native`

 A physical zero slice gives a complete native padding trace with
unchanged memory and the prescribed probe bound. 

### `CopiedSlice.congr`

 A scan of a disjoint buffer preserves bits copied by an earlier scan. 

### `ExponentWords`

 The flat scratch buffer consumed by the exponent stage. 

### `CopiedSlice.pair_exponents`

 The exponent block has one scratch word per bit, in label-major order
and little-endian order within each label. 

### `CopiedSlice.pair_exterior`

 Exterior bits in the auxiliary primed group header. 

### `CopiedSlice.tail_config`

 The exact canonical serialized evaluator configuration at a tail cut. 

### `first_incoming_exponents`

 No incoming exponent field exists in the first group. Its dedicated
scratch starts with the little-endian representation of all-zero exponents. 

### `ExponentWords.congr`

 Keep an already decoded exponent vector through a later phase that
preserves its scratch interval. 

### `exponentBufferValues`

 The input hypothesis of the native exponent checker follows from the
two physically decoded exponent arrays, including the zero endpoint. 
