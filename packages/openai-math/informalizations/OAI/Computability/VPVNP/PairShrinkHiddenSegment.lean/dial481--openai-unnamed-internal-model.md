---
{
  "module": "OAI/Computability/VPVNP/PairShrinkHiddenSegment.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkHiddenSegment.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkHiddenSegment.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Hosting the absorbed-field scan inside the vertex image

The segment enters the header reader on the caller's live operands and
returns to the supplied continuation after the last owned field. It uses
the same register layout as the reset-entry program.


### `segmentCount`

 Number of instructions in the hosted scan segment, comprising the compiled header rows
followed by one row for each scan stage. 

### `segmentLoop`

 Host program counter for a scan stage, indexed in the segment after all compiled header
rows. 

### `segmentHeader`

 Host program counter for a compiled header row, with indices at or beyond the header length
directed to the scan's initialization. 

### `segmentInputs`

 The live source bank in the same layout as the four-operand preamble. 

### `segment`

 Vertex-image segment that prepares the scan from the caller's live operands, guesses the
owner's absorbed fields, and jumps to the supplied continuation. 

### `SegmentOperands`

 The host supplies four live operands in the protected six-register bank. 
