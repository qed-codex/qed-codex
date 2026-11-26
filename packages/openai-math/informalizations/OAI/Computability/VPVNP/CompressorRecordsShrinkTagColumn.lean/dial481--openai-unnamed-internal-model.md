---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsShrinkTagColumn.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsShrinkTagColumn.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsShrinkTagColumn.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Extracting the shrinking tag increments from the displacement column

Before the greedy tag scan, each base port contributes the tag component of its
old displacement. The worker skips the residual lane bits by division, takes
the low tag bits, and writes a separate column in base-port order. A final call
initializes the zero operand used for absent increments.


### `publicWords`

 Both workers use the same frame throughout the two phases. 

### `params`

 Build the workers' shared parameters from the incidence displacement column, tag
destination, zero cell, residual-lane radix and tag radix. 

### `extractOps`

 Read one base port's displacement, divide out its residual lane, write the remaining low
tag bits, and advance the port cursor. 

### `zeroOps`

 Write zero to the operand cell used for absent tag increments and set the return cursor to
one. 

### `extractPass`

 The scheduled worker that extracts one tag increment from the displacement column per call. 

### `zeroPass`

 The scheduled worker that initializes the absent-increment operand after the tag extraction
scan. 

### `cell`

 Natural address of an indexed column entry, obtained by adding its index to the base in
word arithmetic. 

### `extract`

 Recover the displacement's tag component by dividing by the residual radix and reducing
modulo the tag radix. 

### `row`

 Report for one port visit, recording the displacement read, tag increment write, and next
cursor. 

### `zeroRow`

 Report of the final zero-initialization call, with one external write and return cursor
one. 

### `scan`

 Reports from the actual, successively updated external memory. 

### `reports`

 The reports for all base ports in order starting at zero, followed by the report that
initializes the zero operand. 

### `Regions`

 The shift columns do not overlap. The final zero cell is distinct from
all populated output rows. 

### `Result`

 Complete native execution, memory contents, and external charge of the two phases. 

### `packedTagNumber`

 The tag is the binary field directly above the residual lane. 

### `extract_directory`

 The emitted increments are exactly the tag fields used by the ordered
shrinking construction, with an initialized external zero operand. 

### `InColumn`

 The actual word addresses used by an indexed column, including wrapping heads. 

### `scan_footprints`

 The shift scan reads only old base displacements and writes only extracted tags. 

### `zero_footprints`

 The zero initializer has no read dependency and writes just its own cell. 

### `scan_valid`

 The installed frame stays ready through all rows and the final cursor closes the worker. 

### `zero_valid`

 Guard and frame correctness of the single zero write after the shift scan. 
