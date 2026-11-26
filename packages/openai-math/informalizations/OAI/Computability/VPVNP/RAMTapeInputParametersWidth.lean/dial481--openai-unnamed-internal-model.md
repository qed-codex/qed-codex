---
{
  "module": "OAI/Computability/VPVNP/RAMTapeInputParametersWidth.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeInputParametersWidth.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeInputParametersWidth.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Computing the incident-vector width on the validator's actual stacks

The address and bucket registers contain `d` and `H` in unary. The fixed program
forms `w = (d+10)^4`, counts the sorting layers, and writes the entire incident
width of equation (10.1). It returns both input registers and clears its scratch.


### `Port`

 Unary counters for the address, bucket, incident width, and intermediate arithmetic in the
layout-width calculation. 

### `initial`

 Start width computation with address width and bucket size on their counters and zero
elsewhere. 

### `result`

 Final width state containing the original address and bucket tallies and the complete
incident-vector width. 

### `wordProgram`

 Two squarings of `d+10`. Each multiply reads disjoint input stacks. 

### `words`

 Intermediate tallies for the address width plus ten, its square, and its fourth power,
which gives the word width. 

### `payloadProgram`

 Count `(d+1).choose 2` sorting layers and multiply by bucket and word widths. 

### `payloads`

 Intermediate counts for sorting layers, bucket slots across those layers, and their
word-width product. 

### `countProgram`

 Add the successor-field width and the sorting-field width into the output register. 

### `counted`

 State after writing the full incident width while the intermediate geometry tallies are
still present. 

### `cleanup`

 Erase the base, square, word, layers, blocks, and payload counters after storing the
incident width. 

### `program`

 A single fixed finite control, independent of `d` and `H`. 

### `work_program`

 The subroutines' exact instruction counts add across the four stages. 
