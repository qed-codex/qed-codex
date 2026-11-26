---
{
  "module": "OAI/Computability/VPVNP/RAMMemory.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMMemory.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMMemory.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Memory checks in the distributed RAM transcript

In Lemma 10.1, the guessed values of external reads are checked using only the
previous record in address-sorted order. Initialization records are writes.
The chronological semantics below leaves memory unchanged on a read, and
checks the guessed value against the actual current memory.


### `Kind`

 Memory transcript operation, distinguished as a header initialization, an external read or
an external write. 

### `Record`

 Nonempty five-word records. Padding is represented by `none`. 

### `Record.kind`

 Operation that produced this record, used to give header initialization priority over
  later probes. 

### `Record.address`

 External address to which this initialization or probe refers. 

### `Record.value`

 Word installed by an initialization or write, or the value claimed by a read. 

### `Record.startCost`

 Cumulative cost at the start of the issuing call. Initialization records use their own
  address in this timestamp field. 

### `Record.ordinal`

 Probe index within its issuing call, used with the start cost to order probes
  chronologically. 

### `Record.timestamp`

 Initialization precedes every probe. Probes are ordered by the starting
cost of their call and their ordinal within that call. 

### `Chronological`

 The order of events in the RAM computation. 

### `AddressSorted`

 Strict order of the nonempty keys in the sorted probe array. 

### `afterRecord`

 Execute one probe. A read does not modify memory. 

### `ReadsCorrect`

 Correctness of the claimed read values under ordinary sequential RAM
execution from the given memory. Writes may overwrite any previous value. 

### `previousValue`

 Previous value if the previous record addresses this cell, and zero
otherwise. This needs only the predecessor site's last record at a block edge. 

### `PredecessorCheck`

 The local predecessor test on all reads of one block. 

### `address_histories_eq`

 Sorting groups each address while preserving its complete probe history,
including intermediate reads. Strict timestamps prevent tie ambiguities. 

### `predecessorCheck_iff_readsCorrect`

 The neighboring-record tests on the actual sorted permutation accept
exactly the chronological histories whose read answers are correct. 

### `predecessorCheck_append`

 Successor messages suffice for blockwise checking, including the case
of an empty block. 

### `initRecord`

 The initialization writes specified by the headers at addresses below S. 

### `initialRecords`

 Header initialization writes for the consecutive addresses from zero through `S - 1`,
listed in address order. 

### `initialMemory`

 External memory with the supplied header words below `S` and zero at every higher address. 

### `readsCorrect_initialRecords_append`

 Processing the synthetic initialization writes installs exactly the header
memory, retaining zero on all other addresses. 

### `paddedKey`

 The nonempty key has four components: address, initialization priority,
starting cost, and ordinal. A padding record is larger than every such key. 

### `padded_predecessorCheck_iff`

 Validation after sorting and removing padding agrees with executing the
probes against the specified headers. The premises on the sort are its usual
permutation and non-strict ordering postconditions. 

### `PaddedCheck`

 The site validator scans its physical slots, including empties. Its
incoming predecessor field is the final physical slot of the preceding site. 

### `paddedCheck_iff_filter`

 In a sorted array a padding record cannot interrupt an address history. 

### `paddedCheck_iff_readsCorrect`

 Physical site checks, with actual empty slots, recover precisely the
valid RAM reads starting from the headers. 
