---
{
  "module": "OAI/Computability/VPVNP/RAMSortDecodeCost.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMSortDecodeCost.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMSortDecodeCost.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Word work to decode a sorting record

The validator of Lemma 10.1 receives five little-endian words per record. The scan below
visits the most significant remaining bit, doubles the accumulator, and adds the bit.
The decoder retains the five results, parses their tag and checks the resulting canonical
words. Its bound applies to every bit field, including unknown tags and malformed padding.


### `scanFrom`

 The first component is the decoded value. The second counts word operations. At each
bit charge the loop test, decrement, offset arithmetic, bit load, doubling, addition and
loop branch. Offset arithmetic has two operations, giving eight in total. The final zero
counter test costs one. 

### `scan_digit_fits`

 After `w-k-1` bits, doubling the accumulator and adding a bit fits in `w-k` bits.
Thus all intermediate results of the scan from zero fit in a single `w`-bit word. 

### `scanWord`

 Decode a word once. Charge the initialization of the cursor and accumulator. 

### `parseSaved`

 Read the tag register, compare against up to three known tags, and copy four
payload registers into the parsed record. Each failed comparison costs a compare and a
branch. Unknown tags reach the empty-record candidate and are checked below. 

### `checkPrefix`

 Check canonical fields from the highest remaining register downwards. A failed word
comparison exits immediately. Charge the loop test, decrement, two loads, equality and
branch on each iteration, and one test for an empty prefix. 

### `readField`

 The `5*w` physical bits split into five successive word streams. 

### `decodeSlot`

 Scan the five words into registers and run the tag and canonical-field checks.
In addition to their measured costs, charge five register writes, ten operations for
dispatch and writing the five canonical words, and two for the final branch and return.
`some none` is the canonical empty record, and `none` rejects. 

### `decodeSlot_eq`

 The bounded decoder and the message format agree for every input bit string. 
