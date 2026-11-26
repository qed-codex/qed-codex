---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkBundlePlan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkBundlePlan.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkBundlePlan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Dense shrinking visits between greedy preparation and term selection

The preliminary placement uses layout zero. Classification, append, gather
and rank work in the dyadic rank arena. After ranking, its gathered-key
rectangle becomes the absolute motif ID rectangle. Sorted widths, the two
prefixes and AB pieces occupy the consecutive width arena. The resulting
heads are the inputs to the motif demand and term planners.


### `thickCount`

 Number of thick fields per bundle, one quarter of the product of the color-word count and
the input degree. 

### `cap`

 Per-bucket capacity used throughout the shrinking rank and width rectangles at this degree
exponent. 

### `bundles`

 Compute the number of directed bundles from the base vertices, tag count, residual lanes
and input degree. 

### `preliminary`

 Address where preliminary placement begins, immediately after the greedy allocation. 

### `placementColumn`

 Base address of one of the four preliminary placement columns, each reserving one word per
old site. 

### `owner`

 Start of the old-port owner column following the four preliminary site columns. 

### `key`

 Start of the classifier-key column following the owner word for every old port. 

### `counts`

 First address of the per-bucket counts, following the old-port owner and key columns. 

### `bucketCount`

 Number of rank buckets, with one thick and one motif bucket for every directed bundle. 

### `ids`

 First address of the rectangle holding the appended old-port identifiers for the rank
buckets. 

### `rectangle`

 Total words in a rank rectangle, multiplying the number of thick and motif buckets by their
common capacity. 

### `gathered`

 Start of the gathered-key rectangle, reused for absolute identifiers once the ranks have
been computed. 

### `ranks`

 Start of the per-old-port rank column immediately following the gathered-key rectangle. 

### `sorted`

 First address of the sorted thick and motif width rectangles, after the rank column. 

### `blockSize`

 Words in one bundle-by-rank rectangle, for either the thick or the motif entries. 

### `absoluteCD`

 The expression for the CD absolute-ID rectangle head, one bundle-by-rank rectangle past the
gathered-key base. 

### `prefixStart`

 First address of the thick and motif prefix-offset rectangles, following both sorted-width
rectangles. 

### `totalStart`

 First address of the per-bundle totals for the thick and motif prefix scans. 

### `abStart`

 First address of the AB piece-width rectangle, following the per-bucket totals. 

### `termInputs`

 Collect the level dimensions, sorted widths, capacity and AB piece head needed by the
shrinking demand and term recipes. 

### `placementParams`

 The original greedy labels, full base displacements and a fresh four-column
output. Only the preliminary use fixes the layout operand to zero. 

### `classifyParams`

 The classifier's eleven public operands, including level dimensions, old incidence,
preliminary placement columns and the owner and key destinations. 

### `collectParams`

 Public operands for appending the old slots to their owner buckets, including counts,
capacity and the ID rectangle. 

### `gatherParams`

 Public operands for gathering the classified keys by bundle and rank, including the
thick-entry count and both rectangle heads. 

### `rankParams`

 Public operands for finding each old port's rank from its owner, key, bucket count and the
gathered-key rectangle. 

### `widthParams`

 Public operands for scattering old incidence widths into the sorted rectangle at each
port's owner and rank. 

### `absoluteParams`

 Public operands for replacing gathered keys by absolute identifiers, using owner, rank,
key, degree and residual-lane data. 

### `prefixParams`

 Select the width, start-offset and total columns for either the thick or the motif prefix
scan, together with its field count and row stride. 

### `abParams`

 The AB piece worker's capacity, row stride, input total column and output heads for piece
widths and starts. 

### `visits`

 Eleven chronological scans, each with its exact fixed instruction table,
return register, cursor bound and operand arity. 

### `Reads`

 Each expression in the setup uses the input level's published scalars and
the greedy arena already installed at the supplied origin. 

### `HeadValues`

 Evaluation of the bundle-plan expressions yields the physical placement columns, rank-arena
addresses and capacities for this input graph. 

### `absoluteBank`

 The two scattered classes reuse the gathered keys after the rank scan. 

### `absolute_layout`

 The old gather rectangle ends at the rank column. The other two inputs
(owner and key) end before that rectangle. This establishes the scatter's
frame without allocating another pair of rectangles. 

### `stop_counts`

 Cursor bounds in native order. The first position scan includes every old
site. Each subsequent classification or scatter visits the old arcs, while
the two prefix scans visit the populated parts of the thick and CD rows. 
