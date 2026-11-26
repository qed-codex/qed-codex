---
{
  "module": "OAI/Computability/VPVNP/RAMBitTranscript.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMBitTranscript.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMBitTranscript.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Parsimonious transcripts over individual shared bits

Lemma 10.1 sums over bits on existing links. Each site parses its received
fields, checks its outgoing fields for canonical encoding, and validates its
local call reports. All accepted typed messages are representable, so replacing
whole messages by their individual shared bits preserves the path count.


### `RawAssignment`

 An assignment of one Boolean to every sending endpoint of an existing transcript link. 

### `recordPosition`

 The sorting proof numbers each site block by its logarithmic length. 

### `PackedMessages`

 Word-bounded messages with exactly the fields present in the bit layout. 

### `unpackMessages`

 Convert packed successor words and sorting blocks to chain and memory messages, widening
each present record and retaining its position. 

### `Messages.FitsWord`

 Each successor cost fits the total site budget, and every record carried by the sorting and
successor links fits the chosen word width. 

### `packMessages`

 Pack bounded chain costs, states, last records and sorting blocks into the fixed successor
and sorting message formats. 

### `messageBits`

 Encode each outgoing message independently. 

### `parseMessages`

 Parsing uses the fixed length of each field. Malformed patterns have a
candidate parse but fail the sender's canonicality check below. 

### `OutgoingOK`

 One successor-send check when that edge exists, and one send check for
each cross-site layer. Both sides inspect only the fields at the specified site. 

### `IncomingOK`

 Check the incoming predecessor field when present and the incoming
sorting blocks at their XOR partners. These checks reject malformed receives
even when evaluating a single site on an arbitrary incident bit pattern. 

### `BitValidator`

 The site validator applied to raw link bits. Missing end fields carry
zero by construction of the layout, and genuine fields use their unique source. 

### `BitJointPaths`

 Shared-bit assignments together with a list of local call reports at each site, subject to
every site's bit validator. 

### `jointBitEquiv`

 The exact bijection between accepted joint transcripts in their typed and
bit-level forms. In particular padding and clamped fields add no choices. 

### `bitTranscriptEquiv`

 Lemma 10.1's parsimonious correspondence for the exact shared-bit layout. 
