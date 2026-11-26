---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordSlices.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordSlices.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordSlices.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Interval records for the compressor

Appendix E scans the widths in each of two ordered concatenations, then
intersects their fields in absolute coordinates. The output records name a
source and a target field and give their respective offsets and common length.
These computations never enumerate the individual bits of a payload.


### `Field`

 Position and extent of one field in an ordered concatenation. 

### `Field.index`

 Ordinal of this field within its ordered concatenation. 

### `Field.start`

 First absolute bit position of the field in the concatenation. 

### `Field.width`

 Number of consecutive bit positions belonging to the field. 

### `fieldsFrom`

 The prefix scan assigns absolute starts and consecutive field numbers. 

### `fieldsFrom_get`

 The field at a list position stores its width and the sum of all previous widths. 

### `fieldsFrom_bounds`

 All indices and interval endpoints stay inside the two running totals. 

### `Field.contains`

 Test membership of an absolute bit position in the field's half-open interval. 

### `SliceRecord`

 Each entry retains the two field references along with the three words
describing the contiguous copy. 

### `SliceRecord.source`

 The field in the source concatenation from which the intersection is copied. 

### `SliceRecord.target`

 The field in the target concatenation that receives the intersection. 

### `SliceRecord.slice`

 The source offset, target offset, and length of the overlapping bit interval. 

### `intersectFields`

 One comparison of field endpoints. Empty intersections generate no copy. 

### `candidates`

 Candidate field pairs in source-major order. 

### `copyRecords`

 Construct copy records by scanning the two lists of fields. 

### `candidates_length`

 The number of pair tests is independent of all numerical widths. 

### `copyRecords_length_le`

 At most one fixed-size record per pair of fields. 

### `copyRecords_bounds`

 All emitted records fit inside both named fields, including their offsets. 

### `SliceRecord.copies`

 Does this stored slice copy the bit with absolute index `x`? 

### `copyRecords_count`

 Exact coverage, counting *occurrences* of records. With equal total widths
every absolute bit is copied exactly once, including when some fields have width zero. 

### `copyRecords_index`

 A copied bit has one intra-slice index. Both relative addresses at this
index refer to that same absolute bit. 

### `readCopiedBit`

 Use a computed slice to read one bit, given access to old fields by number
and relative index. Only the selected old bit is requested. 

### `readCopiedBit_eq`

 The executable reader returns the old bit at the matching absolute
position in any repartition of the same total width. 

### `orderedField_mem`

 The list scan agrees with the abstract concatenation offset in the shrinking kernel. 

### `record_mem_of_overlap`

 Generate the stored slice for a pair of fields, whenever it has positive length. 

### `orderedWidths`

 The widths supplied to the descriptor scan by a numbered bundle. 

### `numberedField`

 Construct a field from its ordinal in the supplied order, the prefix width before it, and
its own width. 

### `demandBit_record`

 Every bit read by the actual AB demand kernel has its slice in the output of the scan. 

### `survivingSlice_read`

 The same scan, with one surviving wire on its source side, reads the
subdivision bits used by both endpoint maps of the shrinking step. 

### `refreshSegment_record`

 During a degree refresh the target list consists of one concatenated external word.
The generated descriptor for each nonempty source port gives precisely the offset at
which the local kernel reads its bit. 
