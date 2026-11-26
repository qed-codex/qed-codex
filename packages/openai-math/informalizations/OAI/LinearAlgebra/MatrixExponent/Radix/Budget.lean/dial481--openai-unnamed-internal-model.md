---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Radix/Budget.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Radix/Budget.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Radix/Budget.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Packing a stable local sort

The ordered prefix consists, for each digit, of its real rows followed by a
full pack of blanks. Thus even an unaligned pack contains at most one real
digit. At most one live pack extends past this prefix.


### `group_prefix`

 Read the least keys one at a time, leaving all larger keys as a tail. 

### `packing`

 Local stable sorting with P delimiters per digit isolates all digits in
the output packs. Only packs overlapping the real-key prefix can be live. 


# Stable sorting with tagged permutations

Label each record by its input position. Compare by digit, then by
position. A final comparison by record makes the order total even
outside the set of correctly labelled records.



# Sorting packs and discarding the empty tail

All records in a nonempty pack agree on their digit. Stability on packs
therefore preserves order within each digit at the level of records.


 # Reading the digit of a pack in linear time 

 # Crossing a block boundary without permuting the records 

### `Blocked`

 A partial pass before sorting the packs. The additional space for
separators is charged once per input block. 


# A local radix pass

Double the number of slots and fill the new half with separators.
Stable sorting by the augmented key leaves enough empty slots between
digits to make each pack homogeneous.


 # Cost allowances for a radix pass and all passes combined 


# A radix pass at fixed capacity

Half the slots are reserved for padding. All blocks are processed
independently, then a single stable sort reorders their packs. If the
number of packs per block is at least four times the digit alphabet
size, the trailing half is entirely empty and can be discarded.


 # Cost of verifying an ordinary tagged permutation by radix sorting 
