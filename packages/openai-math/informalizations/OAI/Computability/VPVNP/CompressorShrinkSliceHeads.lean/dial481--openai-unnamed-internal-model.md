---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkSliceHeads.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkSliceHeads.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkSliceHeads.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Computing the physical ports of a shrinking supply row

One fixed worker takes a dense motif-and-role cursor. It reads the absolute
old arc identifier, the fixed subdivision count and the stored layout bit,
then writes the seven operands of the supply, split and interval passes.


### `Public`

 The eleven public words supplying table bases and strides, selector width, and the
destination for one slice row’s seven operands. 

### `params`

 External term start and stride, absolute-ID and subdivision tables,
selected layout cell, width start and stride, interval start and stride,
selector width, and the destination for the seven physical operands. 

### `ops`

 Native code that decodes a motif-and-role cursor, reads the motif’s absolute ID, the role’s
subdivision count, and the layout bit, then writes the seven slice operands and advances
the cursor. 

### `dense`

 Dense motif index obtained by dividing the row cursor by the four roles per motif. 

### `role`

 Role index within the motif, given by the row cursor modulo four. 

### `readRow`

 Compute one row’s term address, supply operands, subdivision count, width destination, and
descriptor bank from the cursor and the three input table reads. 

### `words`

 The row header words in storage order are the term address, supply coordinate, selector
width, total address, piece count, width destination, and descriptor bank. 

### `report`

 Trace for one head-worker call, reading the absolute ID, subdivision count, and layout,
writing the seven header words, and returning the next row cursor. 

### `stored`

 The written header is contiguous and has no external effects elsewhere. 

### `readRow_exact`

 The fixed head worker addresses the same term and descriptor rows as
the simultaneous shrinking sweep. All input answers are actual external words. 

### `directory_input`

 The dense directory produced by the physical classified-port scatter
supplies the absolute index column required by the head worker. 

### `prepare`

 One physical row cursor prepares all worker operands from the dense
directory, the subdivision profile and the common layout bit. 
