---
{
  "module": "OAI/Computability/VPVNP/CompressorDescriptorSpace.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorDescriptorSpace.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorDescriptorSpace.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Descriptor addresses across compressor levels

Appendix E uses a fixed number of words per slot and position. We allocate
the controller header, its active frame and its directory first. Each level
then has a persistent header, six packed incidence columns, and rectangular
tables of fixed-width slot records. The old levels remain addressable
after the next level has been written. The initial column addresses agree
with the native cursor scan. Both exclusive cursors and addresses fit a
machine word throughout the logarithmic block schedule.


### `Shape`

 Fixed record dimensions of the program. A directory can contain both
whole-level passes and site-specific rows. The native workspace reserves
the runtime level stride immediately after the active frame. 

### `Shape.arity`

 Number of parameter words in the planner's active frame and in each directory row. 

### `Shape.initialRows`

 Number of directory rows reserved for initialization before any per-level visits. 

### `Shape.levelPasses`

 Number of whole-level passes scheduled at each level, independently of the number of
  positions. 

### `Shape.sitePasses`

 Number of site-specific directory rows reserved per position at each level. 

### `Shape.scalarFields`

 Number of scalar words preceding the incidence and table pointers in a level header. 

### `Shape.tables`

 Number of rectangular slot-record tables reserved at each level. 

### `Shape.slots`

 Maximum number of slots reserved per position in a level's incidence columns and tables. 

### `Shape.fields`

 Number of words in a single slot record of a rectangular table. 

### `Layout`

 All levels use the initial position count as their rectangular capacity. 

### `Layout.shape`

 Fixed dimensions of the directory, level headers, incidence columns, and slot records. 

### `Layout.base`

 Starting address of the controller workspace that precedes the active frame and
  directory. 

### `Layout.positions`

 Initial position count used as the common rectangular capacity across levels. 

### `Layout.levels`

 Number of persistent level regions allocated after the directory. 

### `frameBase`

 Starting address of the active frame, nine words past the controller workspace base. 

### `plannerTag`

 Address reserved immediately after the active frame and immediately before the directory. 

### `directoryBase`

 Starting address of the first scheduler directory row, just past the planner tag cell. 

### `passesPerLevel`

 Number of directory rows per level, combining whole-level passes and site passes for every
position. 

### `directoryRows`

 Total directory row count for initialization and all allocated levels. 

### `levelsBase`

 Address of the first level header, after all fixed-width directory rows. 

### `levelHeaderWords`

 Size in words of the scalar header, six incidence pointers, and one pointer per table. 

### `slotCapacity`

 Number of slots available in a full level, obtained by multiplying positions by slots per
position. 

### `tableWords`

 Size in words of one rectangular table containing a fixed-width record for every reserved
slot. 

### `levelWords`

 Word stride between successive levels, including the header, all incidence columns, and all
tables. 

### `levelStart`

 Address of the header at the given zero-based level index. 

### `endAddress`

 First address beyond the final allocated level. 

### `scalarHead`

 Persistent level scalars, including vertex count, degree, row count,
residual lane count and the operands of the next refresh. 

### `incidenceHead`

 Pointers to the six incidence columns in the native directory order. 

### `tableHead`

 Pointers to the record tables of the particular compressor pass. 

### `incidenceStart`

 Address of the first incidence column immediately after this level's header. 

### `incidenceBase`

 Native scans pack the incidence columns with their actual row count. The
unused part of the reserved region stays available as blank space. 

### `arrayBase`

 Starting address of the rectangular tables after the six incidence columns of this level. 

### `tableBase`

 Starting address of the specified rectangular table within the level. 

### `Cell`

 Coordinates of a table word, indexed by table, position, slot, and record field. 

### `cellAddress`

 Site-major, slot-major, field-minor addressing within each array. 

### `headerIndex`

 Disjoint scalar, incidence-head and array-head fields, with a finite
equivalence giving their word offsets from the start of the level. 

### `tableEnd_le_tableBase`

 Consecutive table IDs give nonoverlapping physical intervals. 

### `olderLevel_preserved`

 A store in a later level cannot overwrite a word in an earlier level.
The statement applies to an entire chronological native event trace. 

### `level_room`

 The exclusive upper end and every intermediate level start fit under
one common bound. 

### `packedIncidence`

 Packed column heads as used by the typed incidence directory. 

### `ports`

 The native scheduler's published frame, directory and control addresses. 

### `Shape.fixedWords`

 One workspace prefix, before accounting for the per-level rows. 

### `Shape.levelFixed`

 Constant words per level, comprising header fields and level-wide pass rows. 

### `Shape.siteWords`

 Words per position at each level, including native directory rows,
six incidence columns and all rectangular slot records. 

### `endAddress_le`

 The allocated words are bounded by a fixed constant times positions
times levels whenever both counts are positive. 

### `cursorLayout`

 The initial level and one level per substep in the repeated block schedule. 

### `eventually_cursor_room`

 At the actual cursor dimensions the descriptor workspace and a polynomial
suffix, including their exclusive end cursors, fit in a word. The same threshold
also certifies the first native scan and its timestamps for every base/lane split. 
