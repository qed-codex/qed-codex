---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkInputTerms.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkInputTerms.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkInputTerms.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Selecting shrinking terms from a completed graph-input pass

The first free cell of the input construction is the dense demand head.
The next two cells per motif hold the AB/CD pair, followed by one strided
term descriptor per motif. The reports consume exactly the original
shrinking choices. Every cell of the completed graph-input arena survives
both scans, including its incidence directory, colors, offsets and old
field starts.


### `demandHead`

 Base address of the dense two-word demand pairs, immediately after the shrinking input
workspace. 

### `termHead`

 Base address of the term descriptors, immediately after one dense AB/CD demand pair per
motif. 

### `termEnd`

 Exclusive end of the descriptor array, allowing one row of the given stride after each
motif's demand pair has been allocated. 

### `thickBank`

 Prefix-scan operand bank for the thick-wire width rows in the completed shrinking input
arena. 

### `cdBank`

 Prefix-scan operand bank for the CD width rows in the completed shrinking input arena. 

### `piecesBank`

 Operand bank for splitting each bundle's width into its ordered AB pieces in the input
arena. 

### `pairBank`

 Six gather operands that pair the AB piece width with the CD width for each motif and
address the dense demand output. 
