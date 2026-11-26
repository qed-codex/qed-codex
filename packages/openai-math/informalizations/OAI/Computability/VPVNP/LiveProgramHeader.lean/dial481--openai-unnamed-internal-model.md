---
{
  "module": "OAI/Computability/VPVNP/LiveProgramHeader.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramHeader.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramHeader.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Entering and leaving the header stage of the full live program

The physical machine reads the outer tag at the first address beyond its
processor array. Its header stage reserves the next address for its own
dispatcher. Every header call protects the outer tag. The accepting call
updates that tag to the mode router and resets the cursor to zero.


### `sizes`

 The concrete live header lengths obtained by evaluating the fixed size expressions at the
group geometry. 

### `base`

 Base of the header workspace, one word beyond the outer stage tag that follows the
processor array. 

### `addr`

 Word address of the outer stage tag checked and updated by the linked header program. 

### `tagFrame`

 Every continuing source call of the physical header leaves the outer
stage tag intact, for arbitrary processor and scratch contents. 

### `valid_prefix`

 The actual linked live program reaches its mode router on exactly the
deterministic header choices. The transferred memory still has the complete
header output image, and the cost includes both dispatchers. 

### `necessary`

 Any accepted path of the full live program must first accept the physical
header checks at its actual remaining source cap. 
