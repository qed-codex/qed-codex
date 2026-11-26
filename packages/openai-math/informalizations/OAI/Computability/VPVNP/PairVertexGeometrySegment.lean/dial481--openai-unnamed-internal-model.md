---
{
  "module": "OAI/Computability/VPVNP/PairVertexGeometrySegment.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairVertexGeometrySegment.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairVertexGeometrySegment.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Installing the combined geometry and cache in the terminal vertex image

The segment uses the caller's saved header, role, and histogram registers.
Its two instruction ranges and its two private register ranges are disjoint.
Renaming the arithmetic and operand flows preserves both instruction counts.


### `frameCount`

 Geometry instruction count before relocation. 

### `cacheCount`

 Instruction count of the finite cache computation and its 38 stores. 

### `count`

 Total number of program-counter slots used by the geometry segment. 

### `regs`

 Size of the segment's private register bank. 

### `workBank`

 The first 24 private registers, used by the geometry reader. 

### `cacheBank`

 Private registers following the geometry reader's register bank. 

### `text`

 Two-bit opcodes are padded to the vertex image's five-bit literal type. 

### `segment`

 Geometry component installed between the ordinal guard and the root gather. 

### `bankFor`

 The combined geometry and cache registers in the actual linked vertex image. 

### `labelsFor`

 Locate a geometry opcode in the enclosing vertex program. 

### `placedBlock`

 Construct the native initialization block from disjoint saved and private registers. 

### `block`

 Initialization block with the actual caller's header, role and histogram registers. 

### `placement`

 Physical address of an instruction in the combined native block. 

### `ret`

 Unconditional jump from the last cache instruction to the root-field gather. 

### `linked`

 Actual opcode at every geometry and cache PC in the full linked image. 
