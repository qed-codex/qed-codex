---
{
  "module": "OAI/Computability/VPVNP/RAMTapeBoundaryBits.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeBoundaryBits.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeBoundaryBits.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Bit-by-bit checks of adjacent RAM records

Two equal-width physical records are scanned together, from low to high bit
within each of the five fields. The finite control recognizes the tag, tracks
address and value equality, and tests the current value for zero. The same
scan also tests complete-slot equality for an outgoing message.


### `TagPhase`

 Position in the tag scan, distinguishing the low bit, second bit, and remaining high bits. 

### `Flags`

 Finite summary of the two tags, field comparisons, and zero test accumulated while scanning
adjacent records. 

### `Flags.phase`

 Position of the next tag bit in the low, second, or high part of the word. 

### `Flags.prevUsed`

 Running test that the predecessor tag denotes an occupied slot. 

### `Flags.currUsed`

 Running test that the current tag denotes an occupied slot. 

### `Flags.currRead`

 Running test that the current tag denotes a read. 

### `Flags.addressEq`

 Whether all address-bit pairs compared so far agree. 

### `Flags.valueEq`

 Whether all value-bit pairs compared so far agree. 

### `Flags.currZero`

 Whether every current value bit examined so far is zero. 

### `Flags.allEqual`

 Whether every pair of record bits examined so far agrees. 

### `initial`

 Start at the low tag bit with empty comparisons and zero tests satisfied. 

### `stepField`

 One physical bit pair. After the first two tag bits, any set bit makes the
corresponding tag invalid. This requires only three phases for every width. 

### `step`

 Update the boundary flags from one pair of bits at the given field index. 

### `foldWord`

 Fold a paired-bit update over two words until either stream ends. 

### `foldField`

 Compare the bits of a single field using its field-specific flag update. 

### `foldFields`

 Scan the specified field indices in order, passing each comparison’s flags to the next. 

### `recordWords`

 The five fields of a physical slot, each encoded as a low-bit-first word. 

### `foldRecord`

 Compare two complete physical slots from the initial flags in field order. 

### `checked`

 Accept a read if its value matches an occupied predecessor at the same address, or is zero
when there is no such predecessor. 

### `equalChecked`

 For an occupied predecessor require complete record equality. For an unused predecessor
require an unused current slot. 

### `checked_foldRecord`

 For arbitrary tuples, the read flag is precisely the word validator's decision. 

### `equalChecked_foldRecord`

 Complete-slot equality ignores the payload when both tags parse as empty. 
