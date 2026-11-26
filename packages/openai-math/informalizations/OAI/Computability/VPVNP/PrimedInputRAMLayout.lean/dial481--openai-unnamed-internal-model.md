---
{
  "module": "OAI/Computability/VPVNP/PrimedInputRAMLayout.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMLayout.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMLayout.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The rectangle of primed input positions

Sections 9.2 and 11 fix two consecutive groups with the same literal program
prefix. Every row of the rectangle consists of that prefix, the site address,
four header and cut bits, the incident ports, and zero padding. Only a middle
cut bit at the first group or an existing send port is a branch location.


### `Lengths`

 Lengths of the pair's supplied header arrays. 

### `Lengths.index`

 Number of bits in the index of each of the two consecutive groups. 

### `Lengths.advice`

 Number of advice bits supplied in the pair's common header. 

### `Lengths.leftCut`

 Number of supplied cut bits on the incoming side of the first group. 

### `Lengths.middleCut`

 Number of shared cut bits chosen between the first and second groups. 

### `Lengths.rightCut`

 Number of supplied cut bits on the outgoing side of the second group. 

### `Lengths.cutCapacity`

 Number of header words reserved for each of the left and right cut arrays. 

### `Header`

 Public fixed offsets of one-bit-per-word header fields. 

### `Header.count`

 Size of the reserved header in words. Three cut lengths precede two group indices, the
advice and two outer cut arrays. 

### `Header.address`

 Physical word address of a supplied header bit, using one word per bit and the reserved
stride between the outer cuts. 

### `Internal`

 Index a complete internal assignment, allowing every value on all
directed transcript bits as well as on the middle cut. 

### `Site`

 A site in the pair of primed groups, identified by its group and its `r`-bit site index. 

### `Field`

 The five parts of a row, in the paper's order. 

### `Cell`

 One bit position in the input rectangle, specified by a group, a site and a field within
that site's row. 

### `fieldIndex`

 The position within a row has exactly the arithmetic offset obtained by
concatenating its fields. 

### `cellIndex`

 Row-major flattening for the two groups, all their sites and all their
bit positions. 

### `Ref`

 Prefix and address are private literals. The only external probes in a
row position are a prescribed header read or a read at a chosen endpoint. 

### `headerRef`

 Resolve the four bits following the address. Beyond a supplied field's
length the bit is a literal zero. 

### `cellRef`

 Resolve a row bit to a literal, a supplied header bit or an internal shared bit. Padding
and missing ports resolve to zero. 

### `Ref.value`

 Read the Boolean value of a row reference using the supplied header and the assignment to
internal bits. 

### `cellOwner`

 Only the outgoing middle-cut slot of group zero and existing send slots
are visited as binary branches during the first pass. 

### `ownerEquiv`

 A bijection, including multiplicities, from the bits in (9.4) to the
exact cells where the first-pass RAM makes a branch. 

### `chosenAddress`

 Physical cell that stores one chosen bit, for second-pass random access. 
