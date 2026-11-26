---
{
  "module": "OAI/Computability/VPVNP/RAMSerialization.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMSerialization.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMSerialization.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Binary messages of the RAM transcript

Lemma 10.1 sends an eight-word successor message and a block of `4H`
five-word records at each cross-site sorting layer. Each word occupies exactly
`w` bits in little-endian order. The parsers below decode fixed-size fields and
check the input against the canonical encoding. This rejects unknown tags,
nonzero padding, and nonzero state fields for halted calls.


### `wordBits`

 Least significant bit first. 

### `arrayBits`

 Concatenate `k` fixed-width words in their given order. 

### `WordRecord`

 Natural-valued records from the trace, with their word range enforced
for all three counter/address fields. 

### `WordRecord.kind`

 Whether this serialized record describes initialization, an external read, or an external
  write. 

### `WordRecord.address`

 External word address of the recorded initialization or probe. 

### `WordRecord.value`

 Word initialized, returned by a read, or supplied to a write. 

### `WordRecord.startCost`

 Word-sized start-cost field used with the ordinal to order probes from the same address. 

### `WordRecord.ordinal`

 Word-sized ordinal giving a probe’s position among the external accesses in its call. 

### `WordRecord.record`

 Widen the address, start cost, and ordinal to natural numbers to obtain the memory record
used by the ordering and read checks. 

### `WordRecord.ofRecord`

 Convert a memory record to word fields using bounds on its address, start cost, and
ordinal. 

### `Format`

 A fixed-length word format with a left inverse. On arbitrary bit strings the
public decoder checks that re-encoding reproduces every bit. 

### `Format.words`

 The fixed array of width-w words that canonically represents a message. 

### `Format.parse`

 Recover a candidate message from a fixed word array, with exact recovery on arrays
  produced by the encoder. 

### `Format.encode`

 Concatenate the message’s word fields in order, with each field written least significant
bit first. 

### `Format.decode`

 Parse the input bits as a word array and accept the resulting message exactly when
re-encoding it reproduces the input. 

### `Format.canonicalEquiv`

 The valid binary patterns are in bijection with the typed messages. 

### `recordFormat`

 `(kind, address, value, start cost, ordinal)`. The all-zero tuple alone
encodes the empty record. The other tags are 1 for init, 2 for read, 3 for write. 

### `Format.replicate`

 Consecutive copies of the same format. Each record occupies its own
complete five-word interval in a sorting block. 

### `blockFormat`

 Format for a sorting block of 4H slots, each occupying five words and holding either a word
record or canonical padding. 

### `narrowSlot`

 Narrow a padded slot once its three natural-valued fields have been
checked against the word width. 

### `decodeBlock`

 Decoding a block produces the same padded-record type that the network sorts. 

### `decodeBlock_iff`

 Every representable sorting block has just one accepted bit pattern. 

### `permuted_block_encoding`

 In a capped run the representability condition follows from membership
in the padded input array. It therefore holds in every permuted intermediate
sorting array. 

### `word_capacity`

 The paper sets `w = (r+10)^4`, where `r = B ⌈log₂ n⌉`. A polynomial
site/call budget gives `d+e = log₂ (SH) ≤ K(r+1)` for some fixed `K`.
Already at `r+1 ≥ K`, all four tags and the final cost `SH` fit. 

### `Successor`

 The status distinguishes a running state word from an accepted halt.
The actual cumulative cost may equal the global cap. 

### `Successor.state`

 Persistent word passed to a running successor, or the empty option for an accepted halt. 

### `Successor.cost`

 Cumulative cost transmitted across the site boundary, bounded inclusively by the global
  cap. 

### `Successor.lastRecord`

 Last padded slot of the sender’s sorted block, transmitted for the predecessor check
  across the site boundary. 

### `successorFormat`

 `(status, cost, state)` followed by the last sorted record. Status 1 means
running and 2 means accepted. On a halt the state word is zero. The whole cost,
including a final cost exactly `SH`, fits when `SH < 2^w`. 

### `clamped_successor`

 The prescribed all-zero end field cannot be misread as a successor
message. A validator handles the boundary locally using its site identifier. 
