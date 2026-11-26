---
{
  "module": "OAI/Computability/VPVNP/PrimedInputRAMLayoutExecution.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMLayoutExecution.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMLayoutExecution.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native RAM histories for the two primed input passes

In Section 11 each internal bit has one owner in the first pass. The second
pass copies the owner's bit to every position that refers to it. For the
prescribed header memory, the accepting native histories are in bijection
with all internal assignments, and their reports recover the parser's input
at every site and bit offset.


### `cursorFits`

 The public cursor reaches both complete rectangles and the final halt. 

### `twoPass`

 Instantiate the two passes at the addresses of the primed tapes. 

### `inputProgram`

 The burst-RAM program that first chooses shared bits in the layout and then copies the
resolved input bits into their rows. 

### `inputReports`

 Native reports including the terminal call, for an internal assignment. 

### `inputReports_preserve_header`

 All prescribed words below the first scratch address survive both passes. 

### `cutLength_lt`

 Each of the three cut lengths fits in its header word. The exterior
lengths are bounded by the reserved header capacity and the middle length
by the number of sites in one rectangle. 

### `inputReports_cutLength`

 A fetch of any supplied cut length yields the exact natural number,
also after the choice and copy phases have run. 

### `inputPathEquiv`

 The bounded, accepting histories of this RAM enumerate the internal bits
with their full multiplicity. The site and bucket parameters here are those
of the auxiliary RAM, which may differ from the primed parameters. 

### `run_inputPath`

 Every path produces the reports of its decoded internal assignment. 

### `run_input_bits`

 At every leaf, the words written by the accepting run give the complete
primed parse input on its assignment, including the exterior header bits. 
