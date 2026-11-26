---
{
  "module": "OAI/Computability/VPVNP/CompressorSlotIncidence.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotIncidence.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotIncidence.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Expanding base incidence into the actual slot columns

The forward scan reads the base mate and the source arc's displacement. The
reverse scan first recovers the source from the inverse base permutation and
then reads that source's displacement. In both directions the lane changes by
one native XOR, since binary-vector translations are their own inverses.


### `visit`

 Public words are the degree, lane count, base permutation, displacement,
and actual incidence output heads. The persistent word is the actual port. 

### `events`

 Trace of one forward or reverse incidence visit, reading a base mate and the source arc's
displacement before writing the translated actual port. 

### `row_footprint`

 Each native visit reads a base mate and a source displacement, then writes
the current actual port. The reverse visit uses the stored mate as its source
index, so a range bound on that word suffices for both directions. 

### `run`

 Construct either actual incidence column over all positions, lanes and
slots. Every call uses two reads and one write, and preserves the input arrays. 
