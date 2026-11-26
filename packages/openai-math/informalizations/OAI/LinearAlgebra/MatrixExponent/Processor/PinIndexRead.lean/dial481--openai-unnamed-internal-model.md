---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Processor/PinIndexRead.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Processor/PinIndexRead.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Processor/PinIndexRead.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A compact index for the old processor inputs

An old physical bit is determined by its tape position and the lower
endpoint of its link. The quotient of the address by the link width
gives the sum of the endpoints modulo the number of processors.


### `portIndex`

 The numbering depends only on the coordinate and symbol, not on
the worker role or current report. 

### `decode`

 A literal emitted at this site always uses its own direct cell.
The second copy is suppressed even for a local literal. 

 # Agreement of batched reads with the message decoder 


# Metadata for a candidate pin

The tape position determines the label and literal offset. To decide
whether an old physical bit exists, only its matching number and
the proposed lower processor index are needed.


### `mode`

 Zero means absent, one means literal, and two means a private pin. 

### `query`

 Using a literal key even for a private pin gives the correct
destination, the only endpoint needed for that case. 

### `activity`

 Zero for absent cells, one for private cells and two for shared cells. 

 # Batched reads of static metadata depending on the worker identifier 

### `packed_pair`

 The reachability tests on source, destination and current site
form an arbitrary static table of at most `(3*r)^3` entries. 

 # Reading worker-specific pin metadata from small fixed tables 

### `packed_port`

 Any function of the worker's selected port can be tabulated before
the old processor index is attached to each copy. 

 # Reading class controls from the worker identifier and report 

 # Batched access to the counts and total widths of classes 

 # Static lookups on worker numbers and variable keys 
